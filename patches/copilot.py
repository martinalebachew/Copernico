from os.path import join
from utils.patching import replace_lines
import shared.nvim as nvim

NAME = "GitHub Copilot Plugin"


old_plugins_closure = r"""
}

local config = require("core.utils").load_config()
"""

new_plugins_closure = r"""

  -- GitHub Copilot
  {
    "github/copilot.vim",
    lazy = false,
  },
}

local config = require("core.utils").load_config()
"""


def patch():
  plugins_file = join(nvim.default_dir, "lua/plugins/init.lua")
  replace_lines(plugins_file, old_plugins_closure, new_plugins_closure)
