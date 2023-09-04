from git import Repo

def clone(github_specifier, to_path, branch="main", shallow=False):
  url = f"https://github.com/{github_specifier}"

  if shallow:
    Repo.clone_from(url, to_path, branch=branch, depth=1)
  else:
    Repo.clone_from(url, to_path, branch=branch)
