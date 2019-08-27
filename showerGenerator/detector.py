class detPos:
  def __init__(self):
    self._id = 0
    self._easting = 0
    self._northing = 0

  @property
  def ID(self):
    return self._id

  @ID.setter
  def ID(self, a):
    self._id = a

  @property
  def easting(self):
    return self._easting

  @easting.setter
  def easting(self, a):
    self._easting = a

  @property
  def northing(self):
    return self._northing
  
  @northing.setter
  def northing(self, a):
    self._northing = a

class detector:
  def __init__(self):
    self._stations = []
    self._eyes = []
    
    f = open("stations.dat","r")
    for line in f:
      if '#' in line:
        continue
      s = line.split(' ')
      st = detPos()
      st.ID = s[0]
      st.northing = s[1]
      st.easting = s[2]
      self._stations.append(st)
    f.close()

    f = open("eyes.dat","r")
    for line in f:
      if '#' in line:
        continue
      s = line.split(' ')
      st = detPos()
      st.ID = s[0]
      st.northing = s[1]
      st.easting = s[2]
      self._eyes.append(st)
    f.close()

    self._center = detPos()
    self._center.ID = 5
    self._center.northing = 6104895.7
    self._center.ID = 470544.3

  @property
  def center(self):
    return self._center

  @property
  def stations(self):
    return self._stations

  @property
  def eyes(self):
    return self._eyes
