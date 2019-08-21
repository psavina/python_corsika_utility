#from . import datacardBase
try:
  from datacardBase import datacardBase
except ImportError:
  from .datacardBase import datacardBase
