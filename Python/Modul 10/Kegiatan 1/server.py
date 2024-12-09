import socket

HOST = 'localhost'  # Server address
PORT = 5003         # Port to connect to

data_diri = {
    'nama': 'THORIQ SAIFUL MUHSININ',
    'nim': 'xxxxxxx029',
    'angkatan': '2024',
    'keluar': 'siap'
}

# Membuat socket untuk server
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
    
    # Menyampaikan respon sesuai data_diri
    if data in data_diri:
        response = data_diri[data]
    else:
        response = 'Pertanyaan macam apa ini?'
    
    kon.send(response.encode())  # Mengirimkan balasan dalam bentuk bytes

# Menutup koneksi setelah selesai
kon.close()
s.close()
