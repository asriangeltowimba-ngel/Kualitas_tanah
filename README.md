# 🌱 Soil Quality Classification System  
### *Sistem Pendukung Keputusan Berbasis Fuzzy Sugeno*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/Django-Framework-green?logo=django">
  <img src="https://img.shields.io/badge/Fuzzy-Sugeno-orange">
  <img src="https://img.shields.io/badge/Status-Skripsi-success">
</p>

---

## 📖 Deskripsi

Project ini merupakan implementasi **Sistem Pendukung Keputusan (SPK)** berbasis **Logika Fuzzy Metode Sugeno** untuk melakukan **klasifikasi kualitas tanah sawah** secara otomatis.

Sistem dibangun menggunakan:
- 🐍 Python  
- 🌐 Django (Web Framework)  

Dengan tujuan untuk membantu:
- Petani 👨‍🌾  
- Peneliti 📊  
- Pengambil keputusan 🧠  

dalam menentukan kualitas tanah secara **cepat, objektif, dan akurat**.

---

## 🎯 Tujuan Penelitian

✔ Mengembangkan model **Fuzzy Inference System (FIS)**  
✔ Mengklasifikasikan kualitas tanah berdasarkan parameter kimia  
✔ Membangun aplikasi berbasis web  
✔ Mengurangi subjektivitas dalam analisis tanah  

---

## 🧠 Metodologi

Metode utama yang digunakan adalah:

### 🔶 Logika Fuzzy Sugeno

Alur sistem:

---

## 📊 Parameter Input

Sistem menggunakan 6 parameter kimia tanah:

| Parameter | Keterangan |
|----------|-----------|
| pH | Tingkat keasaman tanah |
| KTK | Kapasitas Tukar Kation |
| C-Organik | Kandungan bahan organik |
| N-Total | Nitrogen total |
| P-Total | Fosfor total |
| K-Total | Kalium total |

---

## 📈 Output Sistem

Sistem menghasilkan:

| Nilai | Kategori |
|------|---------|
| 0 | Tidak Sehat |
| 1 | Kurang Sehat |
| 2 | Sehat |

---

## 🏗️ Struktur Project

---

## ⚙️ Instalasi, Menjalankan, dan Penggunaan Sistem

Panduan ini menjelaskan langkah-langkah untuk menginstall, menjalankan, dan menggunakan aplikasi web klasifikasi kualitas tanah berbasis Fuzzy Sugeno.

---

## 🧩 1. Clone Repository

Unduh project dari GitHub ke komputer Anda:

```bash
git clone https://github.com/username/kualitas_tanah.git
cd kualitas_tanah
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
http://127.0.0.1:8000/
Input Data → Fuzzifikasi → Rule Base → Inferensi → Defuzzifikasi → Output

