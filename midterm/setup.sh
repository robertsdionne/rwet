#!/usr/bin/env bash

# exit on error
set -e


# setup virtualenv
virtualenv ../venv
source ../venv/bin/activate


# install editdistance module
CFLAGS=-Qunused-arguments CPPFLAGS=-Qunused-arguments pip install editdistance
