import Kegiatan1_MembuatModul_1

menu ='''
PILIHAAN YANG TERSEDIA:
[a] menampilkan nama
[b] menampilkan nim
[c] menampilkan alamat
[d] menampilkan gender
[e] menampilkan umur
[f] menampilkan kesibukan
[g] menampilkan hobi
[k] keluar
'''

print(menu)

pilihan = ''

while (pilihan != 'k'):
    pilihan = input("masukkan perintah: ")

    if pilihan == 'a':
        Kegiatan1_MembuatModul_1.nama()
    elif pilihan == 'b':
        Kegiatan1_MembuatModul_1.nim()
    elif pilihan == 'c':
        Kegiatan1_MembuatModul_1.alamat()
    elif pilihan == 'd':
        Kegiatan1_MembuatModul_1.gender()
    elif pilihan == 'e':
        Kegiatan1_MembuatModul_1.umur()
    elif pilihan == 'f':
        Kegiatan1_MembuatModul_1.kesibukan()
    elif pilihan == 'g':
        Kegiatan1_MembuatModul_1.hobi()
    elif pilihan == 'k':
        print('terima kasih, selesai')
    else:
        print('pilihan tidak dikenal')