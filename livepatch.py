from utils.fs import *
from utils.git import *
from utils.shell import *
import shared.tpm as tpm
import shared.tmux as tmux
import shared.nvim as nvim
from patches import patches

def install_nvchad():
  remove_directory(nvim.backup_dir)
  move(nvim.default_dir, nvim.backup_dir)
  remove_directory(nvim.data_dir)
  clone(nvim.nvchad_repo, nvim.default_dir, shallow=True)


def patch_nvchad():
  for patch in patches:
    try:
      patch.run()
      print_success(f"Applied patch: {patch.name} ({patch.file})")
    except:
      print_error(f"Failed to apply patch: {patch.name} ({patch.file})")
      exit()


def install_tpm():
  remove_directory(tpm.plugins_dir)
  clone(tpm.repo, tpm.default_dir)


def install_tmux_plugins():
  output = run_script(tpm.plugins_script)
  if "fail" in output:
    print_error("Failed to install Tmux plugins")
    exit()


def configure_tmux():
  remove_file(tmux.conf_backup)
  move(tmux.conf_file, tmux.conf_backup)
  copy_file(tmux.conf_source, tmux.conf_file, ignore_file_not_found=False)
  install_tmux_plugins()


def livepatch():
  install_tpm()
  configure_tmux()
  install_nvchad()
  patch_nvchad()


if __name__ == "__main__":
  livepatch()
