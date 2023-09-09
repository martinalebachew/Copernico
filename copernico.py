from utils.updates import *
from utils.fs import *
from shared.prerequisites import *
from livepatch import livepatch

def check_prerequisites():
  for (exec, name) in prerequistes:
    if exec_path(exec) is None:
      print_error(f"Unfulfilled prerequisite: {name}")
      exit(0)


def install_copernico():
  check_for_updates()
  check_prerequisites()
  livepatch()

if __name__ == "__main__":
  install_copernico()
