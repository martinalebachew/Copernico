from utils.updates import *
from utils.fs import *
from utils.logging import *
from utils.nvim import *
from shared.prerequisites import *
from livepatch import livepatch

def check_prerequisites():
  for (exec, name) in prerequistes:
    if exec_path(exec) is None:
      print_error(f"Unfulfilled prerequisite: {name}")
      exit()


def install_copernico():
  check_for_updates()
  check_prerequisites()
  check_nvim_version()
  livepatch()
  
  clear_terminal()
  print_success("Copernico was installed successfully!")


if __name__ == "__main__":
  install_copernico()
