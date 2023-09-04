from utils.fs import *
from utils.git import *
from patches import patches

NVIM_DIR = resolve_path("~/.config/nvim")
NVIM_BACKUP_DIR = resolve_path("~/.config/nvim.backup")
NVIM_DATA_DIR = resolve_path("~/.local/share/nvim")


def install_nvchad():
  remove_directory(NVIM_BACKUP_DIR)
  move(NVIM_DIR, NVIM_BACKUP_DIR)
  remove_directory(NVIM_DATA_DIR)
  clone("NvChad/NvChad", NVIM_DIR, shallow=True)


def patch_nvchad():
  for patch in patches:
    try:
      patch.run(NVIM_DIR)
      print_success(f"Applied patch: {patch.name} ({patch.file})")
    except:
      print_error(f"Failed to apply patch: {patch.name} ({patch.file})")
      exit()


def install_tpm():
  remove_directory("~/.tmux/plugins/tpm")
  clone("tmux-plugins/tpm", "~/.tmux/plugins/tpm")


def main():
  install_tpm()
  install_nvchad()
  patch_nvchad()


if __name__ == "__main__":
  main()
