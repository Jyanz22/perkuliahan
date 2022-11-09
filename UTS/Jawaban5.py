def penjualan():
    c = "Capucino"
    t = "Teh"
    print ("pilihan")
    print ("1.", c)
    print ("2.", t)
    print ("3.", exit)

def welcome():
    nim = (input("NIM : "))
    nama = (input("Nama : "))

def capucino():
    c = "memilih Capucino"
    print (c)
    harga = int(input("Masukan Harga : "))
    bayar = harga + (harga * 10/ 100)
    print ("Jumlah yang harus dibayar : ", bayar)

while True:
    welcome()
    penjualan()
    choice = int(input("Masukan Pilihan : "))
    if choice == 1:
        capucino()
    elif choice == 2:
        Teh()
    elif choice == 3:
        break
    else:
        print ("pilihan salah")    