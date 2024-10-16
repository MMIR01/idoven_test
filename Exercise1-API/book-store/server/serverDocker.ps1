
Write-Host "Removing docker container"
docker stop bookstoreserver
$dockerid = docker ps -aqf "name=bookstoreserver"
docker rm $dockerid

Write-Host "Remove dangling images"
ECHO y | docker image prune

Write-Host "Updating docker image"
docker build -t bookstoreimage . -f DockerfileServer

Write-Host "Run container"
docker run -d --name bookstoreserver -p 5000:5000 bookstoreimage