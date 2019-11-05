FROM python:3.7
MAINTAINER Nathan Dunn <nathandunn>, Anthony Bretadeau <abretaud>, Helena Rasche <erasche>
ENV DEBIAN_FRONTEND noninteractive


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python setup.py install


RUN apt-get -qq update --fix-missing && \
	apt-get --no-install-recommends -y install \
	docker git build-essential wget apt-utils \
	curl ssl-cert zip unzip sudo


# TODO: maybe move to a separate script to be called with docker run python-apollo:latest test-apollo
RUN pip install -U pip setuptools nose
RUN export ARROW_GLOBAL_CONFIG_PATH=`pwd`/test-data/arrow.yml
# RUN ./bootstrap_apollo.sh
# RUN python setup.py nosetests






