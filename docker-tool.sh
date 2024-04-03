#!/bin/bash

# Docker tool
# Shell script for building, running, and stopping a docker container
# version: 1.0, automatic conversion from PowerShell version

# run from the command line
# ./docker-tool.sh [command]
# command: build, run, stop, check, rm (remove dockers)
# example: ./docker-tool.sh build

# ----------------- Functions -----------------

# function for building
dockerBuild() {
    echo "Building docker image..."
    # check if image exists
    if [ "$(docker images -q larpex-backend-app)" ]; then
        echo "Docker image already exists. Removing the image..." 
        # stop dockers
        docker stop $(docker ps -a -q --filter ancestor=larpex-backend-app)
        # remove dockers
        docker rmi larpex-backend-app
    fi
    docker build -t larpex-backend-app .
    echo "Docker image built. Run the container with the 'run' command."
}

# function for running
dockerRun() {
    echo "Running docker container..."
    # check if container exists then run it    
    if [ "$(docker ps -a --filter ancestor=larpex-backend-app)" ]; then
        echo "Docker container already exists. Removing the container..." 
        # stop dockers
        docker stop $(docker ps -a -q --filter ancestor=larpex-backend-app)
        # remove dockers
        docker rm $(docker ps -a -q --filter ancestor=larpex-backend-app)
    fi
    docker run -d -p 8000:8000 larpex-backend-app
    echo "Check if the container is running with the 'check' command."
}

# function for stopping
dockerStop() {
    echo "Stopping docker container..."
    docker stop $(docker ps -a -q --filter ancestor=larpex-backend-app)
    echo "Docker container stopped."
}

# function for removing dockers
removeDockers() {
    echo "Removing docker containers of larpex-backend-app..."
    # stop dockers
    docker stop $(docker ps -a -q --filter ancestor=larpex-backend-app)
    docker rm $(docker ps -a -q --filter ancestor=larpex-backend-app)
    # remove images
    docker rmi larpex-backend-app
    echo "Docker containers removed."
}

# function for checking if container is running
checkIfRunning() {
    echo "Checking if container is running..."
    docker ps -a --filter ancestor=larpex-backend-app
}

# ----------------- Main -----------------

command="$1"
usageStart="Usage: ./docker-tool.sh [command]"
usageExplanation="commands: build, run, stop, check, rm (remove dockers)"
usageExample="example: ./docker-tool.sh build"
warning="Warning: Make sure you have Docker installed and running."

case "$command" in
    "build") dockerBuild ;;
    "run") dockerRun ;;
    "stop") dockerStop ;;
    "check") checkIfRunning ;;
    "rm") removeDockers ;;
    *) echo "$usageStart" && echo "$usageExplanation" && echo "$usageExample" && echo "$warning" && exit 1 ;;
esac
