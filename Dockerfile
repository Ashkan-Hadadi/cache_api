FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /cache_api

COPY requirements.txt /cache_api/
RUN pip install -r requirements.txt

COPY . /cache_api

EXPOSE 8000

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
