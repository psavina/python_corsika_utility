#===========================================================================================
# Datacard Base structure
#-------------------------------------------------------------------------------------------
# A class to handle the corsika Datacard base structure
#-------------------------------------------------------------------------------------------
# author: psavina
# date:   20/08/2019
#===========================================================================================

class datacardBase:
  def __init__(self):
    self._runnr   = ["RUNNR", 10000]
    self._nshow   = ["NSHOW", 1]
    self._evtnr   = ["EVTNR", 1]
    self._prmpar  = ["PRMPAR", 14]
    self._eslope  = ["ESLOPE", -1.0]
    self._erange  = ["ERANGE", [1.00E9,1.00E9]]
    self._seed1   = ["SEED", [100001, 0, 0]]
    self._seed2   = ["SEED", [100002, 0, 0]]
    self._seed3   = ["SEED", [100003, 0, 0]]
    self._thin    = ["THIN", [1.00E-06, 5.349461E+01, 5.000E+3]]
    self._thinh   = ["THINH", [1.00E00, 1.00E02]]
    self._thetap  = ["THETAP", [0.0, 65.0]]
    self._phip    = ["PHIP", [-180.0, 180]]
    self._epos    = ["EPOS", ["T", 0]]
    self._eposig  = ["EPOSIG", "T"]
    self._fixchi  = ["FIXCHI", 0.0]
    self._atmod   = ["ATMOD",18]
    self._obslev  = ["OBSLEV", 1.452E05]
    self._magnet  = ["MAGNET", [1.94E01, -1.41E+01]]
    self._ecuts   = ["ECUTS", [5.00E-02, 1.00E-02, 2.50E-04, 2.50E-04]]
    self._muaddi  = ["MUADDI", ["T"]]
    self._mumult  = ["MUMULT", ["T"]]
    self._hadflag = ["HADFLG", [0, 0, 0, 0, 0, 2]]
    self._elmflg  = ["ELMFLG", ["F", "T"]]
    self._stepfc  = ["STEPFC", 1.0]
    self._radnkg  = ["RADNKG", 5.0E05]
    self._longi   = ["LONGI", ["T", 1.0, "T", "T"]]
    self._ectmap  = ["ECTMAP", 2.5E05]
    self._maxprt  = ["MAXPRT", 1]
    self._datbas  = ["DATBAS", "T"]
    self._parout  = ["PAROUT", ["T", "T"]]
    self._direct  = ["DIRECT", "."]
    self._datdir  = ["DATDIR", "."]
    self._user    = ["USER", "psavina"]
    self._host    = ["HOST", "CNAF"]
    self._debug   = ["DEBUG", ["F", 6, "F", 100000]]


    self._attrList = [
      '_runnr',   
      '_nshow',   
      '_evtnr',   
      '_prmpar',  
      '_eslope',  
      '_erange',  
      '_seed1',   
      '_seed2',   
      '_seed3',   
      '_thin',    
      '_thinh',   
      '_thetap',  
      '_phip',    
      '_epos',    
      '_eposig',  
      '_fixchi',  
      '_atmod',   
      '_obslev',  
      '_magnet',  
      '_ecuts',   
      '_muaddi',  
      '_mumult',  
      '_hadflag', 
      '_elmflg',  
      '_stepfc',  
      '_radnkg',  
      '_longi',   
      '_ectmap',  
      '_maxprt',  
      '_datbas',  
      '_parout',  
      '_direct',  
      '_datdir',  
      '_user',    
      '_host',    
      '_debug',   
    ]
    
  #----------------------------------------------------------------------
  # Utils
  #----------------------------------------------------------------------

  # def getCard(self):
  #   outStr = ""
  #   for attr in self.__dict__.items():
  #     outStr += attr[1][0]+"\t"
  #     if type(attr[1][1]) is list:
  #       for value in attr[1][1]:
  #         outStr+=(str(value)+"\t")
  #       outStr+="\n"
  #     else:
  #       outStr+=(str(attr[1][1])+"\n")

  #   outStr+="EXIT"
  #   return outStr

  def getCard(self):
    outStr = ""
    for attribute in self._attrList:
      attr = self.__dict__[attribute]
      outStr += attr[0]+"\t"
      if type(attr[1]) is list:
        for value in attr[1]:
          outStr+=(str(value)+"\t")
        outStr+="\n"
      else:
        outStr+=(str(attr[1])+"\n")

    outStr+="EXIT"
    return outStr

  
  def printCard(self):
    print(self.getCard())

  #---------------------------------------------------------------------
  # getter and setter declarations
  #---------------------------------------------------------------------

  
  def genSetter(self, attr, a, b):
    if not type(a) == type(b):
      raise ValueError("ERROR: wrong type value for "+attr)
    if type(a) is list:
      if not len(a) == len(b):
        raise ValueError("ERROR: incorrect number of elements for "+attr)

    return b
    
  @property
  def runnr(self):
    return self._runnr[1]

  @runnr.setter
  def runnr(self, a):
    self._runnr[1] = self.genSetter(self._runnr[0], self._runnr[1], a)

  @property
  def nshow(self):
    return self._nshow[1]

  @nshow.setter
  def nshow(self, a):
    self._nshow[1] = self.genSetter(self._nshow[0], self._nshow[1], a)

  @property
  def evtnr(self):
    return self._evtnr[1]

  @evtnr.setter
  def evtnr(self, a):
    self._evtnr[1] = self.genSetter(self._evtnr[0], self._evtnr[1], a)

  @property
  def prmpar(self):
    return self._prmpar[1]

  @prmpar.setter
  def prmpar(self, a):
    self._prmpar[1] = self.genSetter(self._prmpar[0], self._prmpar[1], a)

  @property
  def eslope(self):
    return self._eslope[1]

  @eslope.setter
  def eslope(self, a):
    self._eslope[1] = self.genSetter(self._eslope[0], self._eslope[1], a)

  @property
  def erange(self):
    return self._erange[1]

  @erange.setter
  def erange(self, a):
    self._erange[1] = self.genSetter(self._erange[0], self._erange[1], a)

  @property
  def seed1(self):
    return self._seed1[1]

  @seed1.setter
  def seed1(self, a):
    self._seed1[1] = self.genSetter(self._seed1[0], self._seed1[1], a)

  @property
  def seed2(self):
    return self._seed2[1]

  @seed2.setter
  def seed2(self, a):
    self._seed2[1] = self.genSetter(self._seed2[0], self._seed2[1], a)

  @property
  def seed3(self):
    return self._seed3[1]

  @seed3.setter
  def seed3(self, a):
    self._seed3[1] = self.genSetter(self._seed3[0], self._seed3[1], a)

  @property
  def thin(self):
    return self._thin[1]

  @thin.setter
  def thin(self, a):
    self._thin[1] = self.genSetter(self._thin[0], self._thin[1], a)

  @property
  def thinh(self):
    return self._thinh[1]

  @thinh.setter
  def thinh(self, a):
    self._thinh[1] = self.genSetter(self._thinh[0], self._thinh[1], a)

  @property
  def phip(self):
    return self._phip[1]

  @phip.setter
  def phip(self, a):
    self._phip[1] = self.genSetter(self._phip[0], self._phip[1], a)

  @property
  def epos(self):
    return self._epos[1]

  @epos.setter
  def epos(self, a):
    self._epos[1] = self.genSetter(self._epos[0], self._epos[1], a)

  @property
  def eposig(self):
    return self._eposig[1]

  @eposig.setter
  def eposig(self, a):
    self._eposig[1] = self.genSetter(self._eposig[0], self._eposig[1], a)

  @property
  def fixchi(self):
    return self._fixchi[1]

  @fixchi.setter
  def fixchi(self, a):
    self._fixchi[1] = self.genSetter(self._fixchi[0], self._fixchi[1], a)

  @property
  def atmod(self):
    return self._atmod[1]

  @atmod.setter
  def atmod(self, a):
    self._atmod[1] = self.genSetter(self._atmod[0], self._atmod[1], a)

  @property
  def obslev(self):
    return self._obslev[1]

  @obslev.setter
  def obslev(self, a):
    self._obslev[1] = self.genSetter(self._obslev[0], self._obslev[1], a)

  @property
  def magnet(self):
    return self._magnet[1]

  @magnet.setter
  def magnet(self, a):
    self._magnet[1] = self.genSetter(self._magnet[0], self._magnet[1], a)

  @property
  def ecuts(self):
    return self._ecuts[1]

  @ecuts.setter
  def ecuts(self, a):
    self._ecuts[1] = self.genSetter(self._ecuts[0], self._ecuts[1], a)

  @property
  def muaddi(self):
    return self._muaddi[1]

  @muaddi.setter
  def muaddi(self, a):
    self._muaddi[1] = self.genSetter(self._muaddi[0], self._muaddi[1], a)

  @property
  def mumult(self):
    return self._mumult[1]

  @mumult.setter
  def mumult(self, a):
    self._mumult[1] = self.genSetter(self._mumult[0], self._mumult[1], a)

  @property
  def hadflg(self):
    return self._hadflg[1]

  @hadflg.setter
  def hadflg(self, a):
    self._hadflg[1] = self.genSetter(self._hadflg[0], self._hadflg[1], a)

  @property
  def elmflg(self):
    return self._elmflg[1]

  @elmflg.setter
  def elmflg(self, a):
    self._elmflg[1] = self.genSetter(self._elmflg[0], self._elmflg[1], a)

  @property
  def stepfc(self):
    return self._stepfc[1]

  @stepfc.setter
  def stepfc(self, a):
    self._stepfc[1] = self.genSetter(self._stepfc[0], self._stepfc[1], a)

  @property
  def radnkg(self):
    return self._radnkg[1]

  @radnkg.setter
  def radnkg(self, a):
    self._radnkg[1] = self.genSetter(self._radnkg[0], self._radnkg[1], a)

  @property
  def longi(self):
    return self._longi[1]

  @longi.setter
  def longi(self, a):
    self._longi[1] = self.genSetter(self._longi[0], self._longi[1], a)

  @property
  def ectmap(self):
    return self._ectmap[1]

  @ectmap.setter
  def ectmap(self, a):
    self._ectmap[1] = self.genSetter(self._ectmap[0], self._ectmap[1], a)

  @property
  def maxprt(self):
    return self._maxprt[1]

  @maxprt.setter
  def maxprt(self, a):
    self._maxprt[1] = self.genSetter(self._maxprt[0], self._maxprt[1], a)

  @property
  def datbas(self):
    return self._datbas[1]

  @datbas.setter
  def datbas(self, a):
    self._datbas[1] = self.genSetter(self._datbas[0], self._datbas[1], a)

  @property
  def parout(self):
    return self._parout[1]

  @parout.setter
  def parout(self, a):
    self._parout[1] = self.genSetter(self._parout[0], self._parout[1], a)

  @property
  def direct(self):
    return self._direct[1]

  @direct.setter
  def direct(self, a):
    self._direct[1] = self.genSetter(self._direct[0], self._direct[1], a)

  @property
  def datdir(self):
    return self._datdir[1]

  @datdir.setter
  def datdir(self, a):
    self._datdir[1] = self.genSetter(self._datdir[0], self._datdir[1], a)

  @property
  def user(self):
    return self._user[1]

  @user.setter
  def user(self, a):
    self._user[1] = self.genSetter(self._user[0], self._user[1], a)

  @property
  def host(self):
    return self._host[1]

  @host.setter
  def host(self, a):
    self._host[1] = self.genSetter(self._host[0], self._host[1], a)

  @property
  def debug(self):
    return self._debug[1]

  @debug.setter
  def debug(self, a):
    self._debug[1] = self.genSetter(self._debug[0], self._debug[1], a)


  
