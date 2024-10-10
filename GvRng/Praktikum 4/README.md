**Modul 4 | Perulangan dan pengambilan keputusan**
##
**Perulangan**

  - Jika kalian ingin mengulangi perintah yang sama, di GvRng ada fitur perulangan menggunakan 'do'.
'do' memiliki arti lakukan. Yang berati, kalian ingin melakukan perintah itu berapa kali.
  - Penggunaan perintah do, sama seperti pembuatan fungsi. Yaitu, perintah di dalam 'do' nya harus menjorok ke dalam
  - Misal, ingin memerintah robot untuk jalan 3 kali
  - Awal sebelum mengenal 'do':
  ```
  move move move
  ```
  - atau:
  ```  
    move
    move
    move
  ```
  - setelah mengenal 'do':
  ```
    do 3:
      move
  ```
  Kode di atas bisa dibaca seperti ini,
  
  Do 3: yang berarti lakukan 3x, apa yang dilakukan 3x?, move(maju).
  
> Perulangan sangat simple, bukan?

##

**Pengambilan keputusan**
- **if (Jika)**
  - Ada 18 kondisi yang bisa dibuat untuk pengambilan keputusan. Analoginya begini, jika ada kondisi tertentu, maka melakukan sesuatu. Sesuatu yang dapat dilakukan bisa berupa perulangan, pemanggilan fungsi, perintah inti.
  - Penggunaan perintah pengambilan keputusan, sama seperti pembuatan fungsi. Yaitu, perintah di dalam 'pengambilan keputusan' harus menjorok ke dalam

| **Kondisi**  | **Makna** |
| ------------- | ------------- |
| `front_is_clear`  | Lokasi di depan robot tidak ada penghalang (_wall_)  |
| `front_is_blocked`  | Lokasi di depan robot ada penghalang (_wall_)  |
| `left_is_clear`  | Lokasi di samping kiri robot tidak ada penghalang (_wall_)  |
| `left_is_blocked`  | Lokasi di samping kiri robot ada penghalang (_wall_)  |
| `right_is_clear`  | Lokasi di samping kanan robot tidak ada penghalang (_wall_)  |
| `right_is_blocekd`  | Lokasi di samping kanan robot tidak ada penghalang (_wall_)  |
| `next_to_a_beeper`  | Robot berada pada posisi yang sama dengan beeper (pada koordinat yang sama)  |
| `not_next_to_a_beeper`  | Robot tidak berada pada posisi dekat beeper  |
| `any_beepers_in_beeper_bag`  | Kantong beeper berisi  |
| `no_beepers_in_beeper_bag`  | Kantong beeper kosong  |
| `facing_north`  | Menghadap utara  |
| `not_facing_north`  | Tidak menghadap utara  |
| `facing_south`  | Menghadap selatan  |
| `not_facing_south`  | Tidak menghadap selatan  |
| `facing_east`  | Menghadap timur  |
| `not_facing_east`  | Tidak menghadap timur  |
| `facing_west`  | Menghadap barat  |
| `not_facing_west`  | Tidak menghadap barat  |

#

  - Contoh analogi:
  ```
  jika di depan ada tembok:
    hadap kiri
    maju
  ```
  - Contoh instruksi:
  ```
  if front_is_blocked:
    turnleft
    move
  ```
  - Cara membaca perintah/instruksi di atas adalah. **Jika di depan robot ada penghalang, maka, hadap kiri lalu maju satu langkah**.
  - Robot harus memerika kondisi tersebut dahulu, jika kondisi tersebut terpenuhi, maka robot tersebut akan melakukan perintah di dalam nya.

  - Atau bisa juga seperti ini, variasi menggunakan perintah 'do':
  ```
  if front_is_blocked:
    do 3:
      turnleft
    move
  ```
  - Cara memmbaca perintah/instruksi di atas adalah. **jika di depan robot ada peghalang**, lakukan 3x hadap kiri (hadap kanan), lalu maju satu langkah

#

**Lebih banyak keputusan**
- **if - else**
  - Digunakan untuk membuat lebih banyak keputusan berdasarkan suatu kondisi tertentu.
  - Menggunakan gabungan perintah if-else

- Contoh analoginya begini:
  ```
  jika di depan ada penghalang:
    hadap kiri
    maju
  jika tidak ada penghalang:
    maju
  ```
- Contoh instruksinya begini:
  ```
  if front_is_blocked:
    turnleft
    move
  else:
    move
  ```
- Cara membaca perintah / instruksi di atas adalah. **Jika di depan robot ada penghalang (_wall_)**, lakukan hadap kiri lalu maju satu langkah. **jika tidak ada penghalang di depan robot**, lakukan maju satu langkah.
  
- Di dalam instruksi tersebut juga bisa diisi dengan perintah 'do' dan juga pemanggilan fungsi.
- Contoh instruksinya begini:
  ```
  define hadapkanan:
    do 3:
      turnleft
  
  if front_is_clear:
    do 2:
      move
  else:
    hadapkanan
    do 2:
      move
  ```
- Cara membaca kode perintah/instruksi di atas adalah.
    - Membuat fungsi hadapkanan, dengan cara melakukan 3x hadap kiri. Jika di depan robot tidak ada penghalang, lakukan 2x maju satu langka. Jika di depan robot ada penghalang, lakukan hadapkanan(fungsi hadapkanan dipanggil) lalu maju satu langkah.
    - Kode ini memeriksa apakah ada penghalang di depan robot. Jika tidak ada penghalang, robot akan bergerak maju dua langkah. Jika ada penghalang, robot akan berputar ke kanan dan kemudian bergerak maju dua langkah.
 
#

**Lebih banyak kondisi dan lebih banyak keputusan**
- **if - elif - else** 
  - Digunakan untuk pengecekan lebih dari 1 kondisi.
