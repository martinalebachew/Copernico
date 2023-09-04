from os.path import join
from utils.patching import replace_lines

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


def patch(nvim_dir):
  plugins_file = join(nvim_dir, "lua/plugins/init.lua")
  replace_lines(plugins_file, old_plugins_closure, new_plugins_closure)
