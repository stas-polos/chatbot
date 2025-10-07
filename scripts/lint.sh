#!/bin/bash

set -e
set -x

poetry run mypy src
poetry run ruff check src
poetry run ruff format src --check
