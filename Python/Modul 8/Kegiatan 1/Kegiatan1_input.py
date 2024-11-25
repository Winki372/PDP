import Kegiatan1_Modul
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
        Kegiatan1_Modul.nama()
    elif pilihan == 'b':
        Kegiatan1_Modul.nim()
    elif pilihan == 'c':
        Kegiatan1_Modul.alamat()
    elif pilihan == 'd':
        Kegiatan1_Modul.gender()
    elif pilihan == 'e':
        Kegiatan1_Modul.umur()
    elif pilihan == 'f':
        Kegiatan1_Modul.kesibukan()
    elif pilihan == 'g':
        Kegiatan1_Modul.hobi()
    elif pilihan == 'k':
        print('terima kasih, selesai')
    else:
        print('pilihan tidak dikenal')
