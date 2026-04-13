Sistem Pendukung Keputusan Klasifikasi Kualitas Tanah Berbasis Logika Fuzzy Sugeno
📌 Deskripsi Project

Project ini merupakan implementasi Sistem Pendukung Keputusan (SPK) berbasis Logika Fuzzy Metode Sugeno untuk mengklasifikasikan kualitas tanah sawah. Sistem ini dibangun menggunakan Python dan framework Django untuk mempermudah analisis serta visualisasi hasil klasifikasi secara berbasis web.

Sistem mampu mengolah data parameter kimia tanah dan menghasilkan output berupa kategori kualitas tanah:

Tidak Sehat
Kurang Sehat
Sehat
🎯 Tujuan
Mengembangkan model Fuzzy Inference System (FIS) untuk klasifikasi kualitas tanah
Membangun sistem berbasis web untuk membantu pengambilan keputusan
Memberikan hasil klasifikasi yang lebih objektif, cepat, dan akurat
🧠 Metode yang Digunakan

Metode utama yang digunakan adalah:

🔹 Logika Fuzzy Sugeno

Tahapan dalam sistem:

Fuzzifikasi
Mengubah data numerik menjadi derajat keanggotaan
Rule Base (IF–THEN)
Aturan berdasarkan pengetahuan agronomi
Inferensi Sugeno
Menghasilkan output numerik
Defuzzifikasi (Weighted Average)
Menghasilkan nilai akhir (crisp)
📊 Parameter Input

Sistem menggunakan parameter kimia tanah sebagai input:

pH (Keasaman tanah)
KTK (Kapasitas Tukar Kation)
C-Organik
N-Total
P-Total
K-Total
🖥️ Struktur Project
HASIL_SKRIPSI/
│
├── Hasil_Skripsi/        # Konfigurasi utama Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── tanah/                # Aplikasi utama
│   ├── models.py         # Model database
│   ├── views.py          # Logika proses
│   ├── fuzzy.py          # Implementasi Fuzzy Sugeno
│   ├── urls.py           # Routing aplikasi
│   ├── templates/        # Tampilan web
│   └── ...
│
├── db.sqlite3            # Database
├── manage.py             # Entry point Django
└── README.md
⚙️ Cara Menjalankan Project
1. Clone Repository
git clone https://github.com/username/nama-repo.git
cd nama-repo
2. Install Dependency
pip install -r requirements.txt
3. Jalankan Server
python manage.py runserver
4. Akses di Browser
http://127.0.0.1:8000/
📈 Cara Kerja Sistem
User memasukkan data parameter tanah
Sistem melakukan proses Fuzzy:
Fuzzifikasi
Inferensi
Defuzzifikasi
Sistem menampilkan:
Nilai hasil (crisp)
Kategori kualitas tanah
Hasil digunakan sebagai dasar pengambilan keputusan
🧪 Data Penelitian
Jumlah data: 33 sampel
Lokasi:
Lembah Palu (5 desa)
DAS Unda Bali (16 desa)
📊 Output Sistem

Output berupa:

Nilai numerik (hasil Sugeno)
Kategori:
0 → Tidak Sehat
1 → Kurang Sehat
2 → Sehat
🚀 Kelebihan Sistem
Mengatasi ketidakpastian data
Lebih fleksibel dibanding metode konvensional
Berbasis web (mudah digunakan)
Hasil lebih objektif dan konsisten
👩‍🎓 Penulis

Asri Angel Paskah Towimba
NIM: G20122036
Program Studi Matematika
FMIPA Universitas Tadulako

📚 Referensi

Beberapa referensi utama:

Rahmawati R. Lantoi et al. (2016)
Febriana et al. (2024)
Padmawati et al. (2017)
Purba et al. (2021)