from subprocess import Popen, PIPE, STDOUT
from utils.logging import *

def clone(github_specifier, path, branch=None, shallow=False):
  url = f"https://github.com/{github_specifier}"

  git_command = f"git clone {url} {path}"
  git_command += " --progress"
  git_command += f" --branch {branch}" if branch else ""
  git_command += " --depth 1" if shallow else ""
  git = Popen(git_command, shell=True, stdout=PIPE, stderr=STDOUT, text=True)
  
  if git.stdout.read().endswith("done.\n"):
    print_success(f"Cloned {url} -> {path}")
  else:
    print_error(f"Failed to clone {url} -> {path}")
    exit()

  
def __get_commit_hash_impl(git_command):
  git = Popen(git_command, shell=True, stdout=PIPE, stderr=STDOUT, text=True)
  output = git.stdout.read().strip()

  if len(output) == 7:
    return output
  else:
    print_error(f"Failed to get local last commit hash!")
    exit()


def get_local_last_commit_hash():
  git_command = "git log -n1 --format=\"%h\""
  return __get_commit_hash_impl(git_command)


def get_remote_last_commit_hash():
  git_command = "git rev-parse --short HEAD"
  return __get_commit_hash_impl(git_command)
