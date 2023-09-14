from utils.shell import *
from utils.version import *

def get_nvim_version():
  _, output = run_shell("nvim --version")
  version_string = output.splitlines()[0].split("NVIM v")[0]
  version = parse_version(version_string)
  return version
