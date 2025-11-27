#!/usr/bin/env python3
"""
Script untuk testing perbaikan Telegram integration
"""
import os
import sys
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

def test_telegram_bot():
    """Test Bot Token validity"""
    print("=" * 70)
    print("TEST 1: Validasi Bot Token")
    print("=" * 70)
    
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not bot_token:
        print("❌ GAGAL: Bot Token tidak ditemukan di .env")
        return False
    
    print(f"✓ Bot Token ditemukan: {bot_token[:10]}...")
    
    # Test getMe endpoint
    url = f"https://api.telegram.org/bot{bot_token}/getMe"
    
    try:
        response = requests.get(url, timeout=10)
        result = response.json()
        
        if result.get('ok'):
            print(f"✓ Bot aktif!")
            print(f"  - Bot Name: {result['result']['first_name']}")
            print(f"  - Bot Username: @{result['result']['username']}")
            print(f"  - Bot ID: {result['result']['id']}")
            return True
        else:
            print(f"❌ GAGAL: {result.get('description')}")
            return False
    except Exception as e:
        print(f"❌ GAGAL: {e}")
        return False

def test_send_message_invalid_id():
    """Test sending message dengan ID yang belum start chat"""
    print("\n" + "=" * 70)
    print("TEST 2: Test Kirim Pesan dengan ID Invalid")
    print("=" * 70)
    
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    test_chat_id = "123456789"
    test_message = "Test message"
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': test_chat_id,
        'text': test_message
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        result = response.json()
        
        if result.get('ok'):
            print(f"✓ Pesan terkirim (unexpected)")
        else:
            error_desc = result.get('description', 'Unknown error')
            print(f"❌ Expected Error: {error_desc}")
            
            # Check error handling
            if 'chat not found' in error_desc.lower():
                print("✓ Error detection berfungsi dengan baik")
                print("\n💡 SOLUSI:")
                print("   1. Buka Telegram")
                print("   2. Cari bot: @notifst_bot")
                print("   3. Klik 'Start' atau kirim pesan apapun")
                print("   4. Buka @userinfobot untuk mendapatkan ID Anda")
                print("   5. Gunakan ID tersebut di website")
                return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def print_instructions():
    """Print instruksi lengkap"""
    print("\n" + "=" * 70)
    print("CARA MENGGUNAKAN BOT TELEGRAM")
    print("=" * 70)
    print("\nLangkah-langkah:")
    print("1. Buka aplikasi Telegram di HP atau Desktop")
    print("2. Di kotak pencarian, ketik: @notifst_bot")
    print("3. Klik bot yang muncul, lalu klik tombol 'Start'")
    print("4. Bot akan mengirim pesan selamat datang")
    print("\n5. Untuk mendapatkan Telegram ID Anda:")
    print("   - Di Telegram, cari: @userinfobot")
    print("   - Klik 'Start'")
    print("   - Bot akan menampilkan ID Anda (angka)")
    print("\n6. Copy ID tersebut dan masukkan di website InfoHub")
    print("7. Klik tombol 'Kirim' untuk menerima Daily Briefing")
    print("\n" + "=" * 70)
    print("TROUBLESHOOTING")
    print("=" * 70)
    print("\nJika masih error:")
    print("• Pastikan sudah klik 'Start' di bot @notifst_bot")
    print("• Pastikan ID yang dimasukkan adalah angka (bukan username)")
    print("• Pastikan tidak ada spasi di awal/akhir ID")
    print("• Coba hapus chat dengan bot, lalu start ulang")
    print("=" * 70)

if __name__ == "__main__":
    print("\n🔍 TESTING TELEGRAM INTEGRATION\n")
    
    # Test 1: Bot Token
    if not test_telegram_bot():
        print("\n❌ Bot Token tidak valid. Periksa file .env")
        sys.exit(1)
    
    # Test 2: Send message
    test_send_message_invalid_id()
    
    # Print instructions
    print_instructions()
    
    print("\n✅ Testing selesai!")
    print("Bot Token Anda berfungsi dengan baik.")
    print("Ikuti instruksi di atas untuk menggunakan bot.\n")
