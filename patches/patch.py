class Patch:
  def __init__(self, file, name, patch_method):
    self.file = file
    self.name = name
    self.patch_method = patch_method

  def run(self, nvim_dir):
    self.patch_method(nvim_dir)