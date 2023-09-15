from os.path import join
from utils.patching import replace_lines
import shared.nvim as nvim

NAME = "Disable NvChadUpdate Command"


old_updates_block = r"""
new_cmd("NvChadUpdate", function()
  require "nvchad.updater"()
end, {})
"""


def patch():
  init_file = join(nvim.default_dir, "lua/core/init.lua")
  replace_lines(init_file, old_updates_block, "")
