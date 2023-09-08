from utils.fs import resolve_path

conf_file = resolve_path("~/.tmux.conf")
conf_backup = resolve_path("~/.tmux.conf.backup")
conf_source = "assets/.tmux.conf"