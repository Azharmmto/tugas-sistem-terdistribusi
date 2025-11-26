from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import json

app = Flask(__name__)

# API Endpoints (menggunakan API publik gratis)
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"
QUOTE_API_URL = "https://api.quotable.io/random"
CURRENCY_API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
NEWS_API_URL = "https://saurav.tech/NewsAPI/top-headlines/category/technology/us.json"

@app.route('/')
def index():
    """Halaman utama dashboard"""
    return render_template('index.html')

@app.route('/api/weather', methods=['GET'])
def get_weather():
    """
    Endpoint untuk mendapatkan data cuaca
    Integrasi dengan Open-Meteo API (gratis, tanpa key)
    """
    try:
        # --- BAGIAN YANG DIUBAH ---
        # Default diganti ke koordinat Makassar
        latitude = request.args.get('lat', '-5.1477')  
        longitude = request.args.get('lon', '119.4327')
        # --------------------------
        
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'current_weather': 'true',
            # Timezone sudah benar 'Asia/Makassar' (WITA)
            'timezone': 'Asia/Makassar' 
        }
        
        response = requests.get(WEATHER_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        return jsonify({
            'status': 'success',
            'data': data,
            'timestamp': datetime.now().isoformat()
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/currency', methods=['GET'])
def get_currency():
    """
    Endpoint untuk mendapatkan nilai tukar mata uang
    Integrasi dengan Exchange Rate API
    """
    try:
        response = requests.get(CURRENCY_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Filter beberapa mata uang populer
        rates = data.get('rates', {})
        filtered_rates = {
            'IDR': rates.get('IDR'),
            'EUR': rates.get('EUR'),
            'GBP': rates.get('GBP'),
            'JPY': rates.get('JPY'),
            'CNY': rates.get('CNY')
        }
        
        return jsonify({
            'status': 'success',
            'data': {
                'base': data.get('base'),
                'date': data.get('date'),
                'rates': filtered_rates
            },
            'timestamp': datetime.now().isoformat()
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/news', methods=['GET'])
def get_news():
    """
    Endpoint berita teknologi menggunakan Saurav.tech NewsAPI Mirror.
    Format data: JSON (Berita Bahasa Inggris - US)
    """
    try:
        # 1. Request ke URL API
        response = requests.get(NEWS_API_URL, timeout=10)
        response.raise_for_status()
        
        # 2. Parse sebagai JSON (Bukan XML)
        data = response.json()
        
        # 3. Ambil list artikel (default kosong jika tidak ada)
        raw_articles = data.get('articles', [])[:5]
        
        formatted_articles = []
        
        # 4. Loop dan format data agar sesuai dengan Frontend JS
        for item in raw_articles:
            # Filter: Kadang ada berita yang dihapus/error dengan judul "[Removed]"
            if item.get('title') == '[Removed]':
                continue
                
            formatted_articles.append({
                'title': item.get('title'),
                'description': item.get('description'),
                'url': item.get('url'),
                'publishedAt': item.get('publishedAt'),
                # API ini menggunakan key 'urlToImage', kita ubah jadi 'image' agar JS paham
                'image': item.get('urlToImage') 
            })
            
        return jsonify({
            'status': 'success',
            'data': {
                'total': len(formatted_articles),
                'articles': formatted_articles
            },
            'timestamp': datetime.now().isoformat()
        })

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e),
            'data': {'articles': []}
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint untuk health check sistem"""
    return jsonify({
        'status': 'healthy',
        'service': 'Distributed Systems Dashboard',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
