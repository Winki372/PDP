def KonversiSuhu(Celcius=0,Fahrenheit=0):
    if Celcius != 0:
        Fahrenheit = (9/5)*Celcius + 32
        print("Suhu", Celcius, "Celcius setara dengan", Fahrenheit, "Fahrenheit")
    elif Fahrenheit != 0:
        Celcius = (Fahrenheit-32)*(5/9)
        print("Suhu", Fahrenheit, "Fahrenheit setara dengan", Celcius, "Celcius")
    else:
        print("Suhu 0 Celcius setara dengan 32 Fahrenheit")
        print("Suhu 0 Fahrenheit setara dengan -17.77777777777778 Celcius")

#harusnya programnya diinput. tpai ini langsung disetting
print(KonversiSuhu(Celcius = 40))
print(KonversiSuhu(Fahrenheit = 95))
print(KonversiSuhu(30))
print(KonversiSuhu())
#langsung menampilkan temperature yang diprogram di atas
