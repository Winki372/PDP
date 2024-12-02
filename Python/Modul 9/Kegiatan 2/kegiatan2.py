berkas = open ("L300240029", "r+")
data = berkas.readlines()

data[1]="09/25/2005\n"

berkas.seek(0)

berkas.writelines(data)
if "Sragen" not in data: 
    berkas.write("Sragen")
berkas.close()

print(f"a. {data[2]}")
print(f"b. {data[3]}, {data[1]}")
print(f"c. {data[0]}")    

