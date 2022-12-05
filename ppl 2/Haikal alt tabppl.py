class angka:
    def __init__(self, angka):
        self.angka = angka

    def __add__(self,objek):   
         return angka  (self.angka  + objek.angka
         )

x1 = angka(7)
x2 = angka(8) 
x3 = x1 + x2
print(x3.angka) 

class angka:
    def __init__(self, a, o):
        self.a = a
        self.o = o

    def __str__(self):
        hasil =  self.a + self.o
        return f'Hasil dari {self.a} + {self.o} adalah : {hasil}'

a = angka(int(input("masukan angka 1 : ")),int(input("masukan angka 2 : ")))    
print(a)    

