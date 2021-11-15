#!/bin/bash

uvicorn src.xpto.orders.main:app --host 0.0.0.0 --port 8001