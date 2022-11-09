def menu():
    capu = "Cappucino"
    teh = "Teh"
    print ("Pilihan")
    print ("1.", capu)
    print ("2.", teh)
    print ("3. Keluar")

def welcome():
    nama = (input("Masukkan nim : ") )
    nim =  (input("Nama : "))

def cappucino():
    capu = "Memilih cappucino"
    print (capu)
    capcin = int(input("Masukkan harga : "))
    bayar = capcin + (capcin * 10 / 100)
    print(bayar)

def tehh():
    teh = "Memilih teh"
    print(teh)
    tehh = int(input("Masukkan harga : "))
    bayar = tehh + (tehh * 10 / 100)
    print (bayar)


while True:
    welcome()
    menu()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        cappucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print ("pilihan salah")
