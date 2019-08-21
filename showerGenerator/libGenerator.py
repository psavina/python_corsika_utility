import numpy as np

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

from corsikaDatacard import datacardBase as dcB

class libGenerator:
  def __init__(self, showerID):

    self._energyMin = 17.5
    self._energyMax = 19.5
    self._energyBins = 4
    self._thetaMin = 0.0
    self._thetaMax = 65.0
    self._thetaBins = 1
    self._primaries = [ 'proton', 'photon' ]

    self._mainDir = "."
    
    self._showers = []
    self._datacards = []

    # self._detector
    self._randLib = randLib()

    self._r = np.random
    self._primes = []

    primesFile = open("primes.dat","r")
    for line in primesFile:
      linePrimes = line.split("\t")
      for number in linePrimes:
        self._primes.append( int(number) )

    primesFile.close()
    nPrimes = len(self._primes)
    i = showerID%nPrimes
    j = showerID//nPrimes
    self._seed = self.primes[i]*self.primes[j]


    
