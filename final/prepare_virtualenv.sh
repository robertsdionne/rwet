#/usr/bin/env bash

virtualenv venv
source venv/bin/activate
pip install nltk numpy scipy scikit-learn textblob
python -m textblob.download_corpora lite
