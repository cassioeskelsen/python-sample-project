#!/bin/bash

uvicorn src.xpto.invoices.main:app --host 0.0.0.0 --port 8002