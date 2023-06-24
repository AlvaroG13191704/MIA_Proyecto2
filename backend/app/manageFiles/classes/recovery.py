import os
import shutil
from ..setCredentials import setCredentials
import json
from ... import config
import requests
# if the path does not exist, return error
# if the name comes but the name file does not exist, return error
# if the name does not come, delete the folder

def set_config():
   return config.Settings()

class Recovery():
  def __init__(self, type_to, type_from, ip, port, name) -> None:
    self.type_to = type_to
    self.type_from = type_from
    self.ip = ip
    self.port = port
    self.name = name
    self.s3 = setCredentials()
    self.settings = set_config()
    