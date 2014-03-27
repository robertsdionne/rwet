#!/usr/bin/env bash

# exit on error
set -e

virtualenv ../venv
source ../venv/bin/activate
CFLAGS=-Qunused-arguments CPPFLAGS=-Qunused-arguments pip install editdistance
