#!/bin/bash

set -e

poetry run black --line-length 120 src
poetry run ruff check src --fix
poetry run ruff format src
