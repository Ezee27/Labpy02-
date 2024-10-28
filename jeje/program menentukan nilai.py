#!/usr/bin/python3

nama = input("Masukkan nama: ")
uts = input("Masukkan nilai UTS: ")
uas = input("Masukkan nilai UAS: ")
tugas = input("Masukkan nilai Tugas: ")

# Menghitung nilai akhir
akhir = (int(tugas) * 0.2) + (int(uts) * 0.4) + (int(uas) * 0.4)

# Menentukan keterangan LULUS atau TIDAK LULUS
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]

# Menentukan nilai huruf berdasarkan nilai akhir
if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "E"

# Mencetak hasil
print("\nNama :", nama)
print("Nilai UTS :", uts)
print("Nilai UAS :", uas)
print("Nilai Tugas :", tugas)
print("Nilai Akhir :", akhir)
print("\nNilai Huruf :", huruf)
print("Keterangan :", keterangan)