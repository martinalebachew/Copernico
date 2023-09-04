import shutil
from utils.logging import *

def remove_directory(path, ignore_file_not_found=True):
  try:
    shutil.rmtree(path)

  except Exception as error:
    if not (isinstance(error, FileNotFoundError) and ignore_file_not_found):
      print_error(f"Failed to remove {path}")
      exit()
    
  print_success(f"Successfully removed {path}")
