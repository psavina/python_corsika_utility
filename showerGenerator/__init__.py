
try:
  from showerBase import showerBase
except ImportError:
  from .showerBase import showerBase

try:
  from showerBase import primaryType
except ImportError:
  from .showerBase import primaryType
  
try:
  from randLib import randLib
except ImportError:
  from .randLib import randLib

try:
  from libGenerator import libGenerator
except ImportError:
  from .libGenerator import libGenerator
