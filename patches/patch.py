class Patch:
  def __init__(self, file, name, patch_method):
    self.file = file
    self.name = name
    self.patch_method = patch_method

  def run(self):
    self.patch_method()