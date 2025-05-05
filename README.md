# Aplikasi Analisis Data Mahasiswa

Aplikasi web interaktif untuk menganalisis dan memvisualisasikan data akademik mahasiswa dengan statistik deskriptif dan grafik.

## Deskripsi

Aplikasi Analisis Data Mahasiswa adalah dashboard interaktif yang menyajikan data akademik mahasiswa dan statistik deskriptif mereka. Aplikasi ini memungkinkan pengguna untuk melihat, mencari, dan menganalisis data mahasiswa berdasarkan berbagai metrik akademik seperti IPK, IPS rata-rata, IPS semester akhir, jumlah mata kuliah tidak lulus, jumlah cuti akademik, dan jumlah semester.

## Fitur

- **Tampilan Data Tabular**: Menampilkan data mahasiswa dalam format tabel yang terorganisir
- **Statistik Deskriptif**: Menghitung dan menampilkan statistik deskriptif untuk setiap metrik:
  - Mean (Rata-rata)
  - Median
  - Modus
  - Range
  - Varians
  - Standar Deviasi
  - Kuartil (Q1, Q2, Q3)
- **Visualisasi Grafik**: Menampilkan grafik batang untuk setiap statistik deskriptif
- **Fitur Pencarian**: Memungkinkan pengguna mencari data berdasarkan nama mahasiswa atau nilai
- **Pagination**: Membagi data menjadi beberapa halaman untuk navigasi yang lebih mudah

## Teknologi yang Digunakan

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Bootstrap 5
- **Visualisasi**: Chart.js

## Struktur Aplikasi

- **app.py**: File utama aplikasi Flask yang berisi logika server dan endpoint API
- **templates/index.html**: Tampilan utama aplikasi dengan HTML, CSS, dan JavaScript
- **static/js/chart-boxplot.js**: Implementasi kustom untuk grafik boxplot menggunakan Chart.js
- **static/css/style.css**: File CSS tambahan untuk styling

## Endpoint API

- **/**: Halaman utama aplikasi
- **/api/data**: Endpoint untuk mendapatkan data mahasiswa dengan pagination dan pencarian
- **/api/stats**: Endpoint untuk mendapatkan statistik deskriptif dari data

## Metrik yang Dianalisis

1. **IPK (Indeks Prestasi Kumulatif)**: Rata-rata nilai seluruh mata kuliah
2. **IPS Rata-rata (Indeks Prestasi Semester)**: Rata-rata nilai per semester
3. **IPS Semester Akhir**: Nilai pada semester terakhir
4. **Mata Kuliah Tidak Lulus**: Jumlah mata kuliah yang tidak lulus
5. **Cuti Akademik**: Jumlah semester cuti yang diambil
6. **Jumlah Semester**: Total semester yang telah ditempuh

## Cara Menggunakan

1. Jalankan aplikasi dengan perintah `python app.py`
2. Buka browser dan akses `http://localhost:5000`
3. Pilih tab metrik yang ingin dilihat (IPK, IPS Rata-rata, dll.)
4. Gunakan fitur pencarian untuk menemukan data spesifik
5. Gunakan tombol pagination untuk melihat lebih banyak data
6. Lihat statistik dan grafik di bagian bawah setiap tab

## Perhitungan Statistik

Aplikasi ini menghitung berbagai statistik deskriptif:

- **Mean**: Rata-rata aritmatika dari semua nilai
- **Median**: Nilai tengah dari data yang diurutkan
- **Modus**: Nilai yang paling sering muncul
- **Range**: Selisih antara nilai maksimum dan minimum
- **Varians**: Rata-rata dari kuadrat selisih setiap nilai dengan mean
- **Standar Deviasi**: Akar kuadrat dari varians
- **Kuartil**: Nilai yang membagi data menjadi empat bagian sama besar (Q1, Q2, Q3)

## Kontribusi

Proyek ini dibuat sebagai bagian dari tugas mata kuliah Probabilitas dan Statistika. Kontribusi dan saran perbaikan sangat diterima.

## Lisensi

Proyek ini dilisensikan di bawah lisensi MIT.
