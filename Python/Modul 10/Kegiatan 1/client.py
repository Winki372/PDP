import socket

HOST = 'localhost'  # Server address
PORT = 5003         # Port to connect to

# Membuat socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menghubungkan ke server
s.connect((HOST, PORT))
print("KONEKSI KE SERVER BERHASIL")

while True:
    perintah = input("Masukkan perintah anda (ketik 'q' untuk keluar): ")
    
    # Mengirimkan perintah ke server
    s.send(perintah.encode())  # Encoding input menjadi bytes
    
    if perintah.lower() == 'q':  # Jika perintah 'q', keluar dari loop
        print("Keluar dari program...")
        break
    
    # Menerima respon dari server
    response = s.recv(1024)
    print('Jawaban dari server: ', response.decode())  # Decode response menjadi string

# Menutup koneksi setelah selesai
s.close()
