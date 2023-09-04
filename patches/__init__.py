from glob import glob
from importlib import import_module
from os.path import dirname, basename, isfile, join

methods = []
patch_files = glob(join(dirname(__file__), "*.py"))

for file in patch_files:
  if not file.endswith("__init__.py") and isfile(file):
    module_name = "patches." + basename(file)[:-3]
    module_obj = import_module(module_name)
    methods.append(module_obj.patch)
