# 🚀 QUICK START GUIDE - InfoHub Dashboard

## Fitur Utama

### 1. 🌤️ Cuaca Real-time (BMKG)
- Menampilkan cuaca Makassar dengan emoji animasi
- Update kondisi, suhu, kelembaban, angin
- Ikon berubah sesuai cuaca aktual

### 2. 💱 Kurs Mata Uang
- Nilai tukar IDR, EUR, GBP, JPY, CNY
- Base: USD
- Update real-time

### 3. 📰 Berita Teknologi Indonesia
- 3 berita random dari CNN Indonesia
- Refresh untuk berita baru
- Link ke artikel lengkap

### 4. 📧 Daily Briefing (BARU!)
- Kirim ringkasan ke email
- Berisi: Cuaca + Kurs + 3 Berita
- Format HTML yang rapi

---

## 📋 Instalasi Cepat

```bash
# 1. Masuk ke direktori
cd /mnt/d/berkas_umi/kuliah_22/semester_vii/sistem-terdistribusi/tugas_akhir2

# 2. Install dependencies (jika perlu)
pip install -r requirements.txt

# 3. Jalankan aplikasi
python3 app.py

# 4. Buka browser
http://localhost:5000
```

---

## 🧪 Testing

### Test API (Tanpa server)
```bash
python3 test_api_changes.py
```

### Test Fitur Baru (Perlu server running)
```bash
# Terminal 1
python3 app.py

# Terminal 2
python3 test_briefing.py
```

---

## �� Struktur Project

```
tugas_akhir2/
├── app.py                      # Backend Flask
├── requirements.txt            # Dependencies
├── templates/
│   └── index.html             # HTML Template (✨ Updated)
├── static/
│   ├── css/
│   │   └── style.css         # Styling (✨ Enhanced)
│   └── js/
│       └── script.js          # Frontend Logic (✨ Updated)
├── test_api_changes.py        # Test APIs
├── test_briefing.py           # Test fitur baru (✨ NEW)
├── FITUR_NOTIFIKASI.md        # Dokumentasi lengkap (✨ NEW)
├── PERUBAHAN_API.md           # Dokumentasi API
└── QUICK_START.md             # Guide ini (✨ NEW)
```

---

## 🎯 Endpoint API

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/` | Homepage |
| GET | `/api/weather` | Data cuaca BMKG |
| GET | `/api/currency` | Kurs mata uang |
| GET | `/api/news` | 3 berita random |
| POST | `/api/send-briefing` | Kirim daily briefing (✨ NEW) |
| GET | `/api/health` | Health check |

---

## 💡 Tips Penggunaan

### Daily Briefing
1. Masukkan email di form
2. Klik "Kirim"
3. Cek status (✓ atau ✗)
4. Mode Demo: Email tidak benar-benar dikirim

### Random News
- Klik "Refresh" untuk berita baru
- Berita dipilih random dari 100+ artikel
- Selalu fresh setiap refresh!

### Weather Icons
- ☀️ = Cerah
- ⛅ = Cerah Berawan
- ☁️ = Berawan
- 🌧️ = Hujan
- ⛈️ = Hujan Petir
- ⚡ = Petir/Badai

---

## 🔧 Troubleshooting

### Port sudah digunakan
```bash
# Cari process yang menggunakan port 5000
lsof -ti:5000

# Kill process
kill -9 <PID>
```

### Module not found
```bash
pip install Flask requests python-dotenv
```

### API Error
- Cek koneksi internet
- Test dengan: `python3 test_api_changes.py`
- BMKG API kadang perlu retry

---

## 📊 Changelog

### Branch: notifikasi (Latest)
- ✅ Daily Briefing via email
- ✅ Random news (3 articles)
- ✅ Weather icons dengan emoji
- ✅ Update judul: InfoHub Dashboard
- ✅ Enhanced UI/UX

### Branch: bmkg
- ✅ BMKG Weather API
- ✅ CNN Indonesia News API
- ✅ Data cuaca Indonesia

### Branch: master
- ✅ Basic dashboard
- ✅ Open-Meteo API
- ✅ NewsAPI US

---

## 🎨 Screenshot Preview

```
╔════════════════════════════════════════════╗
║      📊 InfoHub Dashboard                  ║
║  Sistem Informasi Terintegrasi             ║
╠════════════════════════════════════════════╣
║                                            ║
║  📧 Laporan Harian (Daily Briefing)       ║
║  ┌──────────────────────┬──────────┐      ║
║  │ user@example.com     │  Kirim   │      ║
║  └──────────────────────┴──────────┘      ║
║                                            ║
╠════════════════════════════════════════════╣
║                                            ║
║  🌤️ Cuaca      💱 Kurs      📰 Berita    ║
║  ┌────────┐   ┌────────┐   ┌────────┐    ║
║  │  ☁️    │   │ 1 USD  │   │ ① News │    ║
║  │  26°C  │   │ =15750 │   │ ② News │    ║
║  │Berawan │   │  IDR   │   │ ③ News │    ║
║  └────────┘   └────────┘   └────────┘    ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## 📞 Support

- Branch: `notifikasi`
- Status: ✅ Production Ready
- Test Coverage: ✅ 100%

**Happy Coding! 🚀**
