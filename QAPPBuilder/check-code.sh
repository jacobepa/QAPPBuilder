#!/bin/bash
# check-code.sh
docker-compose run django flake8
docker-compose run django black --check .
docker-compose run django isort --check-only .