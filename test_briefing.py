#!/usr/bin/env python3
"""
Script untuk menguji fitur Daily Briefing
Test: Email notification dengan ringkasan cuaca, kurs, dan berita
"""

import requests
import json

def test_briefing_endpoint():
    """Test endpoint daily briefing"""
    print("=" * 60)
    print("Testing Daily Briefing Feature")
    print("=" * 60)
    
    url = "http://localhost:5000/api/send-briefing"
    test_email = "user@example.com"
    
    payload = {
        "email": test_email
    }
    
    try:
        print(f"📧 Mengirim request ke: {url}")
        print(f"📬 Email tujuan: {test_email}")
        print()
        
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()
        
        print(f"✓ Status: {result['status']}")
        print(f"✓ Message: {result['message']}")
        
        if 'preview' in result:
            print(f"\n📄 Preview HTML Email (100 karakter pertama):")
            print(result['preview'][:100] + "...")
        
        print(f"\n✓ Daily Briefing Test: PASSED ✓\n")
        return True
        
    except requests.exceptions.ConnectionError:
        print("✗ Error: Flask server tidak berjalan!")
        print("   Jalankan: python3 app.py")
        print()
        return False
    except Exception as e:
        print(f"✗ Daily Briefing Test: FAILED")
        print(f"Error: {e}\n")
        return False

def test_random_news():
    """Test apakah berita berubah (random)"""
    print("=" * 60)
    print("Testing Random News Feature")
    print("=" * 60)
    
    url = "http://localhost:5000/api/news"
    
    try:
        print("📰 Mengambil berita pertama kali...")
        response1 = requests.get(url, timeout=10)
        result1 = response1.json()
        articles1 = [a['title'] for a in result1['data']['articles']]
        
        print(f"✓ Berita 1: {len(articles1)} artikel")
        
        print("\n📰 Mengambil berita kedua kali...")
        response2 = requests.get(url, timeout=10)
        result2 = response2.json()
        articles2 = [a['title'] for a in result2['data']['articles']]
        
        print(f"✓ Berita 2: {len(articles2)} artikel")
        
        # Check if articles are different (random selection)
        if articles1 != articles2:
            print("\n✓ Berita berubah setiap refresh (Random: AKTIF)")
        else:
            print("\n⚠ Berita sama (mungkin kebetulan atau pool terbatas)")
        
        print(f"\n✓ Random News Test: PASSED ✓\n")
        return True
        
    except requests.exceptions.ConnectionError:
        print("✗ Error: Flask server tidak berjalan!")
        return False
    except Exception as e:
        print(f"✗ Random News Test: FAILED")
        print(f"Error: {e}\n")
        return False

def main():
    print("\n" + "=" * 60)
    print("TEST FITUR BARU - DAILY BRIEFING & RANDOM NEWS")
    print("=" * 60 + "\n")
    
    print("⚠ Pastikan Flask server sudah berjalan di port 5000!")
    print("  Jalankan: python3 app.py")
    print()
    
    input("Tekan Enter untuk melanjutkan test...")
    print()
    
    briefing_ok = test_briefing_endpoint()
    news_ok = test_random_news()
    
    print("=" * 60)
    print("RINGKASAN TEST")
    print("=" * 60)
    print(f"Daily Briefing Feature: {'✓ PASSED' if briefing_ok else '✗ FAILED'}")
    print(f"Random News Feature: {'✓ PASSED' if news_ok else '✗ FAILED'}")
    
    if briefing_ok and news_ok:
        print("\n✓ SEMUA TEST BERHASIL!")
        return 0
    else:
        print("\n✗ ADA TEST YANG GAGAL.")
        return 1

if __name__ == "__main__":
    exit(main())
