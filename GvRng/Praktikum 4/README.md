**Modul 4 | Perulangan dan pengambilan keputusan**
##
**Perulangan**

  - Jika kalian ingin mengulangi perintah yang sama, di GvRng ada fitur perulangan menggunakan 'do'.
'do' memiliki arti lakukan. yang berati, kalian ingin melakukan perintah itu berapa kali.
  - misal, ingin memerintah robot untuk jalan 3 kali
  - awal sebelum mengenal 'do':
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
> perulangan sangat simple, bukan?
##
- **Pengambilan keputusan**
  - ada 18 kondisi yang bisa dibuat untuk pengambilan keputusan. analoginya begini, jika ada kondisi tertentu, maka melakukan sesuatu. sesuatu yang dapat dilakukan bisa berupa perulangan, pemanggilan fungsi, perintah inti. 

| **Kondisi**  | **Makna** |
| ------------- | ------------- |
| `front_is_clear`  | lokasi di depan robot tidak ada penghalang (_wall_)  |
| `front_is_blocked`  | lokasi di depan robot ada penghalang (_wall_)  |
| `left_is_clear`  | lokasi di samping kiri robot tidak ada penghalang (_wall_)  |
| `left_is_blocked`  | lokasi di samping kiri robot ada penghalang (_wall_)  |
| `right_is_clear`  | lokasi di samping kanan robot tidak ada penghalang (_wall_)  |
| `right_is_blocekd`  | lokasi di samping kanan robot tidak ada penghalang (_wall_)  |
| `next_to_a_beeper`  | robot berada pada posisi yang sama dengan beeper (pada koordinat yang sama)  |
| `not_next_to_a_beeper`  | robot tidak berada pada posisi dekat beeper  |
| `any_beepers_in_beeper_bag`  | kantong beeper berisi  |
| `no_beepers_in_beeper_bag`  | kantong beeper kosong  |
| `facing_north`  | menghadap utara  |
| `not_facing_north`  | tidak menghadap utara  |
| `facing_south`  | menghadap selatan  |
| `not_facing_south`  | tidak menghadap selatan  |
| `facing_east`  | menghadap timur  |
| `not_facing_east`  | tidak menghadap timur  |
| `facing_west`  | menghadap barat  |
| `not_facing_west`  | tidak menghadap barat  |

  - contoh analogi:
  ```
  jika di depan ada tembok:
    hadap kiri
    maju
  ```
  - contoh insturksi:
  ```
  if front_is_blocked:
    turnleft
    move
  ```
  - arti dari instruksi di atas adalah. Jika di depan ada penghalang, maka, hadap kiri lalu maju satu langkah
  - robot harus memerika kondisi tersebut dahulu, jika kondisi tersebut terpenuhi, maka robot tersebut akan melakukan perintah di dalam nya.

  - atau bisa juga seperti ini:
  ```
  if front_is_blocked:
    do 3:
      turnleft
    move
  ```
  - arti dari perintah di atas adalah. jika di depan ada peghalang, lakukan 3x hadap kiri (hadap kanan), lalu maju satu langkah
