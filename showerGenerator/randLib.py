import numpy as np

try:
  from showerBase import showerBase
except ImportError:
  from .showerBase import showerBase

try:
  from showerBase import primaryType
except ImportError:
  from .showerBase import primaryType

class randLib:
  def __init__(self):
    self._energyMin = 3.166e17
    self._energyMax = 3.166e19
    self._thetaMin = 0.0
    self._thetaMax = 65.0
    self._spectralIndex = -1.0
  #-----------------------------------------------------
  # functions
  #-----------------------------------------------------

  def generateEnergy(self, u):
    if self._spectralIndex == -1.0:
      return self._energyMin*np.power( self._energyMax/self._energyMin, u)

    a = np.power(self._energyMin, self._spectralIndex+1.0)
    b = np.power(self._energyMax, self._spectralIndex+1.0)
    return np.power(u*(b-a)+a, 1/(self._spectralIndex+1.0))

  def generateTheta(self, u):
    radTM = self._thetaMax*np.pi/180.0
    return (180.0/np.pi)*np.arcsin( np.sin(radTM)*np.sqrt(u) )

  def generateShower(self, a, b, pr):
    shower = showerBase()
    shower.energy = self.generateEnergy(a)
    shower.theta = self.generateTheta(b)
    shower.primary = pr
    return shower
  
  #-----------------------------------------------------
  # getters and setters
  #-----------------------------------------------------

  @property
  def energyMin(self):
    return self._energyMin

  @energyMin.setter
  def energyMin(self, eMin):
    if eMin < 100 or eMin > 1e12:
      raise ValueError("Energy must be expressed in GeV")
    self._energyMin = eMin

  @property
  def energyMax(self):
    return self._energyMax

  @energyMax.setter
  def energyMax(self, eMax):
    if eMin < 100 or eMin > 1e12:
      raise ValueError("Energy must be expressed in GeV")
    self._energyMax = eMax

  @property
  def thetaMin(self):
    return self._thetaMin

  @thetaMin.setter
  def thetaMin(self, thMin):
    self._thetaMin = thMin

  @property
  def thetaMax(self):
    return self._thetaMax

  @thetaMax.setter
  def thetaMax(self, thMax):
    self._thetaMax = thMax

  @property
  def spectralIndex(self):
    return self._spectralIndex

  @spectralIndex.setter
  def spectralIndex(self, n):
    self._spectralIndex = n
