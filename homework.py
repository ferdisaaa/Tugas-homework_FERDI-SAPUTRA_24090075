daftar_buku = [
    {"judul": "superman", "penulis": "Arya"},
    {"judul": "laskar pelangi", "penulis": "Ucup"},
    {"judul": "batas senja", "penulis": "Nichol"},
    {"judul": "bumi manusia ", "penulis": "Siganteng"},
    {"judul": "bukan untuk dibaca", "penulis": "Mulyono"},
    {"judul": "sebuah tutorial", "penulis": "Jefri"},
]

# Daftar untuk menyimpan hasil pencarian
hasil_pencarian = []

# Fungsi untuk mencari buku
def cari_buku(judul):
    hasil_pencarian.clear()  # Kosongkan daftar hasil pencarian
    for buku in daftar_buku:
        if judul.lower() in buku["judul"].lower():
            hasil_pencarian.append(f"Buku ditemukan: {buku['judul']} oleh {buku['penulis']}")

    if not hasil_pencarian:
        hasil_pencarian.append("Buku tidak ditemukan.")

# Input untuk mencari buku
judul_cari = input("Masukkan judul buku yang ingin dicari: ")
cari_buku(judul_cari)

# Tampilkan hasil pencarian
for hasil in hasil_pencarian:
    print(hasil)