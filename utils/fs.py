import shutil
from os.path import expanduser
from utils.logging import *

def remove_directory(path, ignore_file_not_found=True):
  path = resolve_path(path)

  try:
    shutil.rmtree(path)
    print_success(f"Successfully removed {path}")

  except Exception as error:
    if not (isinstance(error, FileNotFoundError) and ignore_file_not_found):
      print_error(f"Failed to remove {path}")
      exit()
    else:
      print_notice(f"Skipped removing {path}")


def move(source, destination, ignore_file_not_found=True):
  source = resolve_path(source)
  destination = resolve_path(destination)

  try:
    shutil.move(source, destination)
    print_success(f"Successfully moved {source} -> {destination}")

  except Exception as error:
    if not (isinstance(error, FileNotFoundError) and ignore_file_not_found):
      print_error(f"Failed to move {source} -> {destination}")
      exit()
    else:
      print_notice(f"Skipped moving {source} -> {destination}")


def resolve_path(path):
  return path.replace("~", expanduser("~"))
