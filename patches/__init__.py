from glob import glob
from patches.patch import Patch
from importlib import import_module
from os.path import dirname, basename, isfile, join

patches = []
patch_files = glob(join(dirname(__file__), "*.py"))

for file in patch_files:
  if isfile(file) and basename(file) not in ["__init__.py", "patch.py"]:
    module_name = "patches." + basename(file)[:-3]
    module_obj = import_module(module_name)
    patches.append(Patch(basename(file), module_obj.NAME, module_obj.patch))
