#!/bin/bash

docker build -t tests .
docker run --name homework --network selenoid tests pytest --browser chrome -n 2
docker cp homework:/app/allure-results .
allure serve allure-results
docker rm tests_run
