import socket

HOST = 'localhost'  # Server address
PORT = 5003         # Port to connect to

# Variabel untuk menyimpan data
luas_alas = 0
luas_selimut = 0

# Membuat socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))  # Binding ke host dan port
s.listen(5)  # Menunggu koneksi masuk
print("SISTEM IS READY")

# Menunggu koneksi dari klien
kon, addr = s.accept()
print(f"Terhubung dengan {addr}")

while True:
    try:
        data = kon.recv(1024).decode()  # Menerima data dan mendekode dari bytes ke string
        
        if not data:  # Jika tidak ada data yang diterima, koneksi mungkin terputus
            print("Koneksi terputus.")
            break

        if data.lower() == 'keluar':  # Jika klien mengirim 'keluar', keluar dari loop
            kon.send("thanks.".encode())  # Mengirim pesan terima kasih
            break
        
        try:
            # Memisahkan data luas alas dan luas selimut
            luas_alas, luas_selimut = map(float, data.split(','))
            print(f"Parameter diterima: luas alas = {luas_alas}, luas selimut = {luas_selimut}")

            kon.send("Parameter is ready, ketik 'hitung' untuk mulai.".encode())

        except ValueError:
            # Jika data tidak dapat diproses (misalnya, bukan angka atau tidak dipisah dengan koma)
            kon.send("Format input tidak valid. Harap kirim data dalam format 'luas_alas,luas_selimut'.".encode())
            continue

        # Menunggu perintah lebih lanjut dari klien
        data = kon.recv(1024).decode()
        
        if data.lower() == 'hitung':  # Jika klien mengirim 'hitung'
            # Menghitung luas prisma segitiga
            luas = 2 * luas_alas + luas_selimut
            response = f"Luas dari prisma segitiga adalah {luas}"
            kon.send(response.encode())
        else:
            # Jika perintah tidak dikenali
            kon.send("Perintah tidak dikenali. Ketik 'hitung' untuk menghitung atau 'keluar' untuk keluar.".encode())

    except ConnectionAbortedError:
        print("Koneksi terputus secara tiba-tiba oleh klien.")
        break
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        break

# Menutup koneksi setelah selesai
kon.close()
s.close()
