Write-Host "Removing docker container"
docker stop testenv
$dockerid = docker ps -aqf "name=testenv"
docker rm $dockerid

Write-Host "Remove dangling images"
ECHO y | docker image prune

Write-Host "Copying needed folders"
$currentFolder = (pwd).path
cd..
ECHO D | xcopy .\configuration\* .\test_environment\configuration/s /e /h
ECHO D | xcopy .\datasets\* .\test_environment\datasets/s /e /h
ECHO D | xcopy .\test_suite\* .\test_environment\test_suite /s /e /h
cd $currentFolder

Write-Host "Updating docker image"
docker build -t testenvimage . -f DockerfileTest

Write-Host "Create volume"
docker volume create --opt type=none --opt o=bind --opt device=$currentFolder/jenkinsdata jenkinsdata

Write-Host "Run container"
docker run -d --name testenv -p 8080:8080 -v jenkinsdata:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -u root testenvimage
# Run as root to avoid permission issues
#docker run -itd -e JENKINS_USER=$(id -u) \
#-v /var/run/docker.sock:/var/run/docker.sock \
#-v $(pwd)/jenkins_home:/var/jenkins_home \
#-v $(which docker):/usr/bin/docker \

cd $currentFolder
Remove-Item .\configuration\ -Force -Recurse
Remove-Item .\datasets\ -Force -Recurse
Remove-Item .\test_suite\ -Force -Recurse