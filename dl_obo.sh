#!/bin/sh
rm -f go.obo && \
wget -O go.obo http://geneontology.org/ontology/go.obo && \
python go_parse.py
