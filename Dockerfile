FROM python:3.8
RUN apt-get update && apt-get -y upgrade && apt-get -y install make && apt-get clean
WORKDIR /app
COPY app .
COPY requirements.txt .
COPY Makefile .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/bin/bash", "-c", "if [ $ENV = 'production' ] ; then make server ; else make dev-server ; fi"]