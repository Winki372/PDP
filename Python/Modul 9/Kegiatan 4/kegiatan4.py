import shelve

f = open("L300240029", 'r')
data = f.readlines()

nim = data[0].strip()
tanggal_lahir = data[1].strip()
nama = data[2].strip()
kota = data[3].strip()

f = shelve.open("Thoriq")
f['nim']= nim.strip() 
f['tgl_lahir']=tanggal_lahir.strip()
f['nama']=nama.strip()
f['kota']=kota.strip()

print(f['nim'])
print(f['tgl_lahir'])
print(f['nama'])
print(f['kota'])
f.close()