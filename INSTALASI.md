# 🚀 PETUNJUK INSTALASI DAN MENJALANKAN APLIKASI

## Langkah 1: Pastikan Python Terinstall
Cek versi Python:
```bash
python --version
# atau
python3 --version
```

Aplikasi membutuhkan Python 3.7 atau lebih baru.

## Langkah 2: Install pip (jika belum ada)

### Untuk Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3-pip
```

### Untuk Windows:
Download dan install Python dari https://www.python.org/downloads/
Pastikan checkbox "Add Python to PATH" tercentang saat instalasi.

### Untuk MacOS:
```bash
brew install python3
```

## Langkah 3: Install Dependencies

Buka terminal/command prompt, navigasi ke folder project, lalu jalankan:

```bash
# Navigasi ke folder project
cd tugas_akhir2

# Install dependencies
pip install -r requirements.txt
# atau jika pip tidak tersedia
pip3 install -r requirements.txt
# atau
python -m pip install -r requirements.txt
# atau
python3 -m pip install -r requirements.txt
```

Dependencies yang akan diinstall:
- Flask==3.0.0 (Web framework)
- requests==2.31.0 (HTTP library untuk API calls)
- Werkzeug==3.0.1 (WSGI utility library)

## Langkah 4: Jalankan Aplikasi

```bash
python app.py
# atau
python3 app.py
```

Anda akan melihat output seperti ini:
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://0.0.0.0:5000
Press CTRL+C to quit
```

## Langkah 5: Akses Aplikasi

Buka browser (Chrome, Firefox, Edge, dll) dan akses:
```
http://localhost:5000
```
atau
```
http://127.0.0.1:5000
```

## 🎉 Selamat! Aplikasi Sekarang Berjalan!

Dashboard akan menampilkan:
- 🌤️ Data cuaca real-time dari Open-Meteo API
- 💭 Quote inspiratif dari Quotable API
- 💱 Nilai tukar mata uang dari Exchange Rate API
- 📰 Berita teknologi dari News API

## Troubleshooting

### Problem: pip tidak ditemukan
**Solusi**: Install pip terlebih dahulu (lihat Langkah 2)

### Problem: ModuleNotFoundError: No module named 'flask'
**Solusi**: Install dependencies dengan benar (Langkah 3)

### Problem: Port 5000 sudah digunakan
**Solusi**: Edit file `app.py`, ubah baris terakhir:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Ubah port ke 5001 atau port lain
```

### Problem: API tidak mengembalikan data
**Solusi**: 
- Pastikan koneksi internet aktif
- Beberapa API mungkin sedang down, tunggu beberapa saat dan refresh

### Problem: Browser tidak bisa akses localhost
**Solusi**: Pastikan firewall tidak memblok port 5000

## Testing API Endpoints

Anda bisa test API endpoints menggunakan browser atau tools seperti Postman:

1. **Weather API**: http://localhost:5000/api/weather
2. **Quote API**: http://localhost:5000/api/quote
3. **Currency API**: http://localhost:5000/api/currency
4. **News API**: http://localhost:5000/api/news
5. **Health Check**: http://localhost:5000/api/health

## Menghentikan Aplikasi

Tekan `CTRL+C` di terminal untuk menghentikan server.

## Tips untuk Presentasi

1. Jalankan aplikasi sebelum presentasi dimulai
2. Buka Network tab di Browser DevTools (F12) untuk menunjukkan API calls
3. Demonstrasikan fitur refresh untuk setiap service
4. Jelaskan flow data: Frontend → Backend → External APIs → Backend → Frontend
5. Tunjukkan error handling dengan disconnect internet sebentar

## Virtual Environment (Opsional tapi Direkomendasikan)

Untuk mengisolasi dependencies project:

### Membuat Virtual Environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies di Virtual Environment:
```bash
pip install -r requirements.txt
```

### Deactivate Virtual Environment:
```bash
deactivate
```

---

**Jika masih ada masalah, silakan hubungi dosen atau asisten lab untuk bantuan teknis.**
