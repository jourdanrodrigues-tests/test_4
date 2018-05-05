#!/usr/bin/env bash

if [ "${1}" == "prod" ]; then
  shift
  docker-compose -f docker-compose.prod.yml ${@}
else
  docker-compose ${@}
fi
