FROM python:3.8-slim

COPY requirements.txt /tmp/


RUN pip3 install --upgrade pip && pip3 install -r /tmp/requirements.txt && useradd --create-home appuser

ADD . /usr/src/app
WORKDIR /usr/src/app
USER appuser

CMD [ "python", "app.py" ]