# variabel celcius digunakan untuk menampung nilai dari input
# input yang dimasukkan oleh user, akan bernilai string meskipun itu nomor
# maka, diperlukan konversi tipe data agar perhitungan angkanya bisa diteruskan
# dengan rumus konversi celcius ke fahrenheit

# gunakan int() untuk mengkonversi string ke integer
# input() digunakan untuk merekam nilai input yang dimasukkan oleh user

# jadi alurnya begini
# input -> konversi -> simpan ke variabel
celcius = int(input("Masukkan nilai celcius : "))

# disini proses perhitungan terjadi/ yang dimana nilai input (yang disimpan pada variabel celcius)
# dikalikan dengan 9, dibagi 5 lalu ditambah 32
# rumus konversi (...°C * 9/5) + 32 = ... °F
fahrenheit = celcius * 9 / 5 + 32

# menampilkan hasil konversi yang ditampung variable fahrenheit dengan menggunakan print()
print("Hasil konversi : ", fahrenheit, "°F")
