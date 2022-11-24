FROM python:3.10.5-alpine3.15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install "poetry==1.2"

RUN mkdir -p /var/www/
WORKDIR /var/www/

COPY poetry.lock pyproject.toml /var/www/

RUN apk update \
    && apk add curl postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

EXPOSE 8080