# Algorithm


Berikut adalah daftar soal yang telah diselesaikan dalam repositori ini:

### Soal 1: Pasangan Subarray dengan Jumlah > K (count_pairs.py)
**Deskripsi**: Menghitung jumlah pasangan indeks (i, j) dengan i < j dalam sebuah array di mana arr[i] + arr[j] lebih besar dari nilai k. Solusi ini dioptimalkan untuk efisiensi dengan kompleksitas waktu O(n
logn) menggunakan metode two-pointer.

### Soal 2: Pembalikan Mutasi DNA (reverse_dna.py)
**Deskripsi**: Menentukan string DNA asli setelah mengalami proses mutasi (balik urutan lalu ganti karakter komplemen) sebanyak k kali. Solusi ini didasarkan pada analisis pola siklus, di mana proses mutasi membatalkan dirinya sendiri setiap dua kali penerapan, sehingga hasilnya hanya bergantung pada apakah k ganjil atau genap.


---
## Cara Menjalankan Kode
Pastikan Anda telah menginstal Python 3 di sistem Anda.

### 1. Clone Repositori
Pertama, clone repositori ini ke mesin lokal Anda:
```
git clone https://github.com/cinnamorollofficials/fullstack-test-algorithm.git
cd fullstack-test-algorithm
```

### 2. Menjalankan Skrip Individual
Setiap soal memiliki file Python-nya sendiri. Jalankan file yang sesuai dari terminal dan berikan input sesuai format yang ditentukan.

#### Soal 1: Pasangan Subarray (count_pairs.py)
Skrip ini mengharapkan input dalam dua baris:

- Baris 1: Dua angka, n (panjang array) dan k, dipisahkan spasi.

- Baris 2: n angka elemen array, dipisahkan spasi.

Contoh Eksekusi:
```
python count_pairs.py
```

Setelah menjalankan perintah di atas, masukkan input berikut di terminal:

```
5 7
1 2 4 6 8
```

Program akan menghasilkan output:
```
6
```

#### Soal 2: Pembalikan Mutasi DNA (reverse_dna.py)
Skrip ini mengharapkan input dalam dua baris:

- Baris 1: Satu angka, k (jumlah mutasi).

- Baris 2: String DNA.

Contoh Eksekusi:
```
python reverse_dna.py
```

Setelah menjalankan perintah di atas, masukkan input berikut di terminal:
```
1
ACGT
```
Program akan menghasilkan output:
```
ACGT
```