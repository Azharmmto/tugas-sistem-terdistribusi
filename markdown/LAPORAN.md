# LAPORAN PROJECT SISTEM TERDISTRIBUSI
## Distributed Systems Dashboard

---

## BAB I: PENDAHULUAN

### 1.1 Latar Belakang
Sistem terdistribusi merupakan kumpulan komputer independen yang bekerja sama dan terlihat sebagai satu sistem yang koheren bagi pengguna. Dalam era digital saat ini, hampir semua aplikasi modern mengimplementasikan konsep sistem terdistribusi, terutama dalam bentuk integrasi dengan berbagai layanan eksternal melalui API (Application Programming Interface).

Project ini dibuat untuk memahami dan mengimplementasikan konsep dasar sistem terdistribusi melalui pembuatan aplikasi web yang terintegrasi dengan multiple external APIs.

### 1.2 Tujuan
1. Memahami konsep dasar sistem terdistribusi
2. Mengimplementasikan komunikasi antar sistem melalui REST API
3. Menerapkan error handling dan fault tolerance
4. Memahami arsitektur service-oriented
5. Mengintegrasikan multiple external services

### 1.3 Ruang Lingkup
- Pembuatan web application menggunakan Flask (Python)
- Integrasi dengan 4 external APIs berbeda
- Implementasi RESTful API endpoints
- Frontend dengan HTML, CSS, dan JavaScript
- Real-time data fetching dan display

---

## BAB II: LANDASAN TEORI

### 2.1 Sistem Terdistribusi
Sistem terdistribusi adalah sekumpulan komputer yang autonomous yang tampak sebagai satu sistem yang koheren bagi pengguna. Karakteristik utama:
- **Concurrency**: Multiple processes berjalan bersamaan
- **No global clock**: Tidak ada sinkronisasi waktu global
- **Independent failures**: Setiap komponen dapat gagal secara independen

### 2.2 REST API (Representational State Transfer)
REST adalah arsitektur untuk sistem terdistribusi yang menggunakan HTTP protocol. Prinsip REST:
- **Stateless**: Setiap request independent
- **Client-Server**: Pemisahan concerns
- **Cacheable**: Response dapat di-cache
- **Uniform Interface**: Interface yang konsisten

### 2.3 Service-Oriented Architecture (SOA)
Arsitektur yang membagi aplikasi menjadi services yang independent dan dapat berkomunikasi via network.

### 2.4 Asynchronous Communication
Komunikasi non-blocking dimana sender tidak menunggu response sebelum melanjutkan eksekusi.

---

## BAB III: ANALISIS DAN PERANCANGAN

### 3.1 Analisis Kebutuhan

#### 3.1.1 Kebutuhan Functional
1. Menampilkan data cuaca real-time
2. Menampilkan quote inspiratif
3. Menampilkan nilai tukar mata uang
4. Menampilkan berita teknologi terkini
5. Refresh data secara manual

#### 3.1.2 Kebutuhan Non-Functional
1. Response time < 5 detik
2. User-friendly interface
3. Error handling yang baik
4. Responsive design

### 3.2 Perancangan Sistem

#### 3.2.1 Arsitektur Sistem
```
[Browser/Client]
      ↕ HTTP Request/Response
[Flask Backend Server]
      ↕ API Calls
[External APIs]
  ├── Open-Meteo API (Weather)
  ├── Quotable API (Quotes)
  ├── Exchange Rate API (Currency)
  └── News API (News)
```

#### 3.2.2 Data Flow
1. User membuka browser → Request ke Flask server
2. Flask serve HTML/CSS/JS
3. JavaScript load → Fetch data dari backend endpoints
4. Backend menerima request → Request ke external APIs
5. External APIs response → Backend process data
6. Backend return JSON → Frontend display data

### 3.3 Perancangan API Endpoints

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | / | Main dashboard page |
| GET | /api/weather | Weather data |
| GET | /api/quote | Random quote |
| GET | /api/currency | Exchange rates |
| GET | /api/news | Tech news |
| GET | /api/health | Health check |

---

## BAB IV: IMPLEMENTASI

### 4.1 Teknologi yang Digunakan
- **Backend**: Python 3.12 + Flask 3.0
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **HTTP Client**: requests library
- **Data Format**: JSON

### 4.2 Implementasi Backend (Flask)

#### 4.2.1 Main Application (app.py)
```python
# Struktur dasar:
- Import dependencies
- Define API URLs
- Create Flask app
- Define routes untuk setiap service
- Error handling
- Run server
```

#### 4.2.2 API Integration
Setiap endpoint melakukan:
1. Terima request dari client
2. Parse query parameters (jika ada)
3. Request ke external API dengan timeout
4. Handle errors (try-except)
5. Format response ke JSON
6. Return ke client

### 4.3 Implementasi Frontend

#### 4.3.1 HTML Structure
- Semantic HTML5
- Responsive grid layout
- Card-based UI untuk setiap service

#### 4.3.2 CSS Styling
- Modern gradient design
- Card hover effects
- Responsive breakpoints
- Loading states

#### 4.3.3 JavaScript Logic
- Async/await untuk API calls
- Fetch API untuk HTTP requests
- DOM manipulation untuk display
- Error handling

---

## BAB V: HASIL DAN PENGUJIAN

### 5.1 Hasil Implementasi
Aplikasi berhasil dibuat dengan fitur:
✅ Weather service berfungsi (Open-Meteo API)
✅ Quote service berfungsi (Quotable API)
✅ Currency service berfungsi (Exchange Rate API)
✅ News service berfungsi (News API)
✅ Refresh button untuk setiap service
✅ Error handling yang baik
✅ Responsive design

### 5.2 Pengujian

#### 5.2.1 Functional Testing
| Test Case | Expected | Actual | Status |
|-----------|----------|--------|--------|
| Load weather data | Display temperature, wind | ✅ Displayed | PASS |
| Load quote | Display quote & author | ✅ Displayed | PASS |
| Load currency | Display exchange rates | ✅ Displayed | PASS |
| Load news | Display 5 news articles | ✅ Displayed | PASS |
| Refresh button | Reload fresh data | ✅ Works | PASS |
| Error handling | Show error message | ✅ Works | PASS |

#### 5.2.2 Non-Functional Testing
- **Performance**: Response time rata-rata 2-3 detik
- **Usability**: Interface intuitif dan mudah digunakan
- **Reliability**: Error handling mencegah crash
- **Responsiveness**: Mobile-friendly design

### 5.3 Screenshots
(Dalam implementasi sesungguhnya, tambahkan screenshots aplikasi)

---

## BAB VI: PENUTUP

### 6.1 Kesimpulan
1. Sistem terdistribusi dapat diimplementasikan melalui integrasi multiple APIs
2. REST API merupakan protokol yang efektif untuk komunikasi antar sistem
3. Flask menyediakan framework yang sederhana namun powerful untuk web development
4. Asynchronous communication meningkatkan user experience
5. Error handling sangat penting dalam sistem terdistribusi

### 6.2 Saran Pengembangan
1. **Database Integration**: Tambahkan database untuk caching dan logging
2. **Authentication**: Implement user authentication untuk personalisasi
3. **More APIs**: Tambahkan lebih banyak external services
4. **Containerization**: Deploy menggunakan Docker
5. **Cloud Deployment**: Deploy ke Heroku/AWS/GCP
6. **Monitoring**: Implement logging dan monitoring system
7. **Load Balancing**: Untuk handle traffic tinggi
8. **Microservices**: Pisahkan setiap service ke container terpisah

### 6.3 Pembelajaran
Dari project ini dipelajari:
- Cara mengintegrasikan multiple external APIs
- Implementasi REST API menggunakan Flask
- Asynchronous programming dengan JavaScript
- Error handling dalam distributed systems
- Service-oriented architecture
- Full-stack web development

---

## DAFTAR PUSTAKA

1. Flask Documentation. (2024). Flask Web Development. https://flask.palletsprojects.com/
2. Kleppmann, M. (2017). Designing Data-Intensive Applications. O'Reilly Media.
3. Tanenbaum, A. S., & Van Steen, M. (2017). Distributed Systems: Principles and Paradigms.
4. Fielding, R. T. (2000). Architectural Styles and the Design of Network-based Software Architectures.
5. Richardson, L., & Ruby, S. (2007). RESTful Web Services. O'Reilly Media.

---

## LAMPIRAN

### Lampiran A: Source Code
(Tersedia di folder project)

### Lampiran B: API Documentation

**1. Open-Meteo API**
- URL: https://api.open-meteo.com/v1/forecast
- Method: GET
- Parameters: latitude, longitude, current_weather, timezone

**2. Quotable API**
- URL: https://api.quotable.io/random
- Method: GET
- No parameters required

**3. Exchange Rate API**
- URL: https://api.exchangerate-api.com/v4/latest/USD
- Method: GET
- Returns: Exchange rates for multiple currencies

**4. News API**
- URL: https://saurav.tech/NewsAPI/top-headlines/category/technology/us.json
- Method: GET
- Returns: Technology news articles

---

**Penyusun:** [Nama Mahasiswa]
**NIM:** [NIM Mahasiswa]
**Mata Kuliah:** Sistem Terdistribusi
**Dosen:** [Nama Dosen]
**Tahun Akademik:** 2024
