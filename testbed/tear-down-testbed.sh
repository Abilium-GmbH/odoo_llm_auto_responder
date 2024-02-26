#!/bin/bash

docker-compose -f docker-compose.yml down --volumes
docker-compose -p test_abilium_llm -f ./docker-compose-test.yml down --volumes
