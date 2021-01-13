# from pkg.pkg import module
from myproject.utils import mymod

mymod.spam()
mymod.ham()

# PYTHONPATH (WINDOWS)
# C:\some\path;d:\some\other\path;\\netshare\pythonjunk\wombats

# PYTHONPATH (LINUX/MAC)
# /some/path:/some/other/path:/pythonjunk/wombats

mymod.doit("walrus.txt", "wombat")
