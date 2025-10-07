#!/bin/bash

set -e

black --line-length 120 src
ruff check src --fix
ruff format src
