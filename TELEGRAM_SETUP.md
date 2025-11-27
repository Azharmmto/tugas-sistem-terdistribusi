# 📱 Panduan Setup Telegram Bot - InfoHub Dashboard

## ✅ Status Bot
- **Bot Name**: notifst
- **Bot Username**: @notifst_bot
- **Bot Token**: ✓ Sudah dikonfigurasi di `.env`
- **Status**: ✓ Bot Aktif dan Berfungsi

---

## 🚀 Cara Menggunakan (PENTING!)

### Langkah 1: Start Chat dengan Bot
**WAJIB dilakukan sebelum menggunakan website!**

1. Buka aplikasi **Telegram** (HP atau Desktop)
2. Di kotak pencarian, ketik: `@notifst_bot`
3. Klik bot yang muncul
4. Klik tombol **"Start"** atau kirim pesan apapun
5. Bot mungkin tidak membalas - **ini normal!**

> ⚠️ **Tanpa langkah ini, bot tidak bisa mengirim pesan ke Anda!**

---

### Langkah 2: Dapatkan Telegram ID Anda

1. Di Telegram, cari bot: `@userinfobot`
2. Klik **"Start"**
3. Bot akan menampilkan informasi Anda, termasuk:
   ```
   Id: 123456789
   ```
4. **Copy angka ID tersebut** (contoh: `123456789`)

---

### Langkah 3: Gunakan di Website

1. Buka website **InfoHub Dashboard**
2. Scroll ke bagian **"Laporan Harian"**
3. Masukkan **Telegram ID** yang sudah Anda dapatkan
4. Klik tombol **"Kirim"**
5. Daily briefing akan dikirim ke Telegram Anda! 🎉

---

## ❌ Troubleshooting - Jika Error

### Error: "Telegram ID tidak ditemukan"
**Penyebab**: Anda belum memulai chat dengan bot

**Solusi**:
1. Buka Telegram, cari `@notifst_bot`
2. Klik **"Start"** atau kirim pesan apapun
3. Tunggu beberapa detik
4. Coba kirim lagi dari website

---

### Error: "Bot telah diblokir"
**Penyebab**: Anda pernah block bot ini

**Solusi**:
1. Buka chat dengan `@notifst_bot`
2. Unblock bot (menu ⋮ → Unblock)
3. Klik **"Start"** lagi
4. Coba kirim lagi dari website

---

### Error: "Telegram ID harus berupa angka"
**Penyebab**: Format ID salah

**Solusi**:
- ✗ Jangan gunakan: `@username` atau `username`
- ✓ Gunakan angka saja: `123456789`
- ✓ Copy-paste langsung dari @userinfobot

---

### Error lainnya
**Cek hal berikut**:
- ✓ Pastikan tidak ada spasi di awal/akhir ID
- ✓ Pastikan ID yang Anda masukkan benar
- ✓ Coba refresh halaman website
- ✓ Coba hapus chat dengan bot, lalu start ulang

---

## 🧪 Test Integrasi Telegram

Jalankan script testing untuk memverifikasi setup:

```bash
python3 test_telegram_fix.py
```

Atau test manual dengan curl:

```bash
# Test 1: Cek bot aktif
curl "https://api.telegram.org/bot8465524984:AAHojMWQ2MEQZsb0txRr1XqMGtvP_VB0jiA/getMe"

# Test 2: Kirim pesan (ganti YOUR_TELEGRAM_ID)
curl -X POST "https://api.telegram.org/bot8465524984:AAHojMWQ2MEQZsb0txRr1XqMGtvP_VB0jiA/sendMessage" \
  -H "Content-Type: application/json" \
  -d '{"chat_id": "YOUR_TELEGRAM_ID", "text": "Test dari InfoHub"}'
```

---

## 📋 Apa yang Akan Dikirim Bot?

Bot akan mengirim **Daily Briefing** berisi:

1. 🌤️ **Cuaca Hari Ini**
   - Kondisi cuaca terkini
   - Suhu, kelembaban, angin
   - Lokasi: Makassar, Sulawesi Selatan

2. 💱 **Kurs Rupiah**
   - Nilai tukar 1 USD ke IDR hari ini

3. 📰 **3 Berita Teknologi Teratas**
   - Berita dari CNN Indonesia
   - Kategori: Teknologi
   - Link untuk baca selengkapnya

---

## 🔐 Keamanan

- ✓ Bot Token tersimpan aman di file `.env` (tidak di-commit ke Git)
- ✓ Bot hanya bisa mengirim pesan ke user yang sudah start chat
- ✓ Bot tidak menyimpan data pribadi
- ✓ Bot tidak bisa membaca pesan Anda

---

## 📞 Support

Jika masih ada masalah:
1. Pastikan file `.env` berisi `TELEGRAM_BOT_TOKEN`
2. Pastikan bot `@notifst_bot` aktif
3. Pastikan sudah start chat dengan bot
4. Cek log di terminal saat menjalankan `python app.py`

---

**Selamat menggunakan InfoHub Dashboard! 🚀**
