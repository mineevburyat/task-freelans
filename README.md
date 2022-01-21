# Host monitoring with psutil and fastapi libraries 
## Create for demonstration!
> main.py - fastapi server  
> shema.py - shema of answer json  
> monitoring.py - function which get host state sach as cpu, memory, disk, interface  

### get request and answer common host information
      get reuest : curl -X 'GET' \
      'http://127.0.0.1:8000/' \
      -H 'accept: application/json'
---
answer:
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
get /cpu - answer detailed information about all cpu and percent usege separately  
get /disk - answer detailed information about all disks: mount point, size and percent usage  
get /process -answer detailed information about all processes: pid, owner, cpu usage.



### Requires to work
Requires the following libraries to be installed:
* pip install fastapi[all]
* pip install uvicorn
* pip install psutil
