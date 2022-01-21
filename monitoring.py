from shema import Memory, Partitions, Interface, CommonInfo, PhisicalDiskCount
import datetime, psutil,socket

def _getHostname():
  return socket.gethostname()

def _getUptime():
  return datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())

def getMemory():
  return Memory(**psutil.virtual_memory()._asdict())

def getPartList():
  parts = []
  for partitions in psutil.disk_partitions():
    parts.append(Partitions(**partitions._asdict()))
  return parts

def getInterfaceList():
  interfaces = []
  for if_name, if_status in psutil.net_if_stats().items():
    interface = Interface(name=if_name, upstatus=if_status.isup, speed=if_status.speed)
    interfaces.append(interface)
  return interfaces

def getInfo():
  return CommonInfo(hostname = _getHostname(),
    uptime = _getUptime(), 
    cpu_core = psutil.cpu_count(True),
    cpu_load = psutil.cpu_percent(interval=1),
    memory = getMemory(),
    partitions=getPartList(),
    iflist = getInterfaceList())

def updateInfo(hostconf):
  hostconf.uptime = _getUptime()
  hostconf.cpu_load = psutil.cpu_percent()
  hostconf.memory = getMemory()
  hostconf.partitions = getPartList()
  return hostconf

def getPhisicalDisk():
  result = {}
  for disk, disk_count in psutil.disk_io_counters(perdisk=True).items():
    result[disk] = PhisicalDiskCount(**disk_count._asdict())
  return result