1#
Nama = 'Thoxxx xxxxxx xxxxxxxx'
Nim = 'xxxxxxx029'
x = '1' + Nim[7:]
#1029 . Karena,
a = int(x)
#1029 . Karena, '1' + indeks ke 7-selesai dari string
b =  len(Nama)
#22 . Karena, panjang dari string nama
#----------------------------------------------------------
#2
type(a)
#<class 'int'> . Karena, isi dari variabel a(1029) bertipe integer
type(b)
#<class 'int'> . Karena, tipe dari variabel b(22) bertipe integer
z = a/b
#46.77272727272727 . Karena, hasil bagi dari variabel a(1029) dibagi dengan variabel b(22)
y = a//b
#46 . Karena, pembulatan dari hasil bagi dari variabel a(1029) dibagi dengan variabel b(22)
w = 10*(a-999)
#300 . Karena, pengerjaan di dalam kurung yang dilakukan dulu, variabel a(1029) dikurangi 999. lalu dikali dengan 10
v = b**2
#484 . Karena, pangkat 2 dari variabel b(22)
u = a%b
#17 . Karena, sisa hasil bagi dari variabel a(1029) dan b(22)
#----------------------------------------------------------------------
#3
c = 12.5
type(c)
#<class 'float'> . Karena, isi dari variabel c(12.5) bertipe desimal
t = a/c
#82.32 . Karena hasil dari pembagian variabel a(1029) dengan variabel c(12.5)
s = a//c 
#82.0 . Karena pembulatan dari hasil bagi variabel a(1029) dengan variabel c(12.5)
r = a%c
#4.0 . Karena, sisa hasil bagi dari variabel a(1029) dengan variabek c(12.5)
#---------------------------------------------------------------------------------
#4
q = c > b
#False . Karena, nilai dari variabel c(12.5) kurang dari nilai variabel b(22)
type(c>b)
#<class 'bool'> . Karena, hasil dari perbandingan tersebut bertipe true/false
p = a > b and b > c
#True . Karena, hasil dari kedua perbandingan tersebut benar semua
o = a > 1100 or b < 10
# False . Karena hasil dari perbandingan tersebut tidak benar
#---------------------------------------------
print('1.')
print(x)
print(a)
print(b)
print('---------------------------')
print('2.')
print(type(a))
print(type(b))
print(z)
print(y)
print(w)
print(v)
print(u)
print('---------------------------')
print('3.')
print(c)
print(type(c))
print(t)
print(s)
print(r)
print('--------------------------')
print('4.')
print(q)
print(type(c>b))
print(p)
print(o)
