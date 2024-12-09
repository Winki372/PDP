import socket

HOST = 'localhost'  # Server address
PORT = 5003         # Port to connect to

# Membuat socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menghubungkan ke server
s.connect((HOST, PORT))
print("KONEKSI KE SERVER BERHASIL")

# Meminta input dari pengguna untuk luas alas dan luas selimut
luas_alas = input("Masukkan luas alas: ")
luas_selimut = input("Masukkan luas selimut: ")

# Mengirim data ke server
s.sendall(f"{luas_alas},{luas_selimut}".encode())

# Menerima respon dari server
response = s.recv(1024).decode()
print(f"Respon dari server: {response}")

# Loop untuk menerima perintah dari pengguna
while True:
    perintah = input("Masukkan perintah anda (ketik 'keluar' untuk keluar): ")
    
    # Mengirimkan perintah ke server
    s.sendall(perintah.encode())  # Encoding input menjadi bytes

    # Jika perintah 'hitung' diterima
    if perintah.lower() == 'hitung':  
        # Menerima hasil perhitungan dari server
        response = s.recv(1024).decode()
        print(f"Hasilnya adalah: {response}")
        break  # Keluar dari loop setelah menerima hasil
    
    # Jika perintah 'keluar' diterima
    elif perintah.lower() == 'keluar':
        # Mengirimkan perintah keluar dan menerima pesan terima kasih
        response = s.recv(1024).decode()
        print(response)
        break  # Keluar dari loop

    else:
        # Jika perintah tidak dikenali
        response = s.recv(1024).decode()
        print(f"Jawaban dari server: {response}")

# Menutup koneksi setelah selesai
s.close()
