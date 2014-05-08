#/usr/bin/env bash

# create, activate and install dependencies into a virtual environment
virtualenv venv
source venv/bin/activate
pip install nltk numpy scipy scikit-learn textblob
python -m textblob.download_corpora lite
