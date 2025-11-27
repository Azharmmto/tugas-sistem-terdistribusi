import os
from dotenv import load_dotenv

# 1. Memuat isi file .env ke dalam sistem
load_dotenv()

# 2. Mengambil token
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Cek apakah token berhasil dimuat (Hanya untuk testing awal)
if TOKEN:
    print("Token berhasil dimuat!")
else:
    print("Token tidak ditemukan. Cek file .env kamu.")

# Selanjutnya, gunakan variabel TOKEN ini untuk bot kamu
# Contoh: application = ApplicationBuilder().token(TOKEN).build()