from subprocess import Popen, PIPE, STDOUT
from utils.logging import *
from utils.fs import resolve_path

def clone(github_specifier, path, branch="main", shallow=False):
  path = resolve_path(path)
  url = f"https://github.com/{github_specifier}"

  git_command = f"git clone --progress -b {branch} {url} {path}"
  git_command += " --depth 1" if shallow else ""
  git = Popen(git_command, shell=True, stdout=PIPE, stderr=STDOUT, text=True)
  
  if git.stdout.read().endswith("done.\n"):
    print_success(f"Successfully cloned {url} -> {path}")
  else:
    print_error(f"Failed to clone {url} -> {path}")
    exit()
