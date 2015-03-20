#!/bin/bash

SOURCE_PATH=$( cd "$PWD/${BASH_SOURCE[0]%/*}"; pwd )
cd "$SOURCE_PATH/.."

./astrond --loglevel info config/cluster.yml
