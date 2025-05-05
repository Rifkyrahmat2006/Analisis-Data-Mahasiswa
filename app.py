from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Data dari data.csv
data = [
    {"Nama Lengkap": "Ahmad Fauzi", "IPK": 3.87, "Mata Kuliah Tidak Lulus": 5, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 13, "Status Kelulusan": 1, "IPS Rata-rata": 3.2992307692307694, "IPS Semester Akhir": 2.66, "IPS Tren": 0.5700000000000003, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Budi Santoso", "IPK": 3.65, "Mata Kuliah Tidak Lulus": 5, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 12, "Status Kelulusan": 0, "IPS Rata-rata": 3.0691666666666664, "IPS Semester Akhir": 3.56, "IPS Tren": 1.21, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Citra Dewi Lestari", "IPK": 3.57, "Mata Kuliah Tidak Lulus": 2, "Jumlah Cuti Akademik": 2, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 11, "Status Kelulusan": 1, "IPS Rata-rata": 2.955454545454545, "IPS Semester Akhir": 2.89, "IPS Tren": -0.5899999999999999, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Dedi Prasetyo", "IPK": 3.96, "Mata Kuliah Tidak Lulus": 0, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 12, "Status Kelulusan": 0, "IPS Rata-rata": 3.2308333333333334, "IPS Semester Akhir": 2.63, "IPS Tren": -1.3400000000000003, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Eka Nurhayati", "IPK": 2.27, "Mata Kuliah Tidak Lulus": 0, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 9, "Status Kelulusan": 1, "IPS Rata-rata": 3.066666666666667, "IPS Semester Akhir": 2.22, "IPS Tren": -1.1399999999999997, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Fajar Setiawan", "IPK": 2.31, "Mata Kuliah Tidak Lulus": 1, "Jumlah Cuti Akademik": 2, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 9, "Status Kelulusan": 0, "IPS Rata-rata": 2.9155555555555557, "IPS Semester Akhir": 3.35, "IPS Tren": 0.54, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Gita Puspita Sari", "IPK": 2.07, "Mata Kuliah Tidak Lulus": 2, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 8, "Status Kelulusan": 1, "IPS Rata-rata": 3.03125, "IPS Semester Akhir": 3.36, "IPS Tren": -0.22999999999999998, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Hendra Kurniawan", "IPK": 3.41, "Mata Kuliah Tidak Lulus": 1, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 8, "Status Kelulusan": 1, "IPS Rata-rata": 2.63, "IPS Semester Akhir": 2.08, "IPS Tren": -0.5, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Indah Permata Sari", "IPK": 2.59, "Mata Kuliah Tidak Lulus": 0, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 11, "Status Kelulusan": 0, "IPS Rata-rata": 2.8663636363636362, "IPS Semester Akhir": 2.6, "IPS Tren": -0.6099999999999999, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Joko Susilo", "IPK": 3.73, "Mata Kuliah Tidak Lulus": 0, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 10, "Status Kelulusan": 1, "IPS Rata-rata": 2.732, "IPS Semester Akhir": 2.16, "IPS Tren": -1.0099999999999998, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Kartika Wijaya", "IPK": 3.65, "Mata Kuliah Tidak Lulus": 1, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 10, "Status Kelulusan": 0, "IPS Rata-rata": 3.081, "IPS Semester Akhir": 2.59, "IPS Tren": -0.71, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Lina Marlina", "IPK": 2.03, "Mata Kuliah Tidak Lulus": 4, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 8, "Status Kelulusan": 0, "IPS Rata-rata": 2.7762499999999997, "IPS Semester Akhir": 2.09, "IPS Tren": -1.37, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Muhammad Rizki", "IPK": 3.51, "Mata Kuliah Tidak Lulus": 2, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 7, "Status Kelulusan": 0, "IPS Rata-rata": 3.097142857142857, "IPS Semester Akhir": 3.65, "IPS Tren": 1.13, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Nia Anggraeni", "IPK": 2.4, "Mata Kuliah Tidak Lulus": 1, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 12, "Status Kelulusan": 0, "IPS Rata-rata": 3.18, "IPS Semester Akhir": 2.78, "IPS Tren": -0.4500000000000002, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Oki Pratama", "IPK": 2.87, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 2, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 7, "Status Kelulusan": 1, "IPS Rata-rata": 3.028571428571429, "IPS Semester Akhir": 2.12, "IPS Tren": -1.62, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Putri Ayu Lestari", "IPK": 3.28, "Mata Kuliah Tidak Lulus": 2, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 10, "Status Kelulusan": 0, "IPS Rata-rata": 2.947, "IPS Semester Akhir": 2.17, "IPS Tren": -1.44, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Rudi Hermawan", "IPK": 2.79, "Mata Kuliah Tidak Lulus": 1, "Jumlah Cuti Akademik": 2, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 14, "Status Kelulusan": 1, "IPS Rata-rata": 3.0964285714285715, "IPS Semester Akhir": 3.4, "IPS Tren": 0.14000000000000012, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Siti Rahmawati", "IPK": 2.88, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 12, "Status Kelulusan": 0, "IPS Rata-rata": 3.141666666666667, "IPS Semester Akhir": 3.67, "IPS Tren": -0.1499999999999999, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Teguh Wibowo", "IPK": 2.89, "Mata Kuliah Tidak Lulus": 4, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 14, "Status Kelulusan": 0, "IPS Rata-rata": 3.0707142857142857, "IPS Semester Akhir": 3.18, "IPS Tren": -0.7799999999999998, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Umi Kulsum", "IPK": 2.1, "Mata Kuliah Tidak Lulus": 1, "Jumlah Cuti Akademik": 2, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 12, "Status Kelulusan": 0, "IPS Rata-rata": 2.790833333333333, "IPS Semester Akhir": 3.23, "IPS Tren": 1.2200000000000002, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Vera Agustina", "IPK": 3.98, "Mata Kuliah Tidak Lulus": 5, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 8, "Status Kelulusan": 1, "IPS Rata-rata": 3.2800000000000002, "IPS Semester Akhir": 3.72, "IPS Tren": -0.03999999999999959, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Wahyu Aditya", "IPK": 3.47, "Mata Kuliah Tidak Lulus": 2, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 11, "Status Kelulusan": 0, "IPS Rata-rata": 3.235454545454546, "IPS Semester Akhir": 3.06, "IPS Tren": 0.1200000000000001, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Yuni Astuti", "IPK": 3.51, "Mata Kuliah Tidak Lulus": 2, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 14, "Status Kelulusan": 0, "IPS Rata-rata": 2.9014285714285717, "IPS Semester Akhir": 2.8, "IPS Tren": -0.7000000000000002, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Zainal Arifin", "IPK": 3.35, "Mata Kuliah Tidak Lulus": 0, "Jumlah Cuti Akademik": 2, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 14, "Status Kelulusan": 0, "IPS Rata-rata": 3.1142857142857148, "IPS Semester Akhir": 2.34, "IPS Tren": -0.9100000000000001, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Ani Ratnasari", "IPK": 2.09, "Mata Kuliah Tidak Lulus": 5, "Jumlah Cuti Akademik": 2, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 12, "Status Kelulusan": 1, "IPS Rata-rata": 3.0041666666666664, "IPS Semester Akhir": 3.11, "IPS Tren": -0.20999999999999996, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Bambang Sudrajat", "IPK": 2.12, "Mata Kuliah Tidak Lulus": 4, "Jumlah Cuti Akademik": 2, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 11, "Status Kelulusan": 0, "IPS Rata-rata": 2.871818181818182, "IPS Semester Akhir": 3.92, "IPS Tren": 1.69, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Cinta Maya Sari", "IPK": 3.66, "Mata Kuliah Tidak Lulus": 2, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 11, "Status Kelulusan": 0, "IPS Rata-rata": 3.0645454545454545, "IPS Semester Akhir": 2.12, "IPS Tren": -0.48, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Dwi Novianto", "IPK": 3.22, "Mata Kuliah Tidak Lulus": 5, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 8, "Status Kelulusan": 0, "IPS Rata-rata": 3.165, "IPS Semester Akhir": 2.6, "IPS Tren": -1.0699999999999998, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Erwin Saputra", "IPK": 3.05, "Mata Kuliah Tidak Lulus": 4, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 13, "Status Kelulusan": 0, "IPS Rata-rata": 3.1853846153846157, "IPS Semester Akhir": 2.35, "IPS Tren": -0.3599999999999999, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Fitriani Handayani", "IPK": 3.61, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 11, "Status Kelulusan": 0, "IPS Rata-rata": 2.8918181818181816, "IPS Semester Akhir": 3.66, "IPS Tren": 1.3600000000000003, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Gilang Ramadhan", "IPK": 2.41, "Mata Kuliah Tidak Lulus": 1, "Jumlah Cuti Akademik": 2, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 10, "Status Kelulusan": 0, "IPS Rata-rata": 2.9010000000000007, "IPS Semester Akhir": 3.01, "IPS Tren": -0.1200000000000001, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Hesti Purwaningsih", "IPK": 3.03, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 10, "Status Kelulusan": 0, "IPS Rata-rata": 3.1730000000000005, "IPS Semester Akhir": 2.73, "IPS Tren": -1.12, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Irfan Maulana", "IPK": 3.78, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 9, "Status Kelulusan": 1, "IPS Rata-rata": 2.8966666666666665, "IPS Semester Akhir": 3.23, "IPS Tren": -0.5699999999999998, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Jihan Fadilah", "IPK": 3.72, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 13, "Status Kelulusan": 1, "IPS Rata-rata": 3.060769230769231, "IPS Semester Akhir": 3.02, "IPS Tren": -0.16999999999999993, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Kiki Amelia", "IPK": 2.14, "Mata Kuliah Tidak Lulus": 2, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 9, "Status Kelulusan": 0, "IPS Rata-rata": 3.0733333333333333, "IPS Semester Akhir": 2.88, "IPS Tren": -0.6299999999999999, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Luki Setiawan", "IPK": 3.38, "Mata Kuliah Tidak Lulus": 1, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 14, "Status Kelulusan": 0, "IPS Rata-rata": 2.9778571428571428, "IPS Semester Akhir": 2.59, "IPS Tren": -1.1100000000000003, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Mila Karmila", "IPK": 3.83, "Mata Kuliah Tidak Lulus": 5, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 11, "Status Kelulusan": 1, "IPS Rata-rata": 2.9818181818181824, "IPS Semester Akhir": 3.68, "IPS Tren": 1.37, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Nanda Putra", "IPK": 2.7, "Mata Kuliah Tidak Lulus": 4, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 14, "Status Kelulusan": 1, "IPS Rata-rata": 2.9857142857142853, "IPS Semester Akhir": 2.88, "IPS Tren": -0.75, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Olivia Febriani", "IPK": 3.05, "Mata Kuliah Tidak Lulus": 4, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 13, "Status Kelulusan": 0, "IPS Rata-rata": 3.1853846153846157, "IPS Semester Akhir": 2.35, "IPS Tren": -0.3599999999999999, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Pandu Wijaya", "IPK": 3.61, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 11, "Status Kelulusan": 0, "IPS Rata-rata": 2.8918181818181816, "IPS Semester Akhir": 3.66, "IPS Tren": 1.3600000000000003, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Qonita Rahma", "IPK": 2.41, "Mata Kuliah Tidak Lulus": 1, "Jumlah Cuti Akademik": 2, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 10, "Status Kelulusan": 0, "IPS Rata-rata": 2.9010000000000007, "IPS Semester Akhir": 3.01, "IPS Tren": -0.1200000000000001, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Rizky Pratama", "IPK": 3.03, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 10, "Status Kelulusan": 0, "IPS Rata-rata": 3.1730000000000005, "IPS Semester Akhir": 2.73, "IPS Tren": -1.12, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Siska Amelia", "IPK": 3.78, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 9, "Status Kelulusan": 1, "IPS Rata-rata": 2.8966666666666665, "IPS Semester Akhir": 3.23, "IPS Tren": -0.5699999999999998, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Taufik Hidayat", "IPK": 3.72, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 13, "Status Kelulusan": 1, "IPS Rata-rata": 3.060769230769231, "IPS Semester Akhir": 3.02, "IPS Tren": -0.16999999999999993, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Aisyah Rahmawati", "IPK": 3.05, "Mata Kuliah Tidak Lulus": 4, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Tidak", "Jumlah Semester": 13, "Status Kelulusan": 0, "IPS Rata-rata": 3.1853846153846157, "IPS Semester Akhir": 2.35, "IPS Tren": -0.3599999999999999, "Kategori Kehadiran": "Tinggi"},
    {"Nama Lengkap": "Bagus Prabowo", "IPK": 3.61, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 1, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 11, "Status Kelulusan": 0, "IPS Rata-rata": 2.8918181818181816, "IPS Semester Akhir": 3.66, "IPS Tren": 1.3600000000000003, "Kategori Kehadiran": "Rendah"},
    {"Nama Lengkap": "Cindy Nurhaliza", "IPK": 2.41, "Mata Kuliah Tidak Lulus": 1, "Jumlah Cuti Akademik": 2, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 10, "Status Kelulusan": 0, "IPS Rata-rata": 2.9010000000000007, "IPS Semester Akhir": 3.01, "IPS Tren": -0.1200000000000001, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Doni Irawan", "IPK": 3.03, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 10, "Status Kelulusan": 0, "IPS Rata-rata": 3.1730000000000005, "IPS Semester Akhir": 2.73, "IPS Tren": -1.12, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Elsa Fitriani", "IPK": 3.78, "Mata Kuliah Tidak Lulus": 3, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 9, "Status Kelulusan": 1, "IPS Rata-rata": 2.8966666666666665, "IPS Semester Akhir": 3.23, "IPS Tren": -0.5699999999999998, "Kategori Kehadiran": "Sedang"},
    {"Nama Lengkap": "Lia Damayanti", "IPK": 2.7, "Mata Kuliah Tidak Lulus": 4, "Jumlah Cuti Akademik": 0, "Pekerjaan Sambil Kuliah": "Ya", "Jumlah Semester": 14, "Status Kelulusan": 1, "IPS Rata-rata": 2.9857142857142853, "IPS Semester Akhir": 2.88, "IPS Tren": -0.75, "Kategori Kehadiran": "Rendah"}
]

def calculate_mean(data, field):
    total = sum(item[field] for item in data)
    return total / len(data)

def calculate_median(data, field):
    sorted_data = sorted([item[field] for item in data])
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        return sorted_data[n//2]

def calculate_mode(data, field):
    values = [item[field] for item in data]
    frequency = {}
    for value in values:
        frequency[value] = frequency.get(value, 0) + 1
    max_freq = max(frequency.values())
    return [k for k, v in frequency.items() if v == max_freq]

def calculate_range(data, field):
    values = [item[field] for item in data]
    return max(values) - min(values)

def calculate_variance(data, field):
    mean = calculate_mean(data, field)
    squared_diff = sum((item[field] - mean) ** 2 for item in data)
    return squared_diff / len(data)

def calculate_std_dev(data, field):
    variance = calculate_variance(data, field)
    # Implementasi manual untuk square root
    if variance < 0:
        return 0
    x = variance
    for _ in range(10):  # 10 iterasi cukup untuk presisi yang baik
        x = (x + variance/x) / 2
    return x

def calculate_quartiles(data, field):
    sorted_data = sorted([item[field] for item in data])
    n = len(sorted_data)
    
    def find_median(arr):
        n = len(arr)
        if n % 2 == 0:
            return (arr[n//2 - 1] + arr[n//2]) / 2
        else:
            return arr[n//2]
    
    q2 = find_median(sorted_data)
    
    if n % 2 == 0:
        lower_half = sorted_data[:n//2]
        upper_half = sorted_data[n//2:]
    else:
        lower_half = sorted_data[:n//2]
        upper_half = sorted_data[n//2 + 1:]
    
    q1 = find_median(lower_half)
    q3 = find_median(upper_half)
    
    return {"q1": q1, "q2": q2, "q3": q3}

# Fungsi untuk mendapatkan data dengan pagination
def get_paginated_data(page=1, per_page=10):
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    
    paginated_data = []
    for item in data[start_idx:end_idx]:
        formatted_item = {
            "Nama Lengkap": item["Nama Lengkap"],
            "IPK": item["IPK"],
            "IPS_Rata_rata": item["IPS Rata-rata"],
            "IPS_Semester_Akhir": item["IPS Semester Akhir"],
            "Mata_Kuliah_Tidak_Lulus": item["Mata Kuliah Tidak Lulus"],
            "Jumlah_Cuti_Akademik": item["Jumlah Cuti Akademik"],
            "Jumlah_Semester": item["Jumlah Semester"],
            "Status_Kelulusan": item["Status Kelulusan"]
        }
        paginated_data.append(formatted_item)
    
    return paginated_data

# Fungsi untuk menghitung total halaman
def get_total_pages(per_page=10):
    return (len(data) + per_page - 1) // per_page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    search_query = request.args.get('search', '').lower()
    
    # Jika ada query pencarian, filter data terlebih dahulu
    if search_query:
        filtered_data = []
        for item in data:
            # Cari di nama dan nilai
            if search_query in item["Nama Lengkap"].lower() or \
               str(item["IPK"]).lower().startswith(search_query) or \
               str(item["IPS Rata-rata"]).lower().startswith(search_query) or \
               str(item["IPS Semester Akhir"]).lower().startswith(search_query) or \
               str(item["Mata Kuliah Tidak Lulus"]).lower().startswith(search_query) or \
               str(item["Jumlah Cuti Akademik"]).lower().startswith(search_query) or \
               str(item["Jumlah Semester"]).lower().startswith(search_query) or \
               str(item["Status Kelulusan"]).lower().startswith(search_query):
                filtered_data.append(item)
        
        # Pagination untuk data yang sudah difilter
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        
        paginated_filtered_data = []
        for item in filtered_data[start_idx:end_idx]:
            formatted_item = {
                "Nama Lengkap": item["Nama Lengkap"],
                "IPK": item["IPK"],
                "IPS_Rata_rata": item["IPS Rata-rata"],
                "IPS_Semester_Akhir": item["IPS Semester Akhir"],
                "Mata_Kuliah_Tidak_Lulus": item["Mata Kuliah Tidak Lulus"],
                "Jumlah_Cuti_Akademik": item["Jumlah Cuti Akademik"],
                "Jumlah_Semester": item["Jumlah Semester"],
                "Status_Kelulusan": item["Status Kelulusan"]
            }
            paginated_filtered_data.append(formatted_item)
        
        total_filtered_pages = (len(filtered_data) + per_page - 1) // per_page
        
        return jsonify({
            'data': paginated_filtered_data,
            'total_pages': total_filtered_pages,
            'current_page': page,
            'total_items': len(filtered_data)
        })
    else:
        # Jika tidak ada query pencarian, gunakan pagination normal
        paginated_data = get_paginated_data(page, per_page)
        total_pages = get_total_pages(per_page)
        
        return jsonify({
            'data': paginated_data,
            'total_pages': total_pages,
            'current_page': page,
            'total_items': len(data)
        })

@app.route('/api/stats')
def get_stats():
    stats = {
        "IPK": {
            "mean": calculate_mean(data, "IPK"),
            "median": calculate_median(data, "IPK"),
            "mode": calculate_mode(data, "IPK"),
            "range": calculate_range(data, "IPK"),
            "variance": calculate_variance(data, "IPK"),
            "std_dev": calculate_std_dev(data, "IPK"),
            "quartiles": calculate_quartiles(data, "IPK"),
            "all_values": [item["IPK"] for item in data]
        },
        "IPS_Rata_rata": {
            "mean": calculate_mean(data, "IPS Rata-rata"),
            "median": calculate_median(data, "IPS Rata-rata"),
            "mode": calculate_mode(data, "IPS Rata-rata"),
            "range": calculate_range(data, "IPS Rata-rata"),
            "variance": calculate_variance(data, "IPS Rata-rata"),
            "std_dev": calculate_std_dev(data, "IPS Rata-rata"),
            "quartiles": calculate_quartiles(data, "IPS Rata-rata"),
            "all_values": [item["IPS Rata-rata"] for item in data]
        },
        "IPS_Semester_Akhir": {
            "mean": calculate_mean(data, "IPS Semester Akhir"),
            "median": calculate_median(data, "IPS Semester Akhir"),
            "mode": calculate_mode(data, "IPS Semester Akhir"),
            "range": calculate_range(data, "IPS Semester Akhir"),
            "variance": calculate_variance(data, "IPS Semester Akhir"),
            "std_dev": calculate_std_dev(data, "IPS Semester Akhir"),
            "quartiles": calculate_quartiles(data, "IPS Semester Akhir"),
            "all_values": [item["IPS Semester Akhir"] for item in data]
        },
        "Mata_Kuliah_Tidak_Lulus": {
            "mean": calculate_mean(data, "Mata Kuliah Tidak Lulus"),
            "median": calculate_median(data, "Mata Kuliah Tidak Lulus"),
            "mode": calculate_mode(data, "Mata Kuliah Tidak Lulus"),
            "range": calculate_range(data, "Mata Kuliah Tidak Lulus"),
            "variance": calculate_variance(data, "Mata Kuliah Tidak Lulus"),
            "std_dev": calculate_std_dev(data, "Mata Kuliah Tidak Lulus"),
            "quartiles": calculate_quartiles(data, "Mata Kuliah Tidak Lulus"),
            "all_values": [item["Mata Kuliah Tidak Lulus"] for item in data]
        },
        "Jumlah_Cuti_Akademik": {
            "mean": calculate_mean(data, "Jumlah Cuti Akademik"),
            "median": calculate_median(data, "Jumlah Cuti Akademik"),
            "mode": calculate_mode(data, "Jumlah Cuti Akademik"),
            "range": calculate_range(data, "Jumlah Cuti Akademik"),
            "variance": calculate_variance(data, "Jumlah Cuti Akademik"),
            "std_dev": calculate_std_dev(data, "Jumlah Cuti Akademik"),
            "quartiles": calculate_quartiles(data, "Jumlah Cuti Akademik"),
            "all_values": [item["Jumlah Cuti Akademik"] for item in data]
        },
        "Jumlah_Semester": {
            "mean": calculate_mean(data, "Jumlah Semester"),
            "median": calculate_median(data, "Jumlah Semester"),
            "mode": calculate_mode(data, "Jumlah Semester"),
            "range": calculate_range(data, "Jumlah Semester"),
            "variance": calculate_variance(data, "Jumlah Semester"),
            "std_dev": calculate_std_dev(data, "Jumlah Semester"),
            "quartiles": calculate_quartiles(data, "Jumlah Semester"),
            "all_values": [item["Jumlah Semester"] for item in data]
        }
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)