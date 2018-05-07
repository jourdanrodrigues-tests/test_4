#!/usr/bin/env bash

CURRENT_DIR=$(dirname ${0})

if [ "${1}" == "prod" ]; then
  shift
  docker-compose -f docker-compose.prod.yml ${@}
else
  if [ ! -d ${CURRENT_DIR}/frontend_app/node_modules ]; then
    # The development volume makes it ignore the "node_modules" folder
    cd ${CURRENT_DIR}/frontend_app
    npm i
    cd ..
  fi
  docker-compose ${@}
fi
