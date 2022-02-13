#!/bin/sh
cd /opt/celery/task-freelans/fastapi_math
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4