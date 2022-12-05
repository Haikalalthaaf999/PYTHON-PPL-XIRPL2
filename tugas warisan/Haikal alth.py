class Agama:
    def __init__(self, nama, agama):
        self.nama = nama
        self.agama = agama

    def perkenalan(self):
        print("Nama saya", self.nama, "Beragama", self.agama)
    

class manusia(Agama):
    def __init__(self, nama, agama, sholat):
        Agama.__init__(self, nama, agama)
        self.sholat = sholat
    pass

class Pelajar(Agama):
    def __init__(self, nama, agama, sembahyang):
        Agama.__init__(self, nama, agama)
        self.sembahyang = sembahyang
    pass
          

Dava = manusia('Dava','Islam','sholat')
Dava.perkenalan()
print(Dava.nama, "beribadah dengan melakukan", Dava.sholat,"\n")

Bong_chin = Pelajar('Bong chin','budha','sembahyang')
Bong_chin.perkenalan()
print(Bong_chin.nama, "beribadah dengan melakukan", Bong_chin.sembahyang,"\n")