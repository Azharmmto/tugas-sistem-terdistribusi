# 📚 Tugas Sistem Terdistribusi

## 📖 Deskripsi
Repositori ini berisi tugas mata kuliah **Sistem Terdistribusi** yang mengimplementasikan aplikasi web berbasis Flask dengan integrasi Telegram Bot. Aplikasi ini mendemonstrasikan konsep sistem terdistribusi melalui komunikasi antar sistem yang berbeda menggunakan API.

## 🎯 Tujuan Pembelajaran
- Memahami konsep dasar sistem terdistribusi
- Implementasi komunikasi client-server
- Integrasi dengan API eksternal (Telegram Bot API)
- Penanganan asynchronous request/response
- Error handling dalam sistem terdistribusi

## 🚀 Fitur Utama
1. ✅ **Telegram Bot Integration** - Integrasi dengan Telegram Bot API untuk mengirim notifikasi
2. ✅ **Web Interface** - Interface web untuk input dan interaksi user
3. ✅ **Real-time Messaging** - Pengiriman pesan real-time ke Telegram
4. ✅ **Document Management** - Sistem manajemen dokumen markdown

## 🛠️ Teknologi yang Digunakan
- **Backend**: Python 3.12 + Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Bot Framework**: python-telegram-bot
- **API**: Telegram Bot API
- **Environment Management**: python-dotenv

## 📁 Struktur Repositori
```
tugas-sistem-terdistribusi/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (TELEGRAM_BOT_TOKEN)
├── templates/
│   └── index.html        # Web interface
├── static/
│   └── js/
│       └── script.js     # Frontend logic
├── markdown/              # 16+ dokumentasi lengkap
│   ├── TELEGRAM_SETUP_GUIDE.md
│   ├── RINGKASAN_PERUBAHAN_TELEGRAM.md
│   ├── README.md
│   └── ... (file lainnya)
└── README.md             # File ini
```

## 📦 Cara Instalasi

### 1. Clone Repositori
```bash
git clone https://github.com/Azharmmto/tugas-sistem-terdistribusi.git
cd tugas-sistem-terdistribusi
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Telegram Bot

#### a. Buat Bot Baru
1. Buka Telegram dan cari `@BotFather`
2. Kirim perintah `/newbot`
3. Ikuti instruksi untuk memberi nama bot
4. Copy **TOKEN** yang diberikan

#### b. Dapatkan Telegram ID Anda
1. Buka Telegram dan cari `@userinfobot`
2. Kirim perintah `/start`
3. Copy **ID** (berupa angka) yang diberikan

#### c. Start Chat dengan Bot
1. Cari bot yang baru Anda buat di Telegram
2. Klik **START** (Wajib dilakukan!)

### 4. Konfigurasi Environment
Buat file `.env` di root folder dan isi dengan:
```bash
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

Ganti `your_bot_token_here` dengan token yang Anda dapatkan dari BotFather.

### 5. Jalankan Aplikasi
```bash
python3 app.py
```

Aplikasi akan berjalan di: `http://localhost:5000`

## 📱 Cara Penggunaan

### Langkah-langkah:
1. **Buka browser** dan akses `http://localhost:5000`
2. **Input Telegram ID** Anda (angka yang didapat dari @userinfobot)
3. **Klik tombol "Kirim"**
4. **Cek Telegram** Anda - pesan akan langsung masuk! 📱⚡

### Contoh Flow:
```
User → Web Interface → Input Telegram ID → Submit
                ↓
        Flask Backend (app.py)
                ↓
        Telegram Bot API
                ↓
        Pesan diterima di Telegram User
```

## 🔧 Troubleshooting

| Error | Penyebab | Solusi |
|-------|----------|--------|
| "Chat not found" | Belum start chat dengan bot | Buka bot di Telegram dan klik START |
| "Token not configured" | File .env tidak ada/kosong | Pastikan file .env berisi TELEGRAM_BOT_TOKEN |
| "ID harus angka" | Input bukan angka | Gunakan Telegram ID berupa angka dari @userinfobot |
| "Bot not responding" | Token salah | Periksa kembali token di .env |

## 📡 Konsep Sistem Terdistribusi yang Diimplementasikan

### 1. **Client-Server Architecture**
- Web browser sebagai client
- Flask application sebagai server
- Telegram API sebagai external service

### 2. **API Integration**
- RESTful communication
- HTTP request/response pattern
- JSON data exchange

### 3. **Asynchronous Communication**
- Non-blocking message delivery
- Real-time notification system

### 4. **Service-Oriented Architecture (SOA)**
- Independent services (Web App + Telegram Bot)
- Loose coupling between components
- Each service has specific responsibility

### 5. **Error Handling & Fault Tolerance**
- Try-catch mechanism
- User-friendly error messages
- Graceful degradation

## 📚 Dokumentasi Lengkap

Untuk dokumentasi lebih detail, lihat folder `markdown/`:
- **TELEGRAM_SETUP_GUIDE.md** - Panduan setup lengkap Telegram Bot
- **RINGKASAN_PERUBAHAN_TELEGRAM.md** - Changelog dan perubahan sistem
- **README.md** - Dokumentasi teknis lengkap

## 🎓 Pembelajaran dari Project Ini

Melalui project ini, mahasiswa belajar tentang:
- ✅ Komunikasi antar sistem yang terdistribusi
- ✅ Integration dengan third-party API
- ✅ Real-time messaging system
- ✅ Client-server architecture
- ✅ Error handling dalam distributed systems
- ✅ Environment configuration management

## 📊 Diagram Arsitektur

```
┌─────────────┐         ┌──────────────┐         ┌────────────────┐
│   Browser   │ ◄─────► │ Flask Server │ ◄─────► │ Telegram API   │
│  (Client)   │  HTTP   │   (Backend)  │  HTTPS  │   (External)   │
└─────────────┘         └──────────────┘         └────────────────┘
                                │
                                ▼
                        ┌──────────────┐
                        │  Telegram    │
                        │  User App    │
                        └──────────────┘
```

## 👨‍💻 Pengembang
**Azhar Mamonto** (AI)

## 📄 Lisensi
Project ini dibuat untuk keperluan akademik - Tugas Mata Kuliah Sistem Terdistribusi.

## 🤝 Kontribusi
Ini adalah project tugas kuliah. Untuk saran atau pertanyaan, silakan buat issue di repositori ini.

---

**Version**: 3.0 - Telegram Bot Edition  
**Status**: ✅ READY TO USE  
**Last Updated**: 2025-12-09

💡 **Tips**: Pastikan Anda sudah start chat dengan bot di Telegram sebelum mengirim pesan pertama!

📖 **Dokumentasi Lengkap**: Lihat folder `markdown/` untuk panduan detail
