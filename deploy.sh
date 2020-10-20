#!/bin/bash

# this script calls several docker-compose
docker-compose down
docker-compose pull
docker-compose up -d
docker-compose ps