from shema import Memory, Disk, Interface, CommonInfo
import datetime, psutil,socket

def _getUptime():
  return datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())

def getMemory():
  return Memory(**psutil.virtual_memory()._asdict())

def getDiskList():
  disks = []
  for disk in psutil.disk_partitions():
    disks.append(Disk(**disk._asdict()))
  return disks

def getInterfaceList():
  interfaces = []
  for if_name, if_status in psutil.net_if_stats().items():
    interface = Interface(name=if_name, upstatus=if_status.isup, speed=if_status.speed)
    interfaces.append(interface)
  return interfaces

def getInfo():
  return CommonInfo(hostname = socket.gethostname(),
    uptime = _getUptime(), 
    cpu_core = psutil.cpu_count(True),
    cpu_load = psutil.cpu_percent(interval=1),
    memory = getMemory(),
    disks=getDiskList(),
    iflist = getInterfaceList())

def updateInfo(hostconf):
  hostconf.uptime = _getUptime()
  hostconf.cpu_load = psutil.cpu_percent()
  hostconf.memory = getMemory()
  return hostconf
