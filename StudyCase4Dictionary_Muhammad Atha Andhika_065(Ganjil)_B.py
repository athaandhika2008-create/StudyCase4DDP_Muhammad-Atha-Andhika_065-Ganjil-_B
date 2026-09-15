buku = {
    "Judul" : "Langkah Mudah Belajar Analisis Data dengan Python untuk Pemula",
    "Penulis" : "Randi Adrika Putra",
    "Tahun_Terbit" : "2024"
}

databukuawal = {
    "Judul" : "Langkah Mudah Belajar Analisi Data dengan Python untuk Pemula",
    "Penulis" : "Randi Adrika Putra",
    "Tahun_Terbit" : "2024"
}

print(buku)

while True:
    print("===== MENU =====")
    print("1. Tampilkan Data Buku")
    print("2. Tambahkan Data Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. Selesai")

    pilihmenu = input("Silahkan Memilih Menu (1-5): ")

    if pilihmenu == "1":
        print("\n-DATA BUKU")
        for key in buku:
            print(key, ":", buku[key])

    elif pilihmenu == "2":
        penerbit = input("Masukkan Nama Penerbit: ")
        buku["Penerbit"] = penerbit

        print("Data Penerbit Berhasil Ditambahkan!")
        print("\n-DATA BUKU")
        for key in buku:
            print(key, ":", buku[key])

    elif pilihmenu == "3":
        ubahpenulis = input("Masukkan Nama Penulis Baru: ")
        buku["Penulis"] = ubahpenulis

        print("Data Penulis Berhasil Diperbarui!")
        print("\n-DATA BUKU")
        for key in buku:
            print(key, ":", buku[key])

    elif pilihmenu == "4":
        if "Penerbit" in buku:
            del buku["Penerbit"]
            print("Data Penerbit Berhasil Dihapus!")
        else:
            print("Data Penerbit Tidak Ditemukan!")

        print("\n-DATA BUKU")
        for key in buku:
            print(key, ":", buku[key])

    elif pilihmenu == "5":
        print("\nProgram Selesai!")
        break

    else:
        print("Pilihan Menu Tidak Valid! Silahkan Pilih Menu (1-5)!")

print("===== Data Buku Sebelum Perubahan =====")
for key in databukuawal:
    print(key, ":", databukuawal[key])

print("\n===== Data Buku Setelah Perubahan =====")
for key in buku:
    print(key, ":", buku[key])