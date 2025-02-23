# Tic Tac Toe Game

Tic Tac Toe adalah permainan klasik dua pemain yang dimainkan di papan 3x3. Proyek ini adalah implementasi Tic Tac Toe menggunakan Python dengan library `tkinter` untuk antarmuka grafis. Permainan ini mendukung dua mode: **Human vs Human** dan **Human vs AI**.

## Fitur
- **Mode Human vs Human**: Dua pemain manusia dapat bermain bergantian.
- **Mode Human vs AI**: Pemain dapat bermain melawan AI yang menggunakan langkah acak.
- **Skor**: Menampilkan skor pemain X dan O.
- **Highlight Pemenang**: Baris, kolom, atau diagonal pemenang akan disorot.
- **Restart Game**: Tombol untuk memulai permainan baru.
- **Antarmuka User-Friendly**: Desain sederhana dan mudah digunakan.

## Cara Menjalankan
1. Pastikan Python sudah terinstall di sistem Anda.
2. Clone repositori ini atau download file `TicTacToe.py`.
3. Buka terminal atau command prompt, lalu navigasikan ke direktori tempat file berada.
4. Jalankan program dengan perintah:
   ```bash
   python TicTacToe.py

## Cara Bermain

### **Pilih Mode:**
- Pilih **Mode** di pojok kiri atas.
- Pilih **Mode AI** untuk bermain melawan komputer atau **Mode Human** untuk bermain melawan teman.

### **Mode AI:**
- Setelah memilih **Mode AI**, Anda akan diminta memilih apakah ingin bermain sebagai **X atau O**.
- Pemain dan AI akan bergantian mengambil giliran hingga ada pemenang atau permainan berakhir seri.

### **Mode Human:**
- Pemain **X** akan bergerak pertama, diikuti oleh pemain **O**.
- Pemain bergantian memilih kotak yang tersedia hingga ada pemenang atau permainan berakhir seri.

## **Cara Memainkan**

### **Klik Kotak:**
- Klik kotak kosong untuk menandainya dengan simbol pemain saat ini (**X atau O**).
- Pemain tidak bisa memilih kotak yang sudah diisi.

### **Menentukan Pemenang:**
- Pemain yang pertama kali mendapatkan tiga simbol berturut-turut dalam satu **baris, kolom, atau diagonal** akan menang.
- Jika semua kotak sudah terisi dan tidak ada yang menang, permainan dinyatakan **seri**.

### **Restart Permainan:**
- Setelah permainan selesai, klik tombol **Restart** untuk memulai permainan baru.
