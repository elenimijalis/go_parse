FROM nginx
RUN apt-get update -qq && \
    apt-get install -y wget python

RUN wget -O go.obo http://geneontology.org/ontology/go.obo

ADD go_parse.py /go_parse.py

RUN mkdir /go && \
    python /go_parse.py /go.obo --outdir /go

ADD server.conf /etc/nginx/conf.d/default.conf
