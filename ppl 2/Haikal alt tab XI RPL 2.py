#public access
class siswa:
    def __init__(self , nama):
        self.nama = nama
nama_org =  siswa('Dava')
print(f'Siswa Kami bernama {nama_org.nama}')    

#protected
class sepuh:
    def __init__(self, murid):
        self._murid = murid

class tzy(sepuh):
    def __init__(self, murid, guru):
        super().__init__(murid)
        self._guru = guru
    
    def kov(self):
        print(f'Guru {self._murid} bernama {self._guru}')
wzk = tzy('Dava', 'Arya')
wzk.kov()

#prifate
class kepsek:
    def __init__(self, nama):
        self.__nama = nama

    def engkong_kepsek(self):
        print(f'Kepsek Arya bernama {self.__nama}')

om = kepsek('Pak Lilik')
om.engkong_kepsek()
