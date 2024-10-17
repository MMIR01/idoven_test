Write-Host "Removing docker container"
docker stop testenv
$dockerid = docker ps -aqf "name=testenv"
docker rm $dockerid

Write-Host "Remove dangling images"
ECHO y | docker image prune

Write-Host "Copying needed folders"
$currentFolder = (pwd).path
cd..
ECHO D | xcopy .\test\configuration\* .\test_environment\configuration/s /e /h
ECHO D | xcopy .\test\datasets\* .\test_environment\datasets/s /e /h
ECHO D | xcopy .\test\test_suite\* .\test_environment\test_suite /s /e /h
cd $currentFolder

Write-Host "Updating docker image"
docker build -t testenvimage . -f DockerfileTest

# This is a persistent volume for Jenkins, so if we reset the container, the data is not lost
# Update this value with your own path
$user_path = $env:USERPROFILE
$jenkins_folder = $user_path + "\Desktop\Programas\"
Write-Host "Create volume"

docker volume create --opt type=none --opt o=bind --opt device=$jenkins_folder/jenkinsdata jenkinsdata

Write-Host "Run container"
# Expose docker socket so container can communicate with docker in the host
docker run -d --name testenv -p 8080:8080 -v $jenkins_folder/jenkinsdata:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -u root testenvimage

cd $currentFolder
Remove-Item .\configuration\ -Force -Recurse
Remove-Item .\datasets\ -Force -Recurse
Remove-Item .\test_suite\ -Force -Recurse