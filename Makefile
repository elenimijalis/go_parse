all: go.obo
	python go_parse.py go.obo

go.obo:
	wget -O go.obo http://geneontology.org/ontology/go.obo
