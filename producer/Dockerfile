FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PDM_CHECK_UPDATE=false
ENV PATH="/home/app/.venv/bin:${PATH}"
RUN pip install -U pdm

RUN addgroup -S app && adduser -S app -G app
USER app
WORKDIR /home/app

COPY --chown=app:app pyproject.toml pdm.lock ./
RUN pdm install --check --prod --no-editable

COPY --chown=app:app src .

CMD ["python", "src/producer"]
