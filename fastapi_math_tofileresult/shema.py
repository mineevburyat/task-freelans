from pydantic import BaseModel
# from xmlrpc.client import Boolean, boolean
import datetime

class PiLeibnicmethod(BaseModel):
	result: float
	percent: int

