# RINGKASAN PERUBAHAN API

## Tanggal: 26 November 2025
## Branch: bmkg

---

## Perubahan yang Dilakukan

### 1. API Cuaca - BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)

**Sebelumnya:**
- API: Open-Meteo API
- URL: `https://api.open-meteo.com/v1/forecast`
- Parameter: latitude, longitude, timezone

**Sekarang:**
- API: BMKG API (API resmi Indonesia)
- URL: `https://api.bmkg.go.id/publik/prakiraan-cuaca`
- Parameter: adm4 (kode wilayah administratif)
- Kode Wilayah: `73.71.09.1009` (Karuwisi Utara, Kota Makassar, Sulawesi Selatan)

**Data yang Ditampilkan:**
- Suhu (°C)
- Kondisi cuaca (deskripsi dalam Bahasa Indonesia)
- Kecepatan angin (km/h)
- Arah angin (derajat dan arah mata angin)
- Kelembaban (%)
- Jarak pandang
- Waktu update
- Lokasi lengkap (Desa, Kecamatan, Kota, Provinsi)

---

### 2. API Berita Teknologi - CNN Indonesia

**Sebelumnya:**
- API: Saurav.tech NewsAPI Mirror
- URL: `https://saurav.tech/NewsAPI/top-headlines/category/technology/us.json`
- Bahasa: Inggris (US)
- Kategori: Teknologi

**Sekarang:**
- API: CNN Indonesia API (via berita-indo-api)
- URL: `https://berita-indo-api-next.vercel.app/api/cnn-news/teknologi`
- Bahasa: Indonesia
- Kategori: Teknologi
- Sumber: CNN Indonesia

**Data yang Ditampilkan:**
- Judul berita
- Deskripsi singkat
- Link artikel
- Tanggal publikasi
- Gambar thumbnail

---

## File yang Dimodifikasi

### 1. `app.py`
- ✓ Mengubah `WEATHER_API_URL` ke BMKG API
- ✓ Mengubah `NEWS_API_URL` ke CNN Indonesia API
- ✓ Mengubah fungsi `get_weather()` untuk menangani struktur data BMKG
- ✓ Menambahkan header User-Agent untuk kompatibilitas BMKG API
- ✓ Mengubah fungsi `get_news()` untuk parsing data CNN Indonesia
- ✓ Menyesuaikan ekstraksi data cuaca dari format BMKG
- ✓ Menyesuaikan ekstraksi data berita dari format CNN Indonesia

### 2. `static/js/script.js`
- ✓ Mengubah fungsi `loadWeather()` untuk menampilkan data BMKG
- ✓ Menyesuaikan parameter request (dari lat/lon ke adm4)
- ✓ Mengupdate tampilan data cuaca dengan field baru:
  - Kondisi cuaca (weather_desc)
  - Kelembaban (hu)
  - Jarak pandang (vs_text)
  - Lokasi lengkap dengan format Indonesia
- ✓ Fungsi `loadNews()` tetap kompatibel dengan struktur baru

### 3. `templates/index.html`
- ✓ Mengubah footer informasi API:
  - "Open-Meteo API" → "BMKG API (Data Cuaca Indonesia)"
  - "News API" → "CNN Indonesia API (Berita Teknologi Indonesia)"

### 4. `test_api_changes.py` (BARU)
- ✓ Script testing untuk validasi API
- ✓ Test BMKG Weather API
- ✓ Test CNN Indonesia News API
- ✓ Output test yang informatif

---

## Hasil Testing

```
============================================================
RINGKASAN TEST
============================================================
BMKG Weather API: ✓ PASSED
Tech News API: ✓ PASSED

✓ SEMUA TEST BERHASIL! API siap digunakan.
```

### Data Real yang Berhasil Diambil:

**BMKG Weather API:**
- Lokasi: Karuwisi Utara, Kota Makassar
- Suhu: 27°C
- Kondisi: Berawan
- Kelembaban: 87%
- Kecepatan Angin: 6.6 km/h

**CNN Indonesia Tech News:**
- Total berita tersedia: 100
- Berita dalam Bahasa Indonesia
- Kategori: Teknologi
- Update real-time

---

## Keunggulan Perubahan

1. **Data Lokal Indonesia**: Menggunakan API resmi BMKG untuk data cuaca Indonesia yang lebih akurat
2. **Berita Bahasa Indonesia**: Berita teknologi dalam bahasa yang mudah dipahami
3. **Data Lebih Lengkap**: BMKG menyediakan informasi cuaca yang lebih detail
4. **Lokasi Spesifik**: Data cuaca untuk wilayah Makassar, Sulawesi Selatan
5. **Sumber Terpercaya**: Menggunakan sumber berita lokal yang kredibel (CNN Indonesia)

---

## Cara Menjalankan

1. Pastikan dependencies terinstall:
   ```bash
   pip install -r requirements.txt
   ```

2. Jalankan aplikasi:
   ```bash
   python3 app.py
   ```

3. Buka browser dan akses:
   ```
   http://localhost:5000
   ```

4. Test API secara terpisah:
   ```bash
   python3 test_api_changes.py
   ```

---

## Catatan Penting

- BMKG API memerlukan User-Agent header untuk mengakses data
- Kode wilayah administratif (adm4) dapat diganti sesuai kebutuhan
- CNN Indonesia API menggunakan proxy dari berita-indo-api-next.vercel.app
- Semua API yang digunakan adalah API publik gratis

---

## Status Branch

- Branch aktif: **bmkg**
- Status: Modified, belum di-commit
- File yang berubah: 3 files (app.py, script.js, index.html)
- File baru: 1 file (test_api_changes.py)

---

**Perubahan berhasil diimplementasikan dan sudah ditest! ✓**
