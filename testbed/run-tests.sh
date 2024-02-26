#!/bin/bash

container_id=$(docker-compose -f ./docker-compose-test.yml -p test_abilium_llm run -d web --test-enable --test-tags invoice --stop-after-init -d test -u odoo_llm_auto_responder)
docker logs $container_id -f
docker rm $container_id
