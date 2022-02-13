#!/bin/bash
cd fastapi_psutil
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2 > /var/log/fastapi_psutil.log 2>&1 &
cd ../fastapi_math
celery -A calcpicelery worker -l info -c 2 > /var/log/celery.log 2>&1 &
uvicorn main:app --host 0.0.0.0 --port 8001 --workers 2 > /var/log/fastapi_math 2>&1