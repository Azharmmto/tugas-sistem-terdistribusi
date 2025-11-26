#!/usr/bin/env python3
"""
Script untuk menguji API endpoints yang telah diubah
Test: BMKG Weather API dan CNN Indonesia Tech News API
"""

import requests
import json

def test_bmkg_api():
    """Test BMKG Weather API"""
    print("=" * 60)
    print("Testing BMKG Weather API")
    print("=" * 60)
    
    url = "https://api.bmkg.go.id/publik/prakiraan-cuaca"
    params = {'adm4': '73.71.09.1009'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        print(f"✓ API Response: OK")
        print(f"✓ Lokasi: {data['lokasi']['desa']}, {data['lokasi']['kotkab']}")
        
        # Get current weather
        current_weather = data['data'][0]['cuaca'][0][0]
        print(f"✓ Suhu: {current_weather['t']}°C")
        print(f"✓ Kondisi: {current_weather['weather_desc']}")
        print(f"✓ Kelembaban: {current_weather['hu']}%")
        print(f"✓ Kecepatan Angin: {current_weather['ws']} km/h")
        print(f"✓ BMKG API Test: PASSED ✓\n")
        return True
        
    except Exception as e:
        print(f"✗ BMKG API Test: FAILED")
        print(f"Error: {e}\n")
        return False

def test_news_api():
    """Test Indonesian Tech News API"""
    print("=" * 60)
    print("Testing CNN Indonesia Tech News API")
    print("=" * 60)
    
    url = "https://berita-indo-api-next.vercel.app/api/cnn-news/teknologi"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        print(f"✓ API Response: OK")
        print(f"✓ Total Berita: {data['total']}")
        print(f"✓ Berita Pertama:")
        
        first_article = data['data'][0]
        print(f"  - Judul: {first_article['title'][:70]}...")
        print(f"  - Link: {first_article['link'][:50]}...")
        print(f"  - Deskripsi: {first_article['contentSnippet'][:60]}...")
        print(f"✓ Tech News API Test: PASSED ✓\n")
        return True
        
    except Exception as e:
        print(f"✗ Tech News API Test: FAILED")
        print(f"Error: {e}\n")
        return False

def main():
    print("\n" + "=" * 60)
    print("TEST API PERUBAHAN - BMKG & CNN Indonesia")
    print("=" * 60 + "\n")
    
    bmkg_ok = test_bmkg_api()
    news_ok = test_news_api()
    
    print("=" * 60)
    print("RINGKASAN TEST")
    print("=" * 60)
    print(f"BMKG Weather API: {'✓ PASSED' if bmkg_ok else '✗ FAILED'}")
    print(f"Tech News API: {'✓ PASSED' if news_ok else '✗ FAILED'}")
    
    if bmkg_ok and news_ok:
        print("\n✓ SEMUA TEST BERHASIL! API siap digunakan.")
        return 0
    else:
        print("\n✗ ADA TEST YANG GAGAL. Periksa koneksi atau endpoint API.")
        return 1

if __name__ == "__main__":
    exit(main())
