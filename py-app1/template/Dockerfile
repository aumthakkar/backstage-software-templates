FROM python:3.12-alpine

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./src /src

ENTRYPOINT python /src/${{values.app_name}}.py
