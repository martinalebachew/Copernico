from git import Repo
from utils.logging import *

def clone(github_specifier, path, branch="main", shallow=False):
  url = f"https://github.com/{github_specifier}"

  try:
    if shallow:
      Repo.clone_from(url, path, branch=branch, depth=1)
    else:
      Repo.clone_from(url, path, branch=branch)

  except:
    print_error(f"Failed to clone {url} -> {path}")
    exit()

  print_success(f"Successfully cloned {url} -> {path}")
