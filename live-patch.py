from utils.fs import *
from utils.git import *

def install_nvchad():
  remove_directory("~/.config/nvim.backup")
  move("~/.config/nvim", "~/.config/nvim.backup")
  remove_directory("~/.local/share/nvim")
  clone("NvChad/NvChad", "~/.config/nvim", shallow=True)


def main():
  install_nvchad()


if __name__ == "__main__":
  main()
