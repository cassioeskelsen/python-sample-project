#!/bin/bash

gunicorn -b 0.0.0.0:8000 src.xpto.api.main:app -w 2 \
        -k uvicorn.workers.UvicornWorker