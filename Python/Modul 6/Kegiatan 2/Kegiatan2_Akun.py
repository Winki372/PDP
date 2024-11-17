##Program Akun 
##Dibuat oleh Thoxxx xxxxxx xxxxxxxx
import random

Nama = 'Thoxxx xxxxxx xxxxxxxx'
Tanggal_Lahir = '25 xxxxxxxxx xxxx'
Angka_Acak = ''.join([str(random.randint(0,5)) for i in range(3)])
Nama_Singkat = f"{Nama[:6]} {Nama[7]}.{Nama[14]}"
Username = (Nama[0])+(Tanggal_Lahir[:2])+(Tanggal_Lahir[-4:])
Password = (Nama[:3])+(Angka_Acak)
#------------------------------------------------------------------
print(f"Nama : {Nama}")
print(f"Tanggal Lahir : {Tanggal_Lahir}")
print(f"Nama Singkat : {Nama_Singkat}")
print(f"Username : {Username}")
print(f"Password Sementara : {Password}")
