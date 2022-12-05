print('Program menghitung\n1. luas Balok\n2. Luas Kubus\n3. Luas Lingkaran\n4. Luas Tabung')
pilihan = int(input('Masukan pilihan: '))
 
def luas_balok(p,l,t):
    B = 2 * ( (p*l) + (p*t) + (l*t) )
    return B
 
def luas_kubus(r):
    K = 6 * ( (r*r))
    return K
 
def luas_lingkaran(r):
    L = 4 * (r)
    return L

def luas_tabung(p,l,t):
    T = 4 * (p + l + t)
    return T
 
if pilihan == 1:
    p = int(input('masukan panjang balok: '))
    l = int(input('masukan lebar balok: '))
    t = int(input('masukan tinggi balok: '))
    luas_balok(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai luas:{}'.format(p,l,t, luas_balok(p,l,t)))
 
elif pilihan == 2:
    r = int(input('masukan panjang Rusuk: '))
    luas_kubus(r)
    print('Jadi Kubus dengan ukuran panjang:{}'.format(r, luas_kubus(r)))
 
elif pilihan == 3:
    p = int(input('masukan panjang balok: '))
    l = int(input('masukan lebar balok: '))
    t = int(input('masukan tinggi balok: '))
    keliling(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai keliling:{}'.format(p,l,t, keliling(p,l,t)))

elif pilihan == 4:
    p = int(input('masukan panjang balok: '))
    l = int(input('masukan lebar balok: '))
    t = int(input('masukan tinggi balok: '))
    keliling(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai keliling:{}'.format(p,l,t, keliling(p,l,t))) 
    
else:
    print('Pilihan tidak tersedia')