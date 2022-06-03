#!/bin/bash
app="docker.test"
docker build -t ${app} .
docker run -d -p 11123:5000 \
  -it \
  --rm \
  --name=${app} \
  -v $PWD:/var/www/server ${app}

