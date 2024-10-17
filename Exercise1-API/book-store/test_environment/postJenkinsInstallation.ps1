Write-Host "Stopping docker container"
docker stop testenv

Write-Host "Copying jenkins jobs images"
ECHO D | xcopy .\jenkins_config\config.xml .\jenkinsdata\config.xml
ECHO D | xcopy .\jenkins_config\jobs\ .\jenkinsdata\jobs\ /s /e /h

Write-Host "Start container again"
docker start testenv
