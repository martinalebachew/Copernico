from os.path import join
from utils.patching import replace_lines

NAME = "Vim Tmux Navigator Plugin"


old_plugins_closure = r"""
}

local config = require("core.utils").load_config()
"""

new_plugins_closure = r"""

  -- Vim Tmux Navigator
  {
    "christoomey/vim-tmux-navigator",
    lazy = false,
  },
}

local config = require("core.utils").load_config()
"""


old_mappings_block = r"""
    ["<C-h>"] = { "<C-w>h", "Window left" },
    ["<C-l>"] = { "<C-w>l", "Window right" },
    ["<C-j>"] = { "<C-w>j", "Window down" },
    ["<C-k>"] = { "<C-w>k", "Window up" },
"""

new_mappings_block = r"""
    ["<C-h>"] = { "<cmd> TmuxNavigateLeft<CR>", "Window left" },
    ["<C-l>"] = { "<cmd> TmuxNavigateRight<CR>", "Window right" },
    ["<C-j>"] = { "<cmd> TmuxNavigateDown<CR>", "Window down" },
    ["<C-k>"] = { "<cmd> TmuxNavigateUp<CR>", "Window up" },
"""


def patch(nvim_dir):
  plugins_file = join(nvim_dir, "lua/plugins/init.lua")
  replace_lines(plugins_file, old_plugins_closure, new_plugins_closure)

  mappings_file = join(nvim_dir, "lua/core/mappings.lua")
  replace_lines(mappings_file, old_mappings_block, new_mappings_block)
