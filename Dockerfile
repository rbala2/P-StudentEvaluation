FROM python:3.7-alpine

ADD aws_service_package/ /aws_services_package

WORKDIR /working

RUN pwd

RUN ls -lrt

RUN apk --update add --virtual build-dependencies python py-pip openssl ca-certificates py-openssl wget libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del build-dependencies

ENTRYPOINT ["python" , "manage.py", "runserver"]

