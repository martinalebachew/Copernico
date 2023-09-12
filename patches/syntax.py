from os.path import join
from utils.patching import replace_lines
import shared.nvim as nvim

NAME = "Enhanced Syntax Highlighting"


old_options_block = r"""
  ensure_installed = { "lua" },
"""

new_options_block = r"""
  ensure_installed = {
    "bash", "c", "c_sharp", "comment", "cpp", "css", "dart", "dockerfile",
    "gitignore", "html", "java", "javascript", "json", "latex", "lua", "make",
    "markdown", "markdown_inline", "ninja", "proto", "python", "regex", "rust",
    "sql", "swift", "tsx", "typescript", "vim", "yaml"
  },
  auto_install = true,
"""


def patch(nvim.default_dir):
  treesitter_file = join(nvim.default_dir, "lua/plugins/configs/treesitter.lua")
  replace_lines(treesitter_file, old_options_block, new_options_block)
