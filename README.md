Скопировать celery.service в /etc/systemd/system/celery.service
systemctl deamon-reload
systemctl enable celery.service
systemctl enable celery.service

# Host monitoring with psutil and fastapi libraries 
## Create for demonstration!
> main.py - fastapi server  
> shema.py - shema of answer json  
> monitoring.py - function which get host state sach as cpu, memory, disk, interface  

### get request and answer common host information
_get request:_  

      curl -X 'GET' \
      'http://127.0.0.1:8000/' \
      -H 'accept: application/json'
---
_answer:_  

      {
      "hostname": "string",
      "uptime": 0,
      "cpu_core": 0,
      "cpu_load": 0,
      "memory": {
        "total": 0,
        "available": 0,
        "percent": 0,
        "used": 0,
        "free": 0
      },
      "disks": [
        {
          "device": "string",
          "mountpoint": "string",
          "fstype": "string",
          "opts": "string"
        }
        ],
      "iflist": [
        {
          "name": "string",
          "upstatus": true,
          "speed": 0
        }
        ]
}  

For read all request and respons use documentations:  
      http://127.0.0.1/docs  
      http://127.0.0.1/redoc



### For use project
Requires the following libraries to be installed:
* pip install fastapi[all]
* pip install uvicorn
* pip install psutil  

After installetions run it:  

* python main.py - start application in console mode with info debug
* uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 - start with workers on multiprocessor product host
* gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 - i dont now why
