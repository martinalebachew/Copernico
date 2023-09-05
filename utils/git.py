from subprocess import Popen, PIPE, STDOUT
from utils.logging import *

COMMIT_HASH_LENGTH = 40
SHORT_COMMIT_HASH_LENGTH = 7


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


def fetch_remote():
  git_command = "git fetch"
  git = Popen(git_command, shell=True, stdout=PIPE, stderr=STDOUT)
  git.wait()

  if git.returncode != 0:
    print_error(f"Failed to fetch remote")
    exit()

  
def __get_commit_hash_impl(git_command):
  git = Popen(git_command, shell=True, stdout=PIPE, stderr=STDOUT, text=True)
  output = git.stdout.read().strip()

  if len(output) == COMMIT_HASH_LENGTH:
    return output
  else:
    print_error(f"Failed to parse commit hash!")
    exit()


def get_local_last_commit_hash():
  git_command = "git rev-parse HEAD"
  return __get_commit_hash_impl(git_command)


def get_remote_last_commit_hash():
  fetch_remote()
  git_command = "git rev-parse origin"
  return __get_commit_hash_impl(git_command)
