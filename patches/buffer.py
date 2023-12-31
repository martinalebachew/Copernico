from os.path import join
from utils.patching import replace_lines
from utils.git import clone
import shared.nvim as nvim

NAME = "Update Post Install Buffer"


old_ui_plugin = r"""
  {
    "NvChad/ui",
    branch = "v2.0",
    lazy = false,
  },
"""

new_ui_plugin_template = r"""
  {
    dir = "ui_dir",
    branch = "v2.0",
    lazy = false,
  },
"""


old_post_install_buffer = r"""
  local text_on_screen = {
    "",
    "",
    "███╗   ██╗   ██████╗  ████████╗ ███████╗ ███████╗",
    "████╗  ██║  ██╔═══██╗ ╚══██╔══╝ ██╔════╝ ██╔════╝",
    "██╔██╗ ██║  ██║   ██║    ██║    █████╗   ███████╗",
    "██║╚██╗██║  ██║   ██║    ██║    ██╔══╝   ╚════██║",
    "██║ ╚████║  ╚██████╔╝    ██║    ███████╗ ███████║",
    "",
    "",
    "  Please read the docs at nvchad.com from start to end 󰕹 󰱬",
    "",
    "  All NvChad available options are in 'core/default_config.lua', know them",
    "",
    "  Mason just downloads binaries, dont expect it to configure lsp automatically",
    "",
    "  Dont edit files outside custom folder or you won't be able to update NvChad",
    "",
    "  Ask NvChad issues in NvChad communities only, go to https://nvchad.com/#community",
    "",
    "  Read the plugin docs to utilize 100% of their functionality.",
    "",
    "  If you dont see any syntax highlighting, you need to install a tsparser for it",
    "",
    "  Can you see this icon  ? If not, you need to read the pre-requisites again https://nvchad.com/docs/quickstart/install",
    "",
    "  Check the default mappings by pressing space + ch or NvCheatsheet command",
    "",
    "  Need help to install a plugin? Check out our nvcommunity plugins in https://github.com/NvChad/nvcommunity",
    "",
    "Now quit nvim!",
  }
"""

new_post_install_buffer = r"""
  local text_on_screen = {
    "",
    "    ______                            _          ",
    "   / ____/___  ____  ___  _________  (_)________ ",
    "  / /   / __ \\/ __ \\/ _ \\/ ___/ __ \\/ / ___/ __ \\",
    " / /___/ /_/ / /_/ /  __/ /  / / / / / /__/ /_/ /",
    " \\____/\\____/ .___/\\___/_/  /_/ /_/_/\\___/\\____/ ",
    "           /_/                                   ",
    "",
    "󱁖  Copernico has been installed successfully!",
    "",
    "󰚩  Use \":Copilot setup\" to activate GitHub Copilot.",
    "",
    "󱔗  Read the plugin docs to utilize 100% of their functionality.",
    "",
    "󰌌  Check the default mappings by pressing space + ch.",
    "",
    "Now quit nvim!",
    "",
    "",
    "Copernico is an open-source terminal configuration by Martin Alebachew,",
    "Based on NvChad by Siduck and Tmux by Nicholas Marriott.",
    "Copyright 󰗦 2023, Martin Alebachew.",
  }
"""


def patch():
  ui_dir = join(nvim.default_dir, "ui_plugin")
  clone("NvChad/ui", ui_dir)

  plugins_file = join(nvim.default_dir, "lua/plugins/init.lua")
  new_ui_plugin = new_ui_plugin_template.replace("ui_dir", ui_dir)
  replace_lines(plugins_file, old_ui_plugin, new_ui_plugin)

  post_install_file = join(ui_dir, "lua/nvchad/post_install.lua")
  replace_lines(post_install_file, old_post_install_buffer, new_post_install_buffer)
