import shutil
from os.path import expanduser
from utils.logging import *

def remove_directory(path, ignore_file_not_found=True):
  try:
    shutil.rmtree(path)

  except Exception as error:
    if not (isinstance(error, FileNotFoundError) and ignore_file_not_found):
      print_error(f"Failed to remove {path}")
      exit()
    
  print_success(f"Successfully removed {path}")


def move(source, destination, ignore_file_not_found=True):
  try:
    shutil.move(source, destination)

  except Exception as error:
    if not (isinstance(error, FileNotFoundError) and ignore_file_not_found):
      print_error(f"Failed to move {source} -> {destination}")
      exit()
    
  print_success(f"Successfully moved {source} -> {destination}")
  

def resolve_path(path):
  return path.replace("~", expanduser("~"))
