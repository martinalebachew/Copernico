from utils.git import *

def check_for_updates():
  local = get_local_last_commit_hash()
  remote = get_remote_last_commit_hash()

  if (local != remote):
    short_local = local[:SHORT_COMMIT_HASH_LENGTH]
    short_remote = remote[:SHORT_COMMIT_HASH_LENGTH]
    
    print_error(f"Updates are available! Please pull the latest changes and try again")
    print_error(f"{short_local} < {short_remote}")
    exit()
