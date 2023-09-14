from utils.shell import *
from utils.logging import *
from utils.version import *
from shared.nvim import mininum_version

def get_nvim_version():
  _, output = run_shell("nvim --version")
  version_string = output.splitlines()[0].split("NVIM v")[1]
  version = parse_version(version_string)
  return version


def check_nvim_version():
  current_version = get_nvim_version()
  if not is_version_sufficient(current_version, mininum_version):
    print_error(f"Minimum required version of Neovim is {mininum_version}")
    exit()
