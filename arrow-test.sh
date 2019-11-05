#!/bin/bash

export ARROW_GLOBAL_CONFIG_PATH=`pwd`/test-data/arrow.yml
./bootstrap_apollo.sh
python setup.py nosetests
