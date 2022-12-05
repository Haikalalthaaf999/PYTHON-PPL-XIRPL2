#belajar pewarisan (intertance)
#objek = Orang, Pelajar, Pekerja
#masing masing mempunyai nama,asal,kemampuan untuk introduce ur self
#pelajar di sekolah, pekerja di kantor

class Orang:
    def __init__(self, nama, asal):
        self.nama= nama
        self.asal= asal
        # print("fungsi init dieksekusi")

    def perkenalan(self):
        print("Perkenalkan nama saya", self.nama, "dari", self.asal)

class Pelajar(Orang):
    # sekolahnya dimana
    def __init__(self, nama, asal, sekolah):
        Orang.__init__(self, nama, asal)
        self.sekolah= sekolah

    pass

class Pekerja(Orang):
    # kerjanya dimana
    def __init__(self, nama, asal, kerja):
        Orang.__init__(self, nama, asal, kerja)
        self.kerja= kerja
    pass

dani = Orang('Dani','Zimbabwe')
dani.perkenalan()          

rahma = Pelajar('rahma','jawa','SMKJP 1')
rahma.perkenalan()
print("Saya Bersekolah di", rahma.sekolah,"/n")

arya = Pekerja('arya','pakistan','SMK JP 1')
arya.perkenalan()
print("Saya bekerja di", arya.kerja,"/n")