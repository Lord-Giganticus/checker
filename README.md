# checker
A pyhon module to check that a pip installable module is installed and also checks the name of the script to check if it's a .exe and if it's not a .exe, updates git submodules.
* Usage:
```
# Python code btw
from checker import module, extension # put this at the top of your script with other imports.

# Use of module class:
module.checker('colorama') # this MUST be a string and a proper pypi package.

# Use of extension class:
extension.checker() # this will check the extension of the script, if it's a .py file, it'll check for the modules folder and ask to update the submodules(if checker.py is in modules, it'll skip itself.). If it's a .exe file, it'll say there is no need to update because all py code from submodules is compiled into the .exe.

* To use in .gitmodules:
Refer to [this repo.](https://github.com/Lord-Giganticus/Python-Modules)