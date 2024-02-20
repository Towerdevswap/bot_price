from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# Fungsi untuk mendapatkan informasi token dari API
def get_token_info(api_url):
    response = requests.get(api_url)
    data = response.json()

    if 'data' in data and 'attributes' in data['data']:
        attributes = data['data']['attributes']
        token_name = attributes['name']
        token_symbol = attributes['symbol']
        price_usd = attributes['price_usd']

        return f"Token: {token_name} ({token_symbol}) - Price USD: {price_usd}"
    else:
        return "Data tidak valid atau tidak lengkap."

# Fungsi yang akan dijalankan ketika perintah /price diterima
def price(update: Update, context: CallbackContext) -> None:
    api_url = "https://api.geckoterminal.com/api/v2/networks/bitgert/tokens/0x43fd2fafa5cfccb66d03061b59a25f02ec194d1b"
    response_message = get_token_info(api_url)
    update.message.reply_text(response_message)

def main() -> None:
    # Token bot Telegram, dapatkan dari BotFather
    updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    # Menambahkan handler untuk perintah /price
    dispatcher.add_handler(CommandHandler('price', price))

    # Memulai polling untuk menerima pesan dari pengguna
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
