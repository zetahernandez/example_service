FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y \
        curl \
        wget \
        vim-nox \
        git-core \
        sudo \
        dnsutils \
        python3 \
        python3-pip \
        python3-setuptools \
        build-essential \
        openssl \
        libssl-dev \
        libyaml-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install --upgrade pip setuptools flake8 ipdb

WORKDIR /srv/example_client

ADD . /srv/example_client/
RUN pip3 install pysoa

ENTRYPOINT ["/bin/bash"]
