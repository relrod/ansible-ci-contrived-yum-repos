#!/usr/bin/env bash

set -eux

for dir in ./*/; do
  pushd "$dir"
    ./build-rpms.sh
  popd
done
