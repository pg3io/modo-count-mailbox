FROM python:3.7

RUN pip install requests

RUN mkdir -p /app
WORKDIR /app

COPY ./modo-count.py /app

ENTRYPOINT [ "python3", "modo-count.py" ]