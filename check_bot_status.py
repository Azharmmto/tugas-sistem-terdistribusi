#!/usr/bin/env python3
"""
Quick check status Telegram Bot
Jalankan: python3 check_bot_status.py
"""
import os
import requests

print("\n🤖 CHECKING TELEGRAM BOT STATUS...\n")
print("=" * 60)

# Load .env manually
env_vars = {}
try:
    with open('.env', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                env_vars[key] = value
                os.environ[key] = value
except FileNotFoundError:
    print("❌ File .env tidak ditemukan!")
    exit(1)

# Get token
bot_token = env_vars.get('TELEGRAM_BOT_TOKEN')

if not bot_token:
    print("❌ TELEGRAM_BOT_TOKEN tidak ada di .env")
    exit(1)

print(f"✓ Bot Token ditemukan")
print(f"  Token: {bot_token[:15]}...{bot_token[-5:]}")

# Check bot
url = f"https://api.telegram.org/bot{bot_token}/getMe"

try:
    response = requests.get(url, timeout=10)
    result = response.json()
    
    if result.get('ok'):
        bot_info = result['result']
        print(f"\n✅ BOT AKTIF!")
        print(f"  Bot ID: {bot_info['id']}")
        print(f"  Bot Name: {bot_info['first_name']}")
        print(f"  Bot Username: @{bot_info['username']}")
        print(f"  Can Join Groups: {bot_info.get('can_join_groups', 'N/A')}")
        
        print(f"\n📱 UNTUK MENGGUNAKAN BOT:")
        print(f"  1. Buka Telegram")
        print(f"  2. Cari: @{bot_info['username']}")
        print(f"  3. Klik 'Start'")
        print(f"  4. Dapatkan ID dari @userinfobot")
        print(f"  5. Gunakan ID di website")
        
    else:
        print(f"\n❌ BOT ERROR!")
        print(f"  Error: {result.get('description', 'Unknown')}")
        print(f"  \n⚠️  Periksa Bot Token di .env")
        
except requests.exceptions.Timeout:
    print(f"\n❌ TIMEOUT!")
    print(f"  Tidak bisa terhubung ke Telegram API")
    print(f"  Periksa koneksi internet")
    
except Exception as e:
    print(f"\n❌ ERROR!")
    print(f"  {e}")

print("=" * 60)
print()
