berkas = open ("*******029.txt", "r+")
data = berkas.readlines()
#menggunakan readlines karena banyak baris sekaligus
data[1]="09/25/2005\n"
#ubah data pada baris indeks ke 1 menjadi yang telah ditentukan
berkas.seek(0)
#ke awal berkas untuk menulis ulang

berkas.writelines(data)
#menulis perubahan
#berkas.write("Sragen")
if "Sragen" not in data: 
    berkas.write("Sragen")
#jika string sragen tidak ada di data, tambahkan sragen ke dalam data yang ada di berkas

berkas.close()
#tutup berkas

print(f"a. {data[2]}")
print(f"b. {data[3]}, {data[1]}")
print(f"c. {data[0]}")    
#menampilkan data yang diambil
