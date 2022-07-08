#!/usr/bin/env bash

pip install -r requirements.txt && pytest -s -W ignore::DeprecationWarning


