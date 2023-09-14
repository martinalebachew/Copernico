from os.path import join
from utils.patching import replace_lines
import shared.nvim as nvim

NAME = "No Example Configuration Prompt"


old_prompt_block = r"""
  if fn.isdirectory(path) ~= 1 then
    local input = fn.input "Do you want to install example custom config? (y/N): "

    if input:lower() == "y" then
      M.echo "Cloning example custom config repo..."
      shell_call { "git", "clone", "--depth", "1", "https://github.com/NvChad/example_config", path }
      fn.delete(path .. "/.git", "rf")
    else
"""

new_prompt_block = r"""
  if fn.isdirectory(path) ~= 1 then
"""


old_end_sequence = r"""
        file:close()
      end
    end
  end
end
"""

new_end_sequence = r"""
      file:close()
    end
  end
end
"""


def patch():
  bootstrap_file = join(nvim.default_dir, "lua/core/bootstrap.lua")
  replace_lines(bootstrap_file, old_prompt_block, new_prompt_block)
  replace_lines(bootstrap_file, old_end_sequence, new_end_sequence)
