# Testing in 'DebugBear' Site
## Table of Contents
- [Features](#features)
- [Software Requirements](#software-requirements)
- [Prerequisites](#prerequisites)
- [Test Environment Installation](#test-environment-installation)
- [Test Suite](#test-suite)
- [Test Execution](#test-execution)

## Test Strategy
For this task, I also decided to containerize the test environment. I will use Cypress for the GUI testing as it is very easy to set up and use. For the GUI testing, I am going to use the default browser coming with the installation (Electron), although Cypress can be configured to use different browsers. In fact, that is the best approach: test the GUI for each browser. However, for the purpose of this task, one browser is enough.

In order to write the test, it is very important to carry out some "exploratory tests", to find out how the webpage is, as well as the DOM elements necessary for the tests. I will explore both positive and negative scenarios.

As a note, on the main page, I only considered the "blue box" that is part of the webpage related to the web speed test. I ignored other info like "pricing, blog, etc." as it is out of the scope. Also, we are using the free version without signing up any user to simplify the task.

## Software requirements
For this task I have used the following stack:
- Windows 10 (it hasn't been tested on different OS versions)
- Powershell

## Prerequisites
In order to use Docker Desktop, WSL is needed. To install it:
```
wsl --install
```

If you find this error `WslRegisterDistribution failed with error: 0x80370102` try to disable and then enable `Windows Virtual Platform` from `Programs and Features`

Install Docker Desktop for Windows from the  [official webpage](https://docs.docker.com/desktop/install/windows-install/). In my case, it has installed Docker version 27.1.1, build 6312585

## Test Environment Installation
In the powershell terminal, type:
```sh
docker pull cypress/included:13.14.2
```

## Test suite
As part of the task there are a bunch of tests written with Cypress in order to test the GUI. These tests can be found in the `automation` folder. To have more information about the tests, I really recommend to check this document:
```test\test_cases.xlsx```

## Test execution
Go to this folder: `automation`. Execute:

```sh
docker run --rm -it -v .:/exec -w /exec cypress/included:13.14.2
```

As an alternative, we can use the DockerFile provided in order to create an interactive container, so we can run the tests from there. For that, in the Powershell terminal, execute:
```sh
.\testDocker.ps1
```

Because the entry point is now bash, we can execute manually the tests via the command line, for that, from `automation` folder, execute:
```sh 
cypress run
```

If you want to run a specific test:
```sh 
cypress run --spec <path_to_the_spec.js_file>
```

I did a test execution before deliverying this solution. The logs have not been attached, but I have commited the file `test_execution_20241018.xlsx` that includes the results.
