Nama: ZAENAL MAULANA RIZKI

Kelas: TI.24.A4

NIM: 312410332

Matkul: Bahasa Pemrograman

# Struktur Kondisi
Penggunaan struktur kondisi menggunakan statement `if`, Konsep pemrograman yang memungkinkan program untuk mengambil keputusan berdasarkan kondisi atau pernyataan tertentu. Struktur seleksi kondisi yang umum digunakan dalam Python

if : Digunakan untuk mengevaluasi suatu kondisi. Jika kondisi tersebut benar (True)

else : Digunakan untuk menentukan apa yang terjadi jika kondisi `if` adalah salah (False)

elif : digunakan untuk mengevaluasi beberapa kondisi. Jika kondisi `if` pertama salah, Python akan mengevaluasi kondisi `elif`. Anda bisa memiliki beberapa `elif`

# Soal latihan
![Screenshot From 2024-10-24 20-34-23](https://github.com/user-attachments/assets/f8dbc4c6-fcd1-49de-b9e2-e96de8af040c)


# Program menentukan nilai akhir
```python
nama = input("Masukkan nama:")
uts = input("Masukkan nilai UTS:")
uas = input("Masukkan nilai UAS:")
tugas = input("Masukkan nilai Tugas:")

akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(uas) * .4)
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]
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
print("\nNama :",nama)
print("Nilai UTS :",uts)
print("Nilai UAS :",uas)
print("Nilai Tugas :",tugas)
print("Nilai Akhir :",akhir)
print("\nNilai Huruf :",huruf)
print("Keterangan :",keterangan)
````

Untuk menentukan nilai akhir pada Python, Anda bisa menggunakan pernyataan `return` untuk menandai akhir fungsi atau Menggunakan fungsi `print()` dan menentukan nilai yang akan dikembalikan. Pernyataan `return` dapat mengembalikan berbagai jenis data, seperti `integer`, `float`, `string`, `list`, `dictionary`, dan fungsi lainnya.

```python
nama = input("Masukkan nama:")
uts = input("Masukkan nilai UTS:")
uas = input("Masukkan nilai UAS:")
tugas = input("Masukkan nilai Tugas:")
````
Fungsi `input()` adalah fungsi untuk menerima masukan dari pengguna dalam bentuk string, 

```python
akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(uas) * .4)
````
Fungsi `int(tugas)`, `int(uts)`, dan `int(uas)` digunakan untuk mengonversi nilai input (yang masih berupa string) menjadi bilangan bulat (integer).

```python
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]
````
Jika nilai `akhir` lebih besar dari 60, maka `keterangan` berisi "LULUS", jika tidak, maka "TIDAK LULUS"

```Python
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
````

Ini adalah Struktur Kondisi Yang Menggunakan `If`, `Elif`, dan `Else`

```Python
print("\nNama :",nama)
print("Nilai UTS :",uts)
print("Nilai UAS :",uas)
print("Nilai Tugas :",tugas)
print("Nilai Akhir :",akhir)
print("\nNilai Huruf :",huruf)
print("Keterangan :",keterangan)
````

Fungsi `Print()` ini akan mencetak Variable-Variable program tersebut

Hasil output

![Screenshot (44)](https://github.com/user-attachments/assets/cc08325a-3b83-4d0c-b1b7-c4aed2f3b48b)

# Program menampilkan status gaji karyawan
```Python
gaji = int(input("Masukkan gaji:"))
berkeluarga = (False, True)[input("Sudah berkeluarga? (Y/T)") == "Y"]
punya_rumah = (False, True)[input("Punya rumah? (Y/T)") == "Y"]


if gaji > 3000000:
    print ("Gaji sudah diatas UMR")
    if berkeluarga:
        print ("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print ("Tidak perlu ikutan asuransi")
    if punya_rumah:
        print ("wajib bayar pajak rumah")

    else:
        print ("tidak wajib bayar pajak rumah")
else:
    print ("Gaji belum UMR")
````
Struktur Kondisi Ini menggunakan desision `if, `elif`, dan `else`

```Python
gaji = int(input("Masukkan gaji:"))
````
Program meminta pengguna memasukkan gaji dengan fungsi `input()`

```Python
berkeluarga = (False, True)[input("Sudah berkeluarga? (Y/T)") == "Y"]
punya_rumah = (False, True)[input("Punya rumah? (Y/T)") == "Y"]
````
Inputan ini menggunakan fungsi `string` yang dimasukan berupa Huruf, dan `(False, True)` ini adalah fungsi pemilihan Y atau T, supaya tidak menggunakan if dilanjutan program tersbut

```Python
if berkeluarga:
        print("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print("Tidak perlu ikutan asuransi")
````
Jika angka gaji lebih dari 3 juta maka Output yang akan keluar "Gaji sudah diatas UMR", dan jika tidak `Output` yang keluar "Tidak perlu ikutan asuransi"

```Python
if punya_rumah:
        print ("wajib bayar pajak rumah")

    else:
        print ("tidak wajib bayar pajak rumah")
````
Jika Memiliki rumah `Output` yang keluar "Wajib bayar Pajak", jika tidak `output` yang keluar "Tidak wajib bayar pajak"

```Python
else:
    print ("Gaji belum UMR")
````
Jika gaji pengguna tidak lebih dari 3 juta, program akan mencetak "Gaji belum UMR".

Hasil output

![Screenshot (45)](https://github.com/user-attachments/assets/709da17d-cfae-4e83-a528-1f4f766cda03)

# Menggunakan kondisi or dengan menginputkan 3 bilangan
```Python
a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
c = int(input("Masukkan bilangan C: "))

if a+b == c or b+c == a or c+a == b:
    print("BENAR")
else:
    print("SALAH")
````
Dalam Python mengevaluasi beberapa kondisi dan mengembalikan True jika salah satu kondisinya benar.

```Python
a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
c = int(input("Masukkan bilangan C: "))
````
Program meminta pengguna untuk memasukkan tiga bilangan `(a, b, dan c)`.

```python
if a+b == c or b+c == a or c+a == b:
    print("BENAR")
else:
    print("SALAH")
````
Bagian ini memeriksa tiga kondisi menggunakan operator logika `or`, jika salah satu dari kondisi di atas terpenuhi, program akan mencetak "BENAR", 
 Jika tidak ada satu pun dari kondisi yang terpenuhi, maka blok `else` akan dijalankan, dan program akan mencetak "SALAH".

Hasil output

![Screenshot (46)](https://github.com/user-attachments/assets/d4908db4-8ef3-4d6a-9534-1fcb9439f10c)

# Latihan3
# Program tiket bioskop

![Screenshot From 2024-10-25 07-25-48](https://github.com/user-attachments/assets/2f9fa784-6b7c-46d1-a3ee-e785b82e5485)

```python
# Fungsi untuk menghitung harga tiket
def hitung_harga_tiket():
    # Harga tiket
    harga_reguler = 50000
    harga_vip = 100000
    diskon_member = 0.20  # Diskon 20%

    # Meminta input dari pengguna
    tipe_tiket = input("Masukkan tipe tiket (reguler/VIP): ").strip().lower()
    status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()

    # Menentukan harga berdasarkan tipe tiket
    if tipe_tiket == "reguler":
        harga_tiket = harga_reguler
    elif tipe_tiket == "vip":
        harga_tiket = harga_vip
    else:
        print("Tipe tiket tidak valid!")
        return

    # Menghitung total harga dengan diskon jika berlaku
    if status_member == "ya":
        total_harga = harga_tiket * (1 - diskon_member)
    elif status_member == "tidak":
        total_harga = harga_tiket
    else:
        print("Status member tidak valid!")
        return

    # Menampilkan total harga
    print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")

# Memanggil fungsi
hitung_harga_tiket()
````
Program ini akan menentukan harga pesanan tiket bioskop, Yang reguler/Vip, dan jika Vip harga 100.000, dan jika reguler 80.0000, dan jika memiliki kartu member pelanggan tersebut akan mendapatkan diskon 20%

```python
harga_reguler = 50000
harga_vip = 100000
````
Untuk menentukan harga tiket tersebut

```python
tipe_tiket = input("Masukkan tipe tiket (reguler/VIP): ").strip().lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()
````
Pengguna diminta untuk memasukkan tipe tiket yang mereka inginkan, bisa "reguler" atau "VIP", Pengguna juga diminta untuk menjawab apakah mereka memiliki kartu member, dengan pilihan "ya" atau "tidak"

```python
if tipe_tiket == "reguler":
    harga_tiket = harga_reguler
elif tipe_tiket == "vip":
    harga_tiket = harga_vip
else:
    print("Tipe tiket tidak valid!")
    return
````
Jika tipe tiket adalah "reguler", harga tiket akan diatur menjadi harga_reguler (Rp50.000), Jika tipe tiket adalah "VIP", harga tiket akan diatur menjadi harga_vip (Rp100.000), Jika tipe tiket yang dimasukkan tidak valid, fungsi akan menampilkan pesan error dan menghentikan proses

```python
if status_member == "ya":
    total_harga = harga_tiket * (1 - diskon_member)
elif status_member == "tidak":
    total_harga = harga_tiket
else:
    print("Status member tidak valid!")
    return
````
Jika pengguna adalah member `(status_member == "ya")`, harga tiket akan dikurangi diskon 20%, Jika pengguna bukan member `(status_member == "tidak")`, harga tiket tetap sama tanpa pengurangan, Jika input untuk status member tidak valid, misalnya selain "ya" atau "tidak", fungsi akan menampilkan pesan error dan menghentikan eksekusi

```python
print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")
hitung_harga_tiket()
````
Setelah menghitung total harga, anda dapat langsung menjalankan fungsinya

Hasil program tersebut:

![Screenshot (47)](https://github.com/user-attachments/assets/1ff29a57-b4ea-4b6b-9d47-2ca1beb169d4)

Code program tersebut:

![Screenshot (48)](https://github.com/user-attachments/assets/ba884b84-ccaf-4cd2-8324-79b8439ca699)

Dan ini flowchart nya

![tiket biskop](https://github.com/user-attachments/assets/e4954a9c-ed41-4b0a-9371-eff8caf81703)

# Program kalkulator sederhana
![gambar](https://github.com/andreanbadeh/Labpy02/blob/e5c4003cbb820d9875a5e7ae0053af58ef5d122c/Image/Screenshot%20From%202024-10-25%2007-25-56.png)
```pyhton
# Fungsi untuk kalkulator sederhana
def kalkulator():
    # Meminta input dari pengguna
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    operator = input("Masukkan operator (+, -, *, /): ").strip()

    # Menghitung hasil berdasarkan operator yang dipilih
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan!")
            return
    else:
        print("Error: Operator tidak valid!")
        return

    # Menampilkan hasil
    print(f"Hasil: {hasil}")

# Memanggil fungsi
kalkulator()
````
Program kalkulator sederhana dalam Python adalah proyek yang baik untuk pemula dan programmer tingkat lanjut. Program ini memungkinkan pengguna untuk melakukan operasi matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian.

```python
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+, -, *, /): ").strip()
````
Pengguna diminta memasukkan angka pertama dan angka kedua, yang kemudian dikonversi menjadi tipe float agar bisa menerima bilangan desimal, Pengguna diminta memasukkan operator aritmatika, yaitu salah satu dari + (penjumlahan), - (pengurangan), * (perkalian), atau / (pembagian). Fungsi strip() digunakan untuk menghapus spasi yang mungkin tidak sengaja dimasukkan.

```python
if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")
        return
````
Jika operator adalah `+`, maka fungsi akan menjumlahkan kedua angka `(angka1 + angka2)`, Jika operator adalah `-`, maka fungsi akan mengurangi angka pertama dengan angka kedua `(angka1 - angka2)`, 
Jika operator adalah `*`, maka fungsi akan mengalikan angka pertama dengan angka kedua `(angka1 * angka2)`, Jika operator adalah `/`, maka fungsi akan membagi angka pertama dengan angka kedua `(angka1 / angka2)`. Namun, sebelum melakukan pembagian, fungsi memastikan bahwa angka kedua `(angka2)` tidak bernilai nol, karena pembagian dengan nol tidak valid dan akan menyebabkan error.

```python
else:
    print("Error: Operator tidak valid!")
    return
print(f"Hasil: {hasil}")
kalkulator()
````
Jika pengguna memasukkan operator yang tidak dikenali (bukan `+, -, *, atau /`), Setelah operasi berhasil dijalankan, hasil perhitungan akan ditampilkan kepada pengguna

Hasil program tersebut:

![Screenshot (50)](https://github.com/user-attachments/assets/901416c4-7154-4f5d-b69f-3e9c0eccf2d3)

Code program tersebut:

![Screenshot (49)](https://github.com/user-attachments/assets/ceb215b0-d8c5-4af5-b416-09196cc6bf3f)

Dan ini flowchart nya

![Screenshot 2024-10-26 051738](https://github.com/user-attachments/assets/5d36b67c-db9b-4939-98f9-1bed18b1f486)
