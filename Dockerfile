FROM python:alpine

LABEL maintainer="piotr.modlinger@gmail.com"

ADD . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 81

ENTRYPOINT ["python", "app.py"]
