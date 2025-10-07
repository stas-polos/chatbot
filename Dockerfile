ARG PYTHON_IMAGE_VERSION

FROM python:${PYTHON_IMAGE_VERSION}

# last poetry version: https://github.com/python-poetry/poetry
ARG POETRY_VERSION=2.2.0

RUN apt-get update -yq && apt-get install -yq --no-install-recommends \
    curl \
    ; \
    apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | python - --version ${POETRY_VERSION}
ENV PATH="${PATH}:/root/.local/bin"

COPY pyproject.toml poetry.lock /app/
WORKDIR /app

RUN poetry config virtualenvs.create false \
    && poetry install \
    && rm -rf ~/.cache/pypoetry \
    ;

COPY src/ /app/src/
COPY scripts/ /app/scripts
