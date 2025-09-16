def tambah(x,y):
    return  x + y

def kurang(x,y):
    return x - y

def kali(x,y):
    return x * y

def bagi(x,y):
    if y == 0:
        return "Error: tidak bisa membagi dengan nol!"
    return x / y

print("Selamat datang di Aplikasi kami")
print("Silahkan pilih operasi matematika di bawah ini ya:!!!")

answer = ""

while answer !="Tidak":
    print('=' * 20)
    print("Pilih Operator")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print('=' *25)

    operator = input("Masukkan operator (1.2.3.4)  :")
    angka1 = int(input("Masukkan Bilangan Pertama :"))
    angka2 = int(input("Masukan Bilangan Kedua :"))

    if operator == "1":
        print(angka1 , "+" , angka2 ,"=" , tambah(angka1,angka2))
    elif operator == "2":
        print(angka1, "+" , angka2 , "=" , kurang(angka1,angka2))
    elif operator == "3":
        print(angka1, "x" , angka2 , "=" , kali(angka1,angka2))
    elif operator == "4":
        print(angka1, "/" , angka2 , "=" , bagi(angka1,angka2))
    else:
        print("Maaf operator yang di pilih tidak Tersedia.")
    
    answer = input("Apakah ingin melakukannya lagi? Ya/Tidak: ")
    if answer =="t":
        print("Terima kasih sudah mengeluarkan aplikasi kami")
        break