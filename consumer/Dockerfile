FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache python3-dev libstdc++ g++ librdkafka librdkafka-dev
RUN pip install uv

RUN addgroup -S app && adduser -S app -G app
USER app
WORKDIR /home/app

COPY --chown=app:app pyproject.toml ./
RUN uv venv && uv pip install -r pyproject.toml

COPY --chown=app:app src .

CMD ["python", "src/consumer"]
