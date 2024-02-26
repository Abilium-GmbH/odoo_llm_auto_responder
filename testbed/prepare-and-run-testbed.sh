#!/bin/bash

git submodule init
git submodule update
docker-compose -f docker-compose.yml up

# after running this, you can access http://localhost:8069 and log in using admin:admin