#!/bin/bash

set -e
set -x

mypy src
ruff check src
ruff format src --check
