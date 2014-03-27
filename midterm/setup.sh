#!/usr/bin/env bash

virtualenv ../venv
source ../venv/bin/activate
CFLAGS=-Qunused-arguments CPPFLAGS=-Qunused-arguments pip install editdistance
