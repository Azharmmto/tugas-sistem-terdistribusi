# Distributed Systems Dashboard - Tugas Akhir Sistem Terdistribusi

## 📋 Deskripsi Project
Aplikasi web berbasis Flask yang terintegrasi dengan multiple API eksternal sebagai implementasi konsep sistem terdistribusi. Aplikasi ini mendemonstrasikan komunikasi antar sistem yang berbeda melalui protokol HTTP/REST API.

## 🎯 Tujuan Pembelajaran
- Memahami konsep sistem terdistribusi
- Implementasi integrasi API eksternal
- Komunikasi client-server menggunakan REST API
- Penanganan request/response asynchronous
- Error handling dalam sistem terdistribusi

## 🚀 Fitur Aplikasi

### 1. **Weather Service** 🌤️
- Integrasi dengan Open-Meteo API
- Menampilkan data cuaca real-time
- Informasi: suhu, kecepatan angin, arah angin

### 2. **Quote Service** 💭
- Integrasi dengan Quotable API
- Menampilkan quote inspiratif acak
- Refresh untuk mendapatkan quote baru

### 3. **Currency Exchange Service** 💱
- Integrasi dengan Exchange Rate API
- Menampilkan nilai tukar mata uang (USD ke IDR, EUR, GBP, JPY, CNY)
- Update rate secara real-time

### 4. **News Service** 📰
- Integrasi dengan News API
- Menampilkan berita teknologi terkini
- Link ke artikel lengkap

## 🛠️ Teknologi yang Digunakan
- **Backend**: Python 3.12 + Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API Integration**: requests library
- **Architecture**: RESTful API

## 📦 Struktur Project
```
tugas_akhir2/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend template
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   └── js/
│       └── script.js     # Frontend logic
└── README.md             # Documentation
```

## 🔧 Instalasi dan Menjalankan Aplikasi

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Jalankan Aplikasi
```bash
python app.py
```

### 3. Akses Aplikasi
Buka browser dan akses: `http://localhost:5000`

## 📡 API Endpoints

### Internal API Endpoints:

1. **GET /** - Halaman utama dashboard
2. **GET /api/weather?lat={lat}&lon={lon}** - Get weather data
3. **GET /api/quote** - Get random inspirational quote
4. **GET /api/currency** - Get currency exchange rates
5. **GET /api/news** - Get technology news
6. **GET /api/health** - Health check endpoint

### External API yang Diintegrasikan:

1. **Open-Meteo API** - https://api.open-meteo.com/v1/forecast
   - Weather data service (gratis, no API key required)

2. **Quotable API** - https://api.quotable.io/random
   - Random quotes service (gratis)

3. **Exchange Rate API** - https://api.exchangerate-api.com/v4/latest/USD
   - Currency exchange rates (gratis)

4. **News API Mirror** - https://saurav.tech/NewsAPI/
   - Technology news service (gratis)

## 🎓 Konsep Sistem Terdistribusi yang Diimplementasikan

### 1. **Service-Oriented Architecture (SOA)**
- Aplikasi terdiri dari multiple independent services
- Setiap service memiliki tanggung jawab spesifik
- Loose coupling antar services

### 2. **API Integration & Communication**
- RESTful API sebagai protokol komunikasi
- HTTP request/response pattern
- JSON sebagai format data exchange

### 3. **Asynchronous Communication**
- Frontend melakukan async fetch ke backend
- Backend melakukan async request ke external APIs
- Non-blocking operations

### 4. **Error Handling & Fault Tolerance**
- Try-catch untuk menangani kegagalan API
- Timeout handling
- User-friendly error messages

### 5. **Scalability Concept**
- Modular architecture memungkinkan scaling
- Setiap service dapat di-deploy independent
- Load distribution across multiple APIs

## 📊 Cara Kerja Sistem

1. **User Request**: User mengakses dashboard via browser
2. **Frontend Rendering**: Flask serve HTML template
3. **API Calls**: JavaScript melakukan fetch ke backend endpoints
4. **Backend Processing**: Flask endpoints memproses request
5. **External API Integration**: Backend request data dari external APIs
6. **Data Aggregation**: Backend mengolah dan format response
7. **Response**: Data dikirim kembali ke frontend dalam format JSON
8. **Display**: Frontend menampilkan data ke user

## 🔒 Keamanan
- Semua API yang digunakan adalah public API (gratis)
- Tidak ada API key yang perlu disimpan
- CORS handling untuk cross-origin requests
- Input validation pada query parameters

## 📝 Pengembangan Lebih Lanjut

Untuk meningkatkan aplikasi ini, bisa ditambahkan:
- Database untuk caching dan logging
- Authentication & Authorization
- Rate limiting
- Containerization dengan Docker
- Deployment ke cloud (Heroku, AWS, GCP)
- Load balancing
- Service monitoring & logging

## 👨‍💻 Cara Penggunaan untuk Presentasi

1. Jalankan aplikasi dengan `python app.py`
2. Tunjukkan dashboard dan jelaskan setiap service
3. Klik tombol "Refresh" untuk demonstrate real-time API calls
4. Buka Network tab di browser DevTools untuk show API requests
5. Jelaskan flow data dari frontend → backend → external APIs

## 📚 Referensi
- Flask Documentation: https://flask.palletsprojects.com/
- REST API Design: https://restfulapi.net/
- Distributed Systems Concepts: Martin Kleppmann - Designing Data-Intensive Applications

## 📄 Lisensi
Project ini dibuat untuk keperluan akademik - Tugas Akhir Mata Kuliah Sistem Terdistribusi

---
**Dibuat dengan ❤️ untuk pembelajaran Sistem Terdistribusi**
