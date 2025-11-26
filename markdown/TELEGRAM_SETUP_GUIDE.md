# 🤖 PANDUAN SETUP TELEGRAM BOT - InfoHub Dashboard

## 🎯 Overview

Aplikasi sekarang menggunakan **Telegram Bot** untuk mengirim Daily Briefing!

---

## ⚙️ CARA SETUP (10 Menit)

### 1️⃣ Buat Telegram Bot

#### A. Buka Telegram & Cari @BotFather
1. Buka aplikasi Telegram (mobile atau desktop)
2. Di search, ketik: `@BotFather`
3. Klik bot dengan centang biru (verified)
4. Klik "START" atau "MULAI"

#### B. Buat Bot Baru
1. Kirim command: `/newbot`
2. BotFather akan tanya nama bot
   - Contoh: `InfoHub Dashboard Bot`
3. BotFather akan tanya username bot (harus diakhiri "bot")
   - Contoh: `infohub_dashboard_bot`
4. BotFather akan memberikan **TOKEN**
   - Format: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`
5. **COPY TOKEN** ini dengan aman!

#### C. Contoh Percakapan dengan BotFather
```
You: /newbot
BotFather: Alright, a new bot. How are we going to call it?

You: InfoHub Dashboard Bot
BotFather: Good. Now let's choose a username for your bot.

You: infohub_dashboard_bot
BotFather: Done! Congratulations on your new bot.
Use this token to access the HTTP API:
1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

Keep your token secure!
```

---

### 2️⃣ Dapatkan Telegram ID User

#### A. Cari @userinfobot
1. Di Telegram, search: `@userinfobot`
2. Klik bot dan klik "START"
3. Bot akan reply dengan info user Anda
4. **Copy ID** (angka panjang)

#### B. Contoh Response dari userinfobot
```
Id: 123456789
First name: John
Username: @johndoe
```

Copy angka `123456789` - ini adalah Telegram ID Anda!

---

### 3️⃣ Start Chat dengan Bot Anda

**PENTING:** User harus start chat dengan bot dulu!

1. Di Telegram, search username bot Anda (contoh: `@infohub_dashboard_bot`)
2. Klik bot
3. Klik "START" atau ketik `/start`
4. Bot mungkin tidak reply (itu normal jika belum ada command handler)
5. Yang penting: chat sudah dimulai!

---

### 4️⃣ Konfigurasi .env

#### A. Copy file template
```bash
cd /mnt/d/berkas_umi/kuliah_22/semester_vii/sistem-terdistribusi/tugas_akhir2
cp .env.example .env
```

#### B. Edit file .env
```bash
nano .env
```

#### C. Isi dengan Bot Token Anda
```env
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

**PENTING:**
- Ganti dengan TOKEN yang diberikan BotFather
- Jangan tambahkan spasi atau quote
- Simpan file

---

### 5️⃣ Test Telegram Bot

#### A. Jalankan aplikasi
```bash
python3 app.py
```

#### B. Buka browser
```
http://localhost:5000
```

#### C. Test kirim pesan
1. Scroll ke "📧 Laporan Harian"
2. Masukkan **Telegram ID** Anda (angka dari @userinfobot)
3. Klik "Kirim"
4. Tunggu beberapa detik
5. **Cek Telegram Anda!** Pesan harus masuk 📱

---

## ✅ TROUBLESHOOTING

### Error: Telegram Bot Token not configured

**Penyebab:**
- File .env kosong atau tidak ada
- Token tidak diisi

**Solusi:**
1. Pastikan file .env ada
2. Isi TELEGRAM_BOT_TOKEN dengan token dari BotFather
3. Restart aplikasi

---

### Error: Bad Request / Chat not found

**Penyebab:**
- User belum start chat dengan bot
- Telegram ID salah

**Solusi:**
1. **Wajib:** Buka bot di Telegram dan klik START
2. Verifikasi Telegram ID benar (dari @userinfobot)
3. Pastikan ID berupa angka saja (tanpa @)

---

### Pesan tidak masuk ke Telegram

**Cek:**
1. ✅ Sudah start chat dengan bot?
2. ✅ Token benar?
3. ✅ Telegram ID benar?
4. ✅ Cek console untuk error
5. ✅ Internet stabil?

**Debug:**
```bash
# Cek console output
Mengirim pesan Telegram ke chat_id: 123456789...
✓ Pesan berhasil dikirim ke Telegram chat_id: 123456789
```

---

### Telegram ID harus berupa angka

**Penyebab:**
- Input bukan angka
- Ada karakter @ atau huruf

**Solusi:**
- Gunakan hanya angka: `123456789`
- Jangan gunakan: `@username` atau nama

---

## 📱 FORMAT PESAN TELEGRAM

### Contoh Pesan yang Dikirim:

```
📊 Laporan Harian (Daily Briefing)
📅 Tanggal: 26 November 2025
━━━━━━━━━━━━━━━━━━━━━━━

🌤️ Cuaca Hari Ini ☁️
├ Kondisi: Berawan
├ Suhu: 26°C
├ Lokasi: Kota Makassar, Sulawesi Selatan
├ Angin: 6.6 km/h (NE)
└ Kelembaban: 89%

💱 Kurs Rupiah Hari Ini
└ 1 USD = Rp 15,750.00

📰 Berita Teknologi Teratas

1. Detik-detik Roket Rusia Meluncur ke Orbit
   Baca selengkapnya

2. Pemerintah Siapkan Peta Jalan AI
   Baca selengkapnya

3. Robot Polisi Patroli Keliling Jaga Dubai
   Baca selengkapnya

━━━━━━━━━━━━━━━━━━━━━━━
InfoHub Dashboard
Sistem Informasi Terintegrasi
```

**Format:**
- ✅ Markdown formatting
- ✅ Emoji untuk visual
- ✅ Link clickable
- ✅ Clean & professional

---

## 🔒 KEAMANAN

### ✅ DO
- ✅ Simpan Bot Token dengan aman
- ✅ File .env di local saja (tidak commit ke Git)
- ✅ Jangan share token ke orang lain
- ✅ Gunakan .gitignore

### ❌ DON'T
- ❌ Jangan commit .env ke Git
- ❌ Jangan share Bot Token di public
- ❌ Jangan hardcode token di code
- ❌ Jangan post screenshot dengan token visible

---

## 🧪 TESTING

### Test Manual
```bash
# 1. Jalankan app
python3 app.py

# 2. Buka browser
http://localhost:5000

# 3. Input Telegram ID
# 4. Klik Kirim
# 5. Cek Telegram!
```

### Test dengan curl
```bash
curl -X POST http://localhost:5000/api/send-briefing \
  -H "Content-Type: application/json" \
  -d '{"telegram_id": "123456789"}'
```

---

## 📊 MONITORING

### Console Output (Success)
```
Mengirim pesan Telegram ke chat_id: 123456789...
✓ Pesan berhasil dikirim ke Telegram chat_id: 123456789
```

### Console Output (Error)
```
ERROR: Telegram Bot Token not configured!
Please set TELEGRAM_BOT_TOKEN in .env file
```

---

## 💡 TIPS & TRICKS

### 1. Test dengan ID Sendiri
- Input Telegram ID Anda sendiri
- Pastikan pesan masuk sebelum share ke user lain

### 2. Bot Commands (Optional)
Tambahkan commands ke bot via @BotFather:
```
/start - Mulai menggunakan bot
/help - Bantuan
/briefing - Dapatkan daily briefing
```

### 3. Custom Bot Profile
Set foto profil dan deskripsi via @BotFather:
- `/setuserpic` - Upload foto bot
- `/setdescription` - Set deskripsi bot
- `/setabouttext` - Set about text

### 4. Rate Limiting
Untuk production, tambahkan rate limiting:
- Max 1 pesan per user per 5 menit
- Hindari spam ke Telegram API

---

## 🔧 KONFIGURASI LANJUTAN

### Environment Variables
```env
# .env file
TELEGRAM_BOT_TOKEN=your_token_here

# Optional: untuk multiple bots
# TELEGRAM_BOT_TOKEN_DEV=dev_token
# TELEGRAM_BOT_TOKEN_PROD=prod_token
```

### Telegram API Limits
- ✅ Max 30 messages per second per bot
- ✅ Max 20 messages per minute per chat
- ✅ Message max 4096 characters

---

## 📝 CHECKLIST SETUP

Sebelum testing:

- [ ] Bot created via @BotFather
- [ ] Bot Token copied
- [ ] User Telegram ID obtained (@userinfobot)
- [ ] User started chat with bot
- [ ] File .env configured with token
- [ ] File .env in .gitignore
- [ ] Application running
- [ ] Test message sent
- [ ] Message received in Telegram

---

## 🎓 UNTUK PRESENTASI

### Demo Flow:
1. ✅ Tampilkan bot di Telegram
2. ✅ Tunjukkan cara dapatkan Telegram ID
3. ✅ Input ID di aplikasi web
4. ✅ Klik "Kirim"
5. ✅ Show console: "✓ Pesan berhasil dikirim"
6. ✅ **Buka Telegram dan tunjukkan pesan!** 📱

### Talking Points:
- "Menggunakan Telegram Bot API"
- "User input Telegram ID, bukan email"
- "Pesan langsung masuk ke Telegram"
- "Format rapi dengan Markdown"
- "Real-time notification"

---

## 🚀 STATUS

**Notification System**: ✅ Telegram Bot  
**Implementation**: ✅ PRODUCTION READY  
**Testing**: ✅ READY  
**Documentation**: ✅ COMPLETE  

---

**Last Updated**: 26 November 2025  
**Version**: 3.0 - Telegram Bot Implementation  
**Status**: ✅ READY FOR USE
