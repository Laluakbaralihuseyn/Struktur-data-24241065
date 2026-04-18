nama_anda= "akbar"

while True:
    nama_input = input("masukkan nama anda:")
    if nama_input == nama_anda:
        print("jika benar akan langjut ke program selanjutnya")
        break
    else:
        print("silahkan coba lagi")

angka = int(input("masukkan angka:"))

i = 4
while i <=15 :
    hasil =angka * 4
    print(f"{angka}*{i}={hasil}")
    i=i=4
