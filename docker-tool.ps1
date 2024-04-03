# Docker tool
# PowerShell script for building, running, and stopping a docker container
# version: 1.0

# run from the command line
# .\docker-tool.ps1 [command]
# command: build, run, stop, check, rm (remove dockers)
# example: .\docker-tool.ps1 build


# ----------------- Functions -----------------

# function for building
function dockerBuild {
    Write-Host "Building docker image..."
    #check if image exists
    $imageExists = docker images -q larpex-backend-app

    if ($imageExists) {
        Write-Host "Docker image already exists. Removing the image..." -ForegroundColor Yellow
        # stop dockers
        docker stop (docker ps -a -q --filter ancestor=larpex-backend-app)
        # remove dockers
        docker rmi larpex-backend-app
    }
    docker build -t larpex-backend-app .
    Write-Host "Docker image built. Run the container with the 'r' command." -ForegroundColor Magenta
}

# function for running
function dockerRun {
    Write-Host "Running docker container..."
    #check if container exists than run it    
    $containerExists = docker ps -a --filter ancestor=larpex-backend-app
    if ($containerExists) {
        Write-Host "Docker container already exists. Removing the container..." -ForegroundColor Yellow
        # stop dockers
        docker stop (docker ps -a -q --filter ancestor=larpex-backend-app)
        # remove dockers
        docker rm (docker ps -a -q --filter ancestor=larpex-backend-app)
    }
    docker run -d -p 8000:8000 larpex-backend-app
    Write-Host "Check if the container is running with the 'c' command." -ForegroundColor Magenta
}

# function for stopping
function dockerStop {
    Write-Host "Stopping docker container..."
    docker stop (docker ps -a -q --filter ancestor=larpex-backend-app)
    Write-Host "Docker container stopped." -ForegroundColor Magenta
}

function removeDockers {
    Write-Host "Removing docker containers of larpex-backend-app..."
    #stop dockers
    docker stop (docker ps -a -q --filter ancestor=larpex-backend-app)
    docker rm (docker ps -a -q --filter ancestor=larpex-backend-app)
    #remove images
    docker rmi larpex-backend-app
    Write-Host "Docker containers removed." -ForegroundColor Magenta
}

function checkIfRunning {
    Write-Host "Checking if container is running..."
    docker ps -a --filter ancestor=larpex-backend-app
}


# ----------------- Main -----------------

$command = $args[0]
$usageStart = "Usage: docker-tool.ps1 [command]"
$usageExplanation = "commands: build, run, stop, check, rm (remove dockers)"
$usageExample = "example: docker-tool.ps1 build"
$warning = "Warning: Make sure you have Docker installed and running."

switch ($command) {
    "build" { dockerBuild }
    "run" { dockerRun }
    "stop" { dockerStop }
    "check" { checkIfRunning }
    "rm" { removeDockers }
    default { Write-Host $usageStart -ForegroundColor Cyan; 
        Write-Host $usageExplanation -ForegroundColor Cyan;
         Write-Host $usageExample -ForegroundColor Magenta;
          Write-Host $warning -ForegroundColor Yellow; break }
}