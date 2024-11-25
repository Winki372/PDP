def KonversiSuhu(C=0,F=0):
    if C != 0:
        F = (9/5)*C + 32
        print("Suhu", C, "Celcius setara dengan", F, "Fahrenheit")
    elif F != 0:
        C = (F-32)*(5/9)
        print("Suhu", F, "Fahrenheit setara dengan", C, "Celcius")
    else:
        print("Suhu 0 Celcius setara dengan 32 Fahrenheit")
        print("Suhu 0 Fahrenheit setara dengan -17.77777777777778 Celcius")

#harusnya programnya diinput. tapi ini langsung disetting
print(temperatureConveter(C = 40))
print(temperatureConveter(F = 95))
print(temperatureConveter(30))
print(temperatureConveter())
#langsung menampilkan temperature yang diprogram di atas
