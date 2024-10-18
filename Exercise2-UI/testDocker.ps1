Write-Host "Removing docker container"
docker stop cypresstest
$dockerid = docker ps -aqf "name=cypresstest"
docker rm $dockerid

Write-Host "Remove dangling images"
ECHO y | docker image prune

Write-Host "Updating docker image"
docker build -t cypress/included:13.14.2 . -f Dockerfile

Write-Host "Run container"
docker run -it --entrypoint=/bin/bash --name cypresstest cypress/included:13.14.2 