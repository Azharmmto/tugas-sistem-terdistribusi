from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import json
import random
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

app = Flask(__name__)

# API Endpoints (menggunakan API publik gratis)
WEATHER_API_URL = "https://api.bmkg.go.id/publik/prakiraan-cuaca"
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
    Menampilkan 3 berita random dari total berita
    """
    try:
        # 1. Request ke URL API berita teknologi Indonesia
        response = requests.get(NEWS_API_URL, timeout=10)
        response.raise_for_status()
        
        # 2. Parse sebagai JSON
        data = response.json()
        
        # 3. Ambil semua artikel
        all_articles = data.get('data', [])
        
        # 4. Pilih 3 berita secara random
        if len(all_articles) >= 3:
            raw_articles = random.sample(all_articles, 3)
        else:
            raw_articles = all_articles
        
        formatted_articles = []
        
        # 5. Loop dan format data agar sesuai dengan Frontend JS
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
        'service': 'InfoHub Dashboard',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/send-briefing', methods=['POST'])
def send_briefing():
    """
    Endpoint untuk mengirim Daily Briefing via Telegram
    Berisi: Cuaca hari ini, Kurs IDR/USD, dan 3 berita teratas
    """
    try:
        data = request.get_json()
        telegram_id = data.get('telegram_id')
        
        if not telegram_id:
            return jsonify({
                'status': 'error',
                'message': 'Telegram ID diperlukan'
            }), 400
        
        # Validasi telegram_id adalah angka
        try:
            telegram_id = str(telegram_id).strip()
            int(telegram_id)  # Test if it's a valid number
        except ValueError:
            return jsonify({
                'status': 'error',
                'message': 'Telegram ID harus berupa angka'
            }), 400
        
        # 1. Ambil data cuaca
        weather_data = get_weather_data()
        
        # 2. Ambil data currency
        currency_data = get_currency_data()
        
        # 3. Ambil 3 berita teratas
        news_data = get_news_data(3)
        
        # 4. Buat pesan Telegram
        message = create_telegram_message(weather_data, currency_data, news_data)
        
        # 5. Kirim via Telegram
        result = send_telegram_message(telegram_id, message)
        
        if result['success']:
            return jsonify({
                'status': 'success',
                'message': f'Daily briefing berhasil dikirim ke Telegram ID: {telegram_id}'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': result['error']
            }), 500
            
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

def get_weather_data():
    """Helper function untuk mengambil data cuaca"""
    try:
        url = WEATHER_API_URL
        params = {'adm4': '73.71.09.1009'}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        current_weather = None
        if data.get('data') and len(data['data']) > 0:
            cuaca_data = data['data'][0].get('cuaca', [])
            if cuaca_data and len(cuaca_data) > 0 and len(cuaca_data[0]) > 0:
                current_weather = cuaca_data[0][0]
        
        return {
            'lokasi': data.get('lokasi', {}),
            'current_weather': current_weather
        }
    except:
        return None

def get_currency_data():
    """Helper function untuk mengambil data currency"""
    try:
        response = requests.get(CURRENCY_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        rates = data.get('rates', {})
        return {
            'base': data.get('base'),
            'idr': rates.get('IDR', 0)
        }
    except:
        return None

def get_news_data(limit=3):
    """Helper function untuk mengambil berita"""
    try:
        response = requests.get(NEWS_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        all_articles = data.get('data', [])
        
        if len(all_articles) >= limit:
            articles = random.sample(all_articles, limit)
        else:
            articles = all_articles[:limit]
        
        return articles
    except:
        return []

def escape_markdown_v2(text):
    """Helper untuk escape karakter MarkdownV2"""
    # Karakter yang perlu di-escape di MarkdownV2
    special_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in special_chars:
        text = text.replace(char, f'\\{char}')
    return text

def create_telegram_message(weather_data, currency_data, news_data):
    """Membuat pesan Telegram untuk daily briefing"""
    message = "📊 *Laporan Harian*\n"
    message += f"📅 Tanggal: {escape_markdown_v2(datetime.now().strftime('%d %B %Y'))}\n"
    message += "━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    
    # Cuaca
    if weather_data and weather_data.get('current_weather'):
        weather = weather_data['current_weather']
        lokasi = weather_data.get('lokasi', {})
        
        # Get weather emoji
        weather_emoji = get_weather_emoji_simple(weather.get('weather_desc', ''))
        
        message += f"🌤️ *Cuaca Hari Ini* {weather_emoji}\n"
        message += f"├ Kondisi: *{escape_markdown_v2(str(weather.get('weather_desc', 'N/A')))}*\n"
        message += f"├ Suhu: *{escape_markdown_v2(str(weather.get('t', 'N/A')))}°C*\n"
        message += f"├ Lokasi: {escape_markdown_v2(lokasi.get('kotkab', 'N/A'))}, {escape_markdown_v2(lokasi.get('provinsi', 'N/A'))}\n"
        message += f"├ Angin: {escape_markdown_v2(str(weather.get('ws', 'N/A')))} km/h \\({escape_markdown_v2(str(weather.get('wd', 'N/A')))}\\)\n"
        message += f"└ Kelembaban: {escape_markdown_v2(str(weather.get('hu', 'N/A')))}%\n\n"
    
    # Currency
    if currency_data:
        message += "💱 *Kurs Rupiah Hari Ini*\n"
        # Format number dan escape
        idr_formatted = f"{currency_data.get('idr', 0):,.2f}".replace(',', '\\,').replace('.', '\\.')
        message += f"└ 1 USD \\= Rp {idr_formatted}\n\n"
    
    # News
    if news_data:
        message += "📰 *Berita Teknologi Teratas*\n\n"
        for i, article in enumerate(news_data[:3], 1):
            title = article.get('title', 'N/A')
            # Escape markdown special characters
            title_escaped = escape_markdown_v2(title)
            message += f"{i}\\. {title_escaped}\n"
            link = article.get('link', '#')
            message += f"   [Baca selengkapnya]({link})\n\n"
    
    message += "━━━━━━━━━━━━━━━━━━━━━━━\n"
    message += "_Tugas Akhir Sistem Terdistribusi_\n"
    
    return message

def get_weather_emoji_simple(condition):
    """Helper untuk mendapatkan emoji cuaca sederhana"""
    weather = condition.lower()
    if 'cerah' in weather and 'berawan' not in weather:
        return '☀️'
    elif 'cerah berawan' in weather or 'cerah-berawan' in weather:
        return '⛅'
    elif 'berawan' in weather:
        return '☁️'
    elif 'hujan petir' in weather or 'hujan lebat' in weather:
        return '⛈️'
    elif 'hujan' in weather:
        return '🌧️'
    elif 'petir' in weather or 'badai' in weather:
        return '⚡'
    elif 'kabut' in weather:
        return '🌫️'
    else:
        return '🌤️'

def send_telegram_message(chat_id, message):
    """
    Mengirim pesan ke Telegram menggunakan Bot API
    """
    try:
        # Ambil bot token dari environment variables
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        
        if not bot_token:
            print("ERROR: Telegram Bot Token not configured!")
            print("Please set TELEGRAM_BOT_TOKEN in .env file")
            return {
                'success': False,
                'error': 'Bot Token tidak dikonfigurasi. Periksa file .env'
            }
        
        # Telegram API URL
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        
        # Payload
        payload = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'MarkdownV2',
            'disable_web_page_preview': True
        }
        
        print(f"Mengirim pesan Telegram ke chat_id: {chat_id}...")
        
        # Send request
        response = requests.post(url, json=payload, timeout=10)
        
        # Parse response
        result = response.json()
        
        if result.get('ok'):
            print(f"✓ Pesan berhasil dikirim ke Telegram chat_id: {chat_id}")
            return {
                'success': True,
                'error': None
            }
        else:
            error_desc = result.get('description', 'Unknown error')
            print(f"ERROR: Telegram API error: {error_desc}")
            
            # Berikan pesan error yang lebih informatif
            if 'chat not found' in error_desc.lower():
                return {
                    'success': False,
                    'error': 'Telegram ID tidak ditemukan. Pastikan Anda sudah memulai chat dengan bot @notifst_bot terlebih dahulu.'
                }
            elif 'bot was blocked' in error_desc.lower():
                return {
                    'success': False,
                    'error': 'Bot telah diblokir oleh user. Silakan unblock bot @notifst_bot di Telegram.'
                }
            else:
                return {
                    'success': False,
                    'error': f'Telegram API Error: {error_desc}'
                }
            
    except requests.exceptions.Timeout:
        print(f"ERROR: Request timeout")
        return {
            'success': False,
            'error': 'Timeout menghubungi Telegram API. Coba lagi.'
        }
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Gagal mengirim pesan Telegram: {e}")
        return {
            'success': False,
            'error': f'Gagal menghubungi Telegram API: {str(e)}'
        }
    except Exception as e:
        print(f"ERROR: {e}")
        return {
            'success': False,
            'error': f'Error tidak terduga: {str(e)}'
        }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
