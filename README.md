# Host monitoring with psutil and fastapi libraries

get / - answer common host information  
get /cpu - answer detailed information about all cpu and percent usege separately  
get /disk - answer detailed information about all disks: mount point, size and percent usage  
get /process -answer detailed information about all processes: pid, owner, cpu usage.

## =Create for demonstration=

### Requires to work
Requires the following libraries to be installed:
* pip install fastapi[all]
* pip install uvicorn
* pip install psutil
