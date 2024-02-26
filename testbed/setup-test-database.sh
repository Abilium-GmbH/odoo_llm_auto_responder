#!/bin/bash

# purge old test database volumes
docker volume ls -q | grep '^[0-9a-fA-F]\{64\}$' | xargs docker volume rm

docker-compose -p test_abilium_llm-f ./docker-compose-test.yml down --volumes
docker-compose -p test_abilium_llm -f ./docker-compose-test.yml up -d
docker logs test_abilium_llm-web-1 -f
