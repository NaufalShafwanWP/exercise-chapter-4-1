a = 200000
b = 10000

Ambil = float(input("Jam ambil mobil:"))
Kembali = float(input("Jam kembali mobil:"))
Lama_pinjam = Kembali - Ambil - 12
Biaya_setelah_12jam = a + b * Lama_pinjam
print(int(Biaya_setelah_12jam))