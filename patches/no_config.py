from os.path import join
from utils.patching import replace_lines

NAME = "No Example Configuration Prompt"


old_block = r"""
  if fn.isdirectory(path) ~= 1 then
    local input = fn.input "Do you want to install example custom config? (y/N): "

    if input:lower() == "y" then
      M.echo "Cloning example custom config repo..."
      shell_call { "git", "clone", "--depth", "1", "https://github.com/NvChad/example_config", path }
      fn.delete(path .. "/.git", "rf")
    else
      -- use very minimal chadrc
      fn.mkdir(path, "p")

      local file = io.open(path .. "/chadrc.lua", "w")
      if file then
        file:write "---@type ChadrcConfig\nlocal M = {}\n\nM.ui = { theme = 'onedark' }\n\nreturn M"
        file:close()
      end
    end
  end
"""


new_block = r"""
  if fn.isdirectory(path) ~= 1 then
    -- use very minimal chadrc
    fn.mkdir(path, "p")

    local file = io.open(path .. "/chadrc.lua", "w")
    if file then
      file:write "---@type ChadrcConfig\nlocal M = {}\n\nM.ui = { theme = 'onedark' }\n\nreturn M"
      file:close()
    end
  end
"""


def patch(nvim_dir):
  bootstrap_file = join(nvim_dir, "lua/core/bootstrap.lua")
  replace_lines(bootstrap_file, old_block, new_block)
