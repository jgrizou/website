#!/bin/bash

PWD=$(pwd)
DIR=$(dirname $0)
FILEPATH="$PWD/$DIR"

cd ${FILEPATH}

cd bin
python -m SimpleHTTPServer

cd ${FILEPATH}
