# import ini jangan dihapus/diedit yak
import random

def totalPenjualan(data, n):
    if n != 0:
        return data[n - 1][1] + totalPenjualan(data, n - 1)
    else:
        return 0

def penjualanTertinggi(data, n):
    if n != 1:
        if data[0][1] > penjualanTertinggi(data[1:], n - 1)[1]:
            return data[0]
        else:
            return penjualanTertinggi(data[1:], n - 1)
    else:
        return data[0]

def diAtasRataRata(penjualan, rataRata):
    temp = 0
    for i in penjualan.values():
        if i > rataRata:
            temp += 1
        else:
            temp = temp
    return temp
        

# Program Utama - Jangan dihapus/diedit yak
angka = int(input("NIM: "))
random.seed(angka)

barang = [
    "Beras",
    "Minyak",
    "Gula",
    "Telur",
    "Kopi",
    "Teh"
]

penjualan = {}

for namaBarang in barang:
    penjualan[namaBarang] = random.randint(100, 500)

data = list(penjualan.items())
n = len(data)

print("\n===== Data Penjualan =====")
for namaBarang, jumlah in penjualan.items():
    print(namaBarang, ":", jumlah)

total = totalPenjualan(data, n)
tertinggi = penjualanTertinggi(data, n)
rataRata = total / n
jumlahDiAtasRataRata = diAtasRataRata(penjualan, rataRata)

print("\n===== Hasil Analisis =====")
print("Total penjualan        :", total)
print("Penjualan tertinggi    :", tertinggi[0], "(", tertinggi[1], ")")
print("Rata-rata penjualan    :", round(rataRata, 2))
print("Di atas rata-rata      :", jumlahDiAtasRataRata, "barang")