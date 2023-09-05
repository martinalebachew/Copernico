from utils.git import *

def check_for_updates():
  local = get_local_last_commit_hash()
  remote = get_remote_last_commit_hash()

  if (local != remote):
    print_error(f"Updates are available! Please pull the latest changes and try again ({local}, {remote})")
    exit()
