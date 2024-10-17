# Book Store REST API

## Table of Contents
- [Test Strategy](#test-strategy)
- [Software Requirements](#software-requirements)
- [Prerequisites](#prerequisites)
- [Program structure](#program-structure)
- [Server Installation](#server-installation)
- [Test Environment Installation](#test-environment-installation)
- [Test Suite](#test-suite)
- [Test Execution](#test-execution)

## Test Strategy
For this task, I decided to containerize the server (bookstore_apy.py). A container will give us a big flexibility, so we can reset the container when it is a code change, and also we can separate the test and the production environment.
This implies changing the api code. It is necessary to bind flask with `0.0.0.0` in the run command from the main.
Without the separation between the server and the test environment, we could have used:
```bash
#from api.bookstore_api import app, books
```
So you could use `app` to interact directly with the server without creating a socket. Also, you could use books to delete the database.
However, we have to use http request to create a socket and interact with the server. Although this is a bit more laborious, I think it is a more realistic testing approach.

Our tests are based on pytest and they are going to exercise all the resources of the bookstore api. This is, covering all the CRUD operations for both nominal and non-nominal situations.

Our test environment is going to consist on a Jenkins machine that is going to have a pipeline with the following stages:
1. git pull the code from the GitHub server
2. Deploy a new server container with the changes
3. Run all the pytests
4. Publish the report (inside Jenkins)

For our test environment, I also containerize the solution

## Software Requirements
For this task I have used the following stack:
- Windows 10 (it hasn't been tested on different OS versions)
- Powershell


## Prerequisites
In order to use Docker Desktop, WSL is needed. To install it:

```bash
wsl --install
```

If you find this error `WslRegisterDistribution failed with error: 0x80370102` try to disable and then enable Windows Virtual Platform from Programs and Features

Install Docker Desktop for Windows from the official webpage. In my case, it has installed Docker version 27.1.1, build 6312585

When Docker Desktop is opened, please download python 3.90.20 slim


## Program structure
The Exercise1-API folder contains the following files:

```bash
|   +--- README.md
|   +--- server
|   |   +--- api
|   |   |   +--- bookstore_api.py > code provided by Idoven
|   |   +--- DockerfileServer > Docker File used to configured the server
|   |   +--- poetry.lock
|   |   +--- poetry.toml
|   |   +--- pyproject.toml
|   |   +--- serverDocker.ps1 > script executed to run the server
|   +--- test
|   |   +--- configuration
|   |   +--- datasets
|   |   +--- test_suite
|   |   |   +--- nominal_tests
|   |   |   +--- non_nominal_tests
|   |   |   +--- test_cases.xlsx > contain a description of all the tests
|   |   |   +--- test_execution_20241017.xlsx > results of a test execution
|   +--- test_environment > contains files to deploy a container with Jenkins
+--- Exercise1-instructions.md
```

## Server installation
Download the official python3.10.6 image. For that, open a Powershell terminal and execute:
```bash
docker pull python:3.10.6-slim
```

In the Powershell terminal, execute the script called `serverDocker.ps1` inside the server folder. The script will create a new image called `bookstoreimage`, and a new container called `bookstoreserver`. The script can be also used to update the image when there are some code changes. It is using the `DockerFile` provided

If you can't execute the script, please try the following with Powershell:
```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser .\serverDocker.ps1
```

Check the image is running. For that, go to Docker Desktop > containers, or in Powershell:
```bash
docker ps
```

Check the server is up and running. Open a web browser and type:
```http://127.0.0.1:5000/books```

You should see an empty HTML without errors

Note:
Poetry is used to install the server api but it is automatically done in the docker file

## Test Environment Installation
Download Jenkins image [here](https://hub.docker.com/r/jenkins/jenkins). Or as alternative, in the Powershell type:
```bash
docker pull jenkins/jenkins
```
Note: make sure is jenkins/jenkins


Go to the `test_environment` and open the script called `testDocker.ps1`. Update the `jenkins_folder` variable with an appropiate value for your machine (it has to be a different folder where the git repository is). Repeat the same with `postInstallation.ps1`. After that, open the powershell and execute the test. The script will create a new image called `testenvimage`, and a new container called `testenv`.

In summary, this script will:
- Remove any test environment previously created 
- Create a new test env image (using the `Dockerfile` provided)
- Create a new volume, so all the test data can be persistent
- Run a new container (port 8080)

The script can be also used to update the image when there are some changes in the environment

If you can't execute the script, please try the following with Powershell:
```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser .\updateDockerTest.ps1
```

Check the image is running. For that, go to Docker Desktop > containers, or in Powershell:
```bash
docker ps
```

When the script finishes, open: ```http://localhost:8080/```

(it might take a few minutes until Jenkins is up and running)

Jenkins will request a password. To get it, execute:
```bash
docker ps # (to get the current container id)
docker exec <container_id> cat /var/jenkins_home/secrets/initialAdminPassword
```
Note: you can also see the password in the console output of the container from the Docker Desktop

After that:
- Click on "Select plugins to install"
- Click on: JUNIT
- Click on: Install

Wait until the installation finished.

Create admin user. I have used the following data:
- User: test1
- Pass: 123456
- Full name: Test1
- Email address: test1@test.com

Click on:
- Save and Continue
- Save and Finish
- Start using Jenkins

Execute the ```postInstallation.ps1``` script provided in the ```test_environment``` folder. It will:
- Stop Jenkins container
- Copy the provided Jobs (they contain the commands to run the tests)
- Start Jenkins container again

After that, Jenkins will reload the page (it can take a few minutes to startup). Introduce the login details.

You will see Jenkins with all the jobs installed.

There are a few more things to configure:
1. Install plugin. Go to Manage Jenkins > Plugins > Available Plugins. And search for this one:
- Multibranch Scan Webhook Trigger
- Select it, and click on Install
2. Create a personal token for your Github account
- Make sure credentials have: admin:org_hook scope
- Don't forget to copy it once created
3. Create a credential (necessary to link GitHub with Jenkins). From Jenkins:
- Jenkins > Manage Jenkins > Credentials > Domains > click on global > Add credential
- Type: username with password.
- username: <your github username>
- password: <token>
- ID: idoven_token
4. Open the configuration of each job, and make sure the "Git" section is using the credential configured
5. Expose Jenkins to the Internet so GitHub can send the webhook.
- Go to `https://ngrok.com/` and create a Developer account. Follow the instructions to download and install the app.
- Click on ngrok.exe. It opens a terminal. Type: 
```bash
ngrok http http://localhost:8080
```
- It will put your Jenkins available online. In my case under this IP:
https://f673-46-6-27-120.ngrok-free.app
6. Webhook. We need a webhook in order to trigger an automatic build after a new commit in the repository. For that, from the repository page in GitHub:
- Click on settings > WebHooks
- Add a new one
- Payload URL: <the generated ULR above>//multibranch-webhook-trigger/invoke?token=idoventoken

The current pipeline is configured to use the following repository:
`https://github.com/MMIR01/idoven_test`
It will scan all the branch availables, and will trigger an execution when receive a webhook


## Test Suite
As part of the task there are a bunch of tests written with pytest in order to test the serverAPI. These tests can be found in the ```test\test_suite``` folder. 

To have more information about the tests, I really recommend to check this document:
```test\test_suite\test_cases.xlsx```

## Test Execution
There are three ways to execute the tests:
1. From the pipeline. 
- Open Jenkins. Click on the "play" button for the pipeline job. It will deploy a new server container and will run the tests.
2. From Jenkins. Open Jenkins and execute the desired job:
- Execute all tests
- Execute nominal tests
- Execute non-nominal tests
3. Manually from your host machine:
- Go to the test folder and execute:
```bash
python -m pytest 
# Nominal tests
cd nominal_tests
python -m pytest
# Specific test
python -m pytest test_get.py
```
4. From your test machine execute. Same as above, but inside the docker container
```bash
# In a powershell
docker exec -it testenv sh
cd /code/test_suite
# Same instructions as step 3
python3 -m pytest
```

I did a test execution before deliverying this solution. The logs have not been attached, but I have commited the file `test_execution_20241017.xlsx` that includes the results.
