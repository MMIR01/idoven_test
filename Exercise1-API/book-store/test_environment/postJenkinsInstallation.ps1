Write-Host "Stopping docker container"
docker stop testenv

Write-Host "Copying jenkins jobs images"
# Update this value with your own path
$user_path = $env:USERPROFILE
$jenkins_folder = $user_path + "\Desktop\Programas\"
ECHO D | xcopy .\jenkins_config\config.xml $jenkins_folder\jenkinsdata\config.xml
ECHO D | xcopy .\jenkins_config\jobs\ $jenkins_folder\jenkinsdata\jobs\ /s /e /h

Write-Host "Start container again"
docker start testenv
