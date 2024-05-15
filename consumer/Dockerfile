# syntax=docker/dockerfile:1

ARG PYTHON_VERSION="3.12"
ARG ALPINE_VERSION="3.19"

FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION} as build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

RUN apk add --no-cache python3-dev libstdc++ g++ librdkafka librdkafka-dev
RUN pip install uv

COPY pyproject.toml ./
RUN uv venv $VIRTUAL_ENV && uv pip install -r pyproject.toml

FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

RUN addgroup -S app && adduser -S app -G app
USER app
WORKDIR /home/app

COPY --from=build --chown=app:app $VIRTUAL_ENV $VIRTUAL_ENV
COPY --chown=app:app src .

EXPOSE 8000
CMD ["uvicorn", "consumer.main:app", "--host", "0.0.0.0", "--proxy-headers"]
