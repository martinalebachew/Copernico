from utils.fs import resolve_path

plugins_dir = resolve_path("~/.tmux/plugins")
default_dir = resolve_path("~/.tmux/plugins/tpm")
plugins_script = resolve_path("~/.tmux/plugins/tpm/scripts/install_plugins.sh")
repo = "tmux-plugins/tpm"