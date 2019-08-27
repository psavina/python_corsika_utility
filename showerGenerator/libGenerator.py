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

try:
  from detector import detector
except ImportError:
  from .detector import detector
  
from corsikaDatacard import datacardBase as dcB

class libGenerator:
  def __init__(self):

    self._energyMin = 17.5
    self._energyMax = 19.5
    self._energyBins = 4
    self._thetaMin = 0.0
    self._thetaMax = 65.0
    self._thetaBins = 1
    self._showerPerPrimary = 200000
    self._primaries = [ 'proton', 'photon' ]

    self._spectralIndex = {
      'proton': -1.0,
      'photon': -1.0
    }
    self._months = [1, 4, 7, 10]
    self._mainDir = "."
    
    self._showers = []
    self._datacards = []
    self._showerPerBin = []

    self._detector = detector()
    self._randLib = randLib()

    self._r = np.random
    self._primes = []

    self._PhysicalDistributions = True
    
    primesFile = open("primes.dat","r")
    for line in primesFile:
      linePrimes = line.split("\t")
      for number in linePrimes:
        self._primes.append( int(number) )

    primesFile.close()
    #nPrimes = len(self._primes)
    #i = showerID%nPrimes
    #j = showerID//nPrimes
    self._seed = -1
    #self._seed = self.primes[i]*self.primes[j]

  #------------------------------------------------------------
  # utils
  #------------------------------------------------------------
  def _getShower(self, rndEne, rndPhi, pr):
    if self._PhysicalDistributions:
      return self._randLib.generateShower( rndEne, rndPhi, pr)
    else:
      minEne = self._randLib.energyMin()
      maxEne = self._randLib.energyMax()
      minTh = self._randLib.thetaMin()
      maxTh = self._randLib.thetaMax()
      shower = showerBase()
      shower.energy = (maxEne-minEne)*rndEne+minEne
      shower.theta = (maxTh-minTh)*rndTh+minTh
  def _setBinEnergy(self):
    return a
  
  def genDatacard(self, showerID):
    return showerID
    
    
  #------------------------------------------------------------
  # getter and setter
  #------------------------------------------------------------
  @property
  def energyMin(self):
    return self._energyMin

  @energyMin.setter
  def energyMin(self, a):
    self._energyMin = a

  @property
  def energyMax(self):
    return self._energyMax

  @energyMax.setter
  def energyMax(self, a):
    self._energyMax = a

  @property
  def energyBins(self):
    return self._energyBins

  @energyBins.setter
  def energyBins(self, a):
    if a < 1 :
      raise ValueError("ERROR: number of energy bins must be at least 1")
    self._energyBins = a

  @property
  def thetaMin(self):
    return self._thetaMin

  @thetaMin.setter
  def thetaMin(self, a):
    self._thetaMin = a

  @property
  def thetaBins(self):
    return self._thetaBins

  @thetaBins.setter
  def thetaBins(self, a):
    if a < 1 :
      raise ValueError("ERROR: number of theta bins must be at least 1")
    self._thetaBins = a
  
  @property
  def showerPerPrimary(self):
    return self._showerPerPrimary

  @showerPerPrimary.setter
  def showerPerPrimary(self, a):
    if (a/(self._energyBins*self._thetaBins)) < 1.0:
      raise ValueError("ERROR: number of shower per each bin must be at least 1")
    self._showerPerPrimary = a


  @property
  def spectralIndex(self):
    return self._spectralIndex

  @spectralIndex.setter
  def spectralIndex(self, pr, a):
    self._spectralIndex[pr] = a

  @property
  def months(self):
    return self._months

                    
  @months.setter
  def months(self, a):
    self._months = a
                    
  @property
  def physicalDistributions(self):
    return self._PhysicalDistributions

  @physicalDistributions.setter
  def physicalDistributions(self, a):
    self._PhysicalDistributions = a
