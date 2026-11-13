#No 1
print("Soal NO.1")
def cetak_garis():
    print("="*40)
cetak_garis()
print()

#No 2
print("Soal NO.2")
hasil=[]
def luas_persegi(x,y,z):
    L=x*x
    M=y*y
    N=z*z
    return L, M, N
L, M, N = luas_persegi(5,10,15)
hasil.extend([L, M, N])
print("Luas persegi adalah:", hasil)
print()

#No 3
print("Soal NO.3")
def cek_genap(angka):
    if angka % 2 == 0:
        return True
    else:
        return False
status_angka= cek_genap(10)
print("Status angka genap:", status_angka) 
print()

#No 3.1
print("Soal NO 3.1")

def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    print(f"Luas persegi adalah: {luas}")
    return luas

def rata_rata_luas(daftar_luas):
    rata = sum(daftar_luas) / len(daftar_luas)
    print(f"Rata-rata luas persegi adalah: {rata}")

# Menghitung luas masing-masing persegi
hasil = []
for sisi in [5, 10, 15]:
    hasil.append(hitung_luas_persegi(sisi))

# Menghitung rata-rata
rata_rata_luas(hasil)
print()

#No 4 
print("Soal NO.4")
def salam (waktu, nama="Kawan"):
    print(f"Selamat {waktu},{nama}!")

salam("Pagi", "Andi")
salam("Sore")
print()

#No 5
print("Soal No.5")

def konversi_nilai(nilai_angka):
    if nilai_angka>=86:
        return "A"
    elif nilai_angka >= 76 and nilai_angka < 86 :
        return "AB"
    elif nilai_angka>= 66 and nilai_angka < 76 :
        return "B"
    else:
        return "C"

nilai_angka=int(input("Input Your Scor :"))
indeks = konversi_nilai(nilai_angka)
print(f"Nilai huruf Anda adalah :{indeks}")