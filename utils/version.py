from utils.logging import *

class Version:
  def __init__(self, version_string):
    try:
      version = version_string.split(".")
      self.major = int(version[0])
      self.minor = int(version[1])
      self.patch = int(version[2])
      
    except:
      print_error("Failed to parse version")
      exit()


def is_version_sufficient(current, minimum):
  if current.major < minimum.major:
    return False
  
  if current.minor < minimum.minor:
    return False
  
  if current.patch < minimum.patch:
    return False
  
  return True
