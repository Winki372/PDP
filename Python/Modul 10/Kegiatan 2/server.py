import socket
import platform

HOST = 'localhost'  # Server address
PORT = 5003         # Port to connect to

list_perintah = {
    'mesin': platform.machine(),
    'sistem': platform.system(),
    'versi': platform.version(),
    'node': platform.node(),
    'keluar': ''
}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))  # Binding ke host dan port
s.listen(5)  # Menunggu koneksi masuk
print("SISTEM IS READY")

# Menunggu koneksi dari klien
kon, addr = s.accept()
print(f"Terhubung dengan {addr}")

while True:
    data = kon.recv(1024).decode()  # Menerima data dan mendekode dari bytes ke string
    if data.lower() == 'q':  # Jika klien mengirim 'q', keluar dari loop
        print("Koneksi ditutup oleh klien.")
        break
    print(f'Masukkan perintah dari klien: {data}')
    
    # Menyampaikan respon sesuai list_perintah
    if data in list_perintah:
        response = list_perintah[data]
    else:
        response = 'Pertanyaan macam apa ini?'
    
    kon.send(response.encode())  # Mengirimkan balasan dalam bentuk bytes

# Menutup koneksi setelah selesai
kon.close()
s.close()
