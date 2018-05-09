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

ENV PYSOA_SETTINGS_MODULE example_service.settings.dev

RUN echo 'alias rs="python3 -m example_service.standalone -s example_service.settings.dev"' >> ~/.bashrc

WORKDIR /srv/example_service

ADD . /srv/example_service/
RUN pip3 install -e /srv/example_service[testing]

ENTRYPOINT ["python3", "-m", "example_service.standalone"]
CMD ["-s", "example_service.settings.dev", "-f", "5", "--use-file-watcher", "example_service,pysoa,conformity"]
