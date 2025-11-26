from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import json

app = Flask(__name__)

# API Endpoints (menggunakan API publik gratis)
WEATHER_API_URL = "https://api.bmkg.go.id/publik/prakiraan-cuaca"
QUOTE_API_URL = "https://api.quotable.io/random"
CURRENCY_API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
NEWS_API_URL = "https://berita-indo-api-next.vercel.app/api/cnn-news/teknologi"

@app.route('/')
def index():
    """Halaman utama dashboard"""
    return render_template('index.html')

@app.route('/api/weather', methods=['GET'])
def get_weather():
    """
    Endpoint untuk mendapatkan data cuaca
    Integrasi dengan BMKG API (Badan Meteorologi, Klimatologi, dan Geofisika)
    """
    try:
        # Kode wilayah BMKG untuk Karuwisi Utara, Makassar
        adm4_code = request.args.get('adm4', '73.71.09.1009')
        
        params = {
            'adm4': adm4_code
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(WEATHER_API_URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Ekstrak data cuaca terkini (data pertama dari array)
        current_weather = None
        if data.get('data') and len(data['data']) > 0:
            cuaca_data = data['data'][0].get('cuaca', [])
            if cuaca_data and len(cuaca_data) > 0 and len(cuaca_data[0]) > 0:
                current_weather = cuaca_data[0][0]
        
        return jsonify({
            'status': 'success',
            'data': {
                'lokasi': data.get('lokasi', {}),
                'current_weather': current_weather,
                'raw_data': data
            },
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
    Endpoint berita teknologi Indonesia menggunakan CNN Indonesia API.
    Format data: JSON (Berita Bahasa Indonesia)
    """
    try:
        # 1. Request ke URL API berita teknologi Indonesia
        response = requests.get(NEWS_API_URL, timeout=10)
        response.raise_for_status()
        
        # 2. Parse sebagai JSON
        data = response.json()
        
        # 3. Ambil list artikel (default kosong jika tidak ada)
        raw_articles = data.get('data', [])[:5]
        
        formatted_articles = []
        
        # 4. Loop dan format data agar sesuai dengan Frontend JS
        for item in raw_articles:
            formatted_articles.append({
                'title': item.get('title'),
                'description': item.get('contentSnippet'),
                'url': item.get('link'),
                'publishedAt': item.get('isoDate'),
                'image': item.get('image', {}).get('small') if item.get('image') else None
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
