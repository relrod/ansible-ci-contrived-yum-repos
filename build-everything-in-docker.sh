#!/usr/bin/env bash

set -eux

docker build -t ansible-ci-contrived-yum-repos:latest .
docker run --rm -v "$(pwd)/repos:/mnt/:z" ansible-ci-contrived-yum-repos:latest ./build-everything.sh
