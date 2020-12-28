FROM python:3.7

WORKDIR /app

RUN pip install poetry
COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install