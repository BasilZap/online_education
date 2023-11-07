
FROM python:3.11

WORKDIR /project

COPY ./requirements.txt /project/

RUN pip install -r /project/requirements.txt

COPY . .