from wifi import Cell, Scheme

class Connection(object):
    _cell = Cell.all('wlan0')
    def __init__(self,ssid="",pwd=""):
        self._ssid=""
        self._pwd=""

    @property
    def SSID(self):
        return self._ssid
    @SSID.setter
    def SSID(self,ssid):
        self._ssid = ssid
    @property
    def PASSWORD(self):
        return self._pwd
    @PASSWORD.setter
    def PASSWORD(self,pwd):
        self._pwd = pwd
    
    def getAllAP(self):
        AP_list=[]
        for ap in self._cell:
            AP_list.append(ap.ssid)
        return AP_list
    
    def findAP(self):
        for index,cel in enumerate(self._cell):
            if cel.ssid == self._ssid:
                return index
            
    def connectToAP(self,name='home'):
        try:
            exists_scheme = Scheme.find('wlan0','home')
            if exists_scheme is None:
                scheme = Scheme.for_cell('wlan0',name,self._cell[self.findAP()],self._pwd)
                scheme.activate()
                scheme.save()
            else:
                exists_scheme.activate()
        except Exception as e:
            print(str(e))
