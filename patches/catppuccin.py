from os.path import join
from utils.patching import replace_lines
import shared.nvim as nvim

NAME = "Set Theme To Catppuccin"


old_bootstrap_block = r"""
      file:write "---@type ChadrcConfig\nlocal M = {}\n\nM.ui = { theme = 'onedark' }\n\nreturn M"
"""

new_bootstrap_block = r"""
      file:write "---@type ChadrcConfig\nlocal M = {}\n\nM.ui = { theme = 'catppuccin' }\n\nreturn M"
"""


old_defaults_block = r"""
  theme_toggle = { "onedark", "one_light" },
  theme = "onedark", -- default theme
"""

new_defaults_block = r"""
  theme_toggle = { "catppuccin", "one_light" },
  theme = "catppuccin", -- default theme
"""


def patch():
  bootstrap_file = join(nvim.default_dir, "lua/core/bootstrap.lua")
  replace_lines(bootstrap_file, old_bootstrap_block, new_bootstrap_block)

  defaults_file = join(nvim.default_dir, "lua/core/default_config.lua")
  replace_lines(defaults_file, old_defaults_block, new_defaults_block)
