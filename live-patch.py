from utils.fs import *
from utils.git import *

nvim_dir = resolve_path("~/.config/nvim")
nvim_dir_backup = resolve_path("~/.config/nvim.backup")
nvim_data_dir = resolve_path("~/.local/share/nvim")

def install_nvchad():
  remove_directory(nvim_dir_backup)
  move(nvim_dir, nvim_dir_backup)
  remove_directory(nvim_data_dir)
  clone("NvChad/NvChad", nvim_dir, shallow=True)


def patch_nvchad():
  for patch in patches.methods:
    patch()


def main():
  install_nvchad()
  patch_nvchad()


if __name__ == "__main__":
  main()
