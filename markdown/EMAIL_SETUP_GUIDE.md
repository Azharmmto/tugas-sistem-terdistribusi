# 📧 PANDUAN SETUP EMAIL - InfoHub Dashboard

## 🎯 Overview

Aplikasi ini sekarang **benar-benar mengirim email** ke user menggunakan SMTP Gmail!

---

## ⚙️ CARA SETUP (Step-by-Step)

### 1️⃣ Setup Gmail App Password

#### A. Aktifkan 2-Factor Authentication
1. Buka https://myaccount.google.com/security
2. Cari "2-Step Verification" 
3. Klik dan ikuti instruksi untuk mengaktifkan
4. Gunakan phone number atau authenticator app

#### B. Generate App Password
1. Setelah 2FA aktif, kembali ke https://myaccount.google.com/security
2. Cari "App passwords" atau "Sandi aplikasi"
3. Klik "App passwords"
4. Pilih:
   - **App**: Mail
   - **Device**: Other (Custom name)
   - **Name**: InfoHub Dashboard
5. Klik "Generate"
6. **COPY** 16-digit password yang muncul (format: abcd efgh ijkl mnop)
7. Simpan password ini dengan aman!

### 2️⃣ Konfigurasi Environment Variables

#### A. Copy file .env.example
```bash
cd /mnt/d/berkas_umi/kuliah_22/semester_vii/sistem-terdistribusi/tugas_akhir2
cp .env.example .env
```

#### B. Edit file .env
```bash
nano .env
# atau gunakan text editor favorit
```

#### C. Isi dengan credentials Anda
```env
SMTP_EMAIL=johndoe@gmail.com
SMTP_PASSWORD=abcdefghijklmnop
```

**PENTING:**
- Ganti `johndoe@gmail.com` dengan email Gmail Anda
- Ganti `abcdefghijklmnop` dengan App Password 16-digit (hapus spasi)
- Jangan gunakan password Gmail biasa!

### 3️⃣ Test Email

#### A. Jalankan aplikasi
```bash
python3 app.py
```

#### B. Buka browser
```
http://localhost:5000
```

#### C. Test kirim email
1. Scroll ke bagian "📧 Laporan Harian (Daily Briefing)"
2. Masukkan email tujuan (bisa email Anda sendiri untuk test)
3. Klik tombol "Kirim"
4. Tunggu beberapa detik
5. Cek inbox email Anda!

---

## ✅ TROUBLESHOOTING

### Error: SMTP Authentication failed

**Penyebab:**
- App Password salah
- 2FA belum aktif
- Email atau password tidak valid

**Solusi:**
1. Pastikan 2FA sudah aktif
2. Generate ulang App Password
3. Copy App Password dengan benar (tanpa spasi)
4. Edit .env dengan credentials yang benar

### Error: SMTP credentials not configured

**Penyebab:**
- File .env tidak ada
- File .env kosong
- Nama variable salah

**Solusi:**
1. Pastikan file .env ada di root directory
2. Pastikan isi file .env:
   ```
   SMTP_EMAIL=your_email@gmail.com
   SMTP_PASSWORD=your_app_password
   ```
3. Restart aplikasi

### Email tidak masuk

**Cek:**
1. Spam folder
2. Console/terminal untuk error messages
3. Email tujuan valid?
4. Koneksi internet stabil?

---

## 🔒 KEAMANAN

### DO ✅
- ✅ Gunakan App Password (bukan password Gmail biasa)
- ✅ Simpan .env di local saja (jangan commit ke Git)
- ✅ Gunakan environment variables
- ✅ Backup App Password di tempat aman

### DON'T ❌
- ❌ Jangan commit .env ke Git
- ❌ Jangan share App Password ke orang lain
- ❌ Jangan hardcode password di code
- ❌ Jangan gunakan password Gmail biasa

---

## 📧 FORMAT EMAIL YANG DIKIRIM

### Subject
```
Daily Briefing - InfoHub Dashboard
```

### Content (HTML)
```html
📊 Laporan Harian (Daily Briefing)
Tanggal: 26 November 2025

🌤️ Cuaca Hari Ini
- Berawan - 26°C
- 📍 Kota Makassar, Sulawesi Selatan
- 💨 Angin: 6.6 km/h (NE)
- 💧 Kelembaban: 89%

💱 Kurs Rupiah Hari Ini
- 1 USD = Rp 15,750.00

📰 Berita Teknologi Teratas
1. [Judul Berita 1]
   Deskripsi...
   [Baca selengkapnya →]

2. [Judul Berita 2]
3. [Judul Berita 3]

---
InfoHub Dashboard
Email ini dibuat secara otomatis. Mohon tidak membalas email ini.
```

---

## 🧪 TESTING

### Test Manual
1. Jalankan aplikasi: `python3 app.py`
2. Buka browser: `http://localhost:5000`
3. Input email Anda sendiri
4. Klik "Kirim"
5. Cek inbox (dan spam folder)

### Test Script
```bash
# Edit test_briefing.py untuk menggunakan real email
python3 test_briefing.py
```

---

## 📊 MONITORING

### Check Console Output
Saat mengirim email, console akan menampilkan:
```
Mengirim email ke user@example.com...
✓ Email berhasil dikirim ke user@example.com
```

### Error Messages
```
ERROR: SMTP Authentication failed!
ERROR: SMTP credentials not configured!
ERROR: Gagal mengirim email: [error detail]
```

---

## 🔧 KONFIGURASI LANJUTAN

### Gunakan SMTP Server Lain

Edit `app.py` di fungsi `send_email_smtp()`:

```python
# Untuk Outlook/Hotmail
with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:

# Untuk Yahoo
with smtplib.SMTP('smtp.mail.yahoo.com', 587) as server:

# Untuk SMTP custom
with smtplib.SMTP('your-smtp-server.com', 587) as server:
```

### Rate Limiting (Production)

Tambahkan di app.py untuk limit email per user:
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/api/send-briefing', methods=['POST'])
@limiter.limit("5 per hour")  # Max 5 email per jam per IP
def send_briefing():
    # ...
```

---

## 📝 CHECKLIST FINAL

Sebelum deploy ke production:

- [ ] 2FA Gmail aktif
- [ ] App Password generated
- [ ] File .env configured dengan credentials valid
- [ ] File .env masuk .gitignore
- [ ] Test kirim email berhasil
- [ ] Email diterima di inbox
- [ ] Format email rapi dan benar
- [ ] Error handling works
- [ ] Console logging clear

---

## 🎉 SELESAI!

Email sekarang benar-benar dikirim! 📧

**Status**: Production Ready ✅

---

## 💡 TIPS

1. **Test dengan email sendiri dulu** sebelum kirim ke orang lain
2. **Cek spam folder** jika email tidak masuk
3. **Backup App Password** di password manager
4. **Monitor console** untuk debugging
5. **Rate limit** untuk avoid abuse

---

**Last Updated**: 26 November 2025  
**Status**: Real Email Implementation ✅
