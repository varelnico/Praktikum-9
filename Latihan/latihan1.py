txt = "Hello World"

# Hitung jumlah karakter
print("Jumlah karakter:", len(txt))

# Ambil karakter terakhir
print("Karakter terakhir:", txt[-1])

# Ambil karakter index ke-2 sampai ke-4 (llo)
print("Index 2 sampai 4:", txt[2:5])

# Hilangkan spasi
print("Tanpa spasi:", txt.replace(" ", ""))

# Ubah menjadi huruf besar
print("Huruf besar:", txt.upper())

# Ubah menjadi huruf kecil
print("Huruf kecil:", txt.lower())

# Ganti karakter H dengan J
print("Ganti H jadi J:", txt.replace("H", "J"))