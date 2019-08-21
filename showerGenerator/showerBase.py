#=====================================================================================================
# CR Shower base structure
#-----------------------------------------------------------------------------------------------------
# author: psavina
# date: 21/08/2019
#=====================================================================================================

primaryType = {
  "photon": 1,
  "proton": 14,
  "iron": 999
}

class showerBase:
  def __init__(self):
    self._energy = 0.0
    self._theta = 0.0
    self._core = [0.0, 0.0]
    self._primaryType = primaryType['proton']

  @property
  def energy(self):
    return self._energy

  @energy.setter
  def energy(self, ene):
    self._energy = ene

  @property
  def theta(self):
    return self._theta

  @theta.setter
  def theta(self, th):
    self._theta = th

  @property
  def primary(self):
    return self._primaryType

  @primary.setter
  def primary(self, pr):
    self._primaryType = primaryType[pr]

  @property
  def core(self):
    return self._core

  @core.setter
  def core(self, c):
    if not type(c) is list:
      raise ValueError("Error: wrong data type for the core")
    if not len(c) == 2:
      raise ValueError("Error: wrong number of elements for the core")
    self._core = c

  
