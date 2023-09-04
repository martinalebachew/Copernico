from utils.logging import *

def format_newlines(text):
  return "\n".join(text.splitlines())


def replace_lines(path, old_block, new_block):
  with open(path, "r") as file:
    contents = format_newlines(file.read())

  # Ignore first and last padding newlines
  old_block = format_newlines(old_block[1:-1])
  new_block = format_newlines(new_block[1:-1])
  
  if old_block not in contents:
    raise LookupError(f"Find and replace operation failed on file {path}")
  
  with open(path, "w") as file:
    file.write(contents.replace(old_block, new_block))
