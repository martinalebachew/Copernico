from utils.logging import *

class Version:
  def __init__(self, major, minor, patch):
    self.major = major
    self.minor = minor
    self.patch = patch


def parse_version(version_string):
  try:
    version = version_string.split(".")
    major = int(version_string[0])
    minor = int(version_string[1])
    patch = int(version_string[2])

  except:
    print_error("Failed to parse version")
    exit()
