from telegram.ext import CommandHandler, Application, ContextTypes
from telegram import ForceReply, Update
from telegram_api_token import tg_api_token
import aiohttp
import requests
from datetime import datetime

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def tokyo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = 'https://www.worldtimeapi.org/api/timezone/Asia/Tokyo.txt'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                text = await response.text()
                # Extract the datetime line
                datetime_line = next((line for line in text.split('\n') if line.startswith('datetime')), None)
                if datetime_line:
                    # Extract the datetime string
                    datetime_str = datetime_line.split(' ', 1)[1]
                    # Parse the datetime string
                    datetime_obj = datetime.fromisoformat(datetime_str)
                    # Format the datetime object to only show the time
                    time_str = datetime_obj.strftime('%H:%M')
                    await update.message.reply_text(f"Current time in Tokyo: {time_str}")
            else:
                await update.message.reply_text("Failed to retrieve time information.")

async def dubai(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Setup the Open-Meteo API parameters for Dubai
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 25.2048,
        "longitude": 55.2708,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
        "forecast_days": 1
    }

    # Make a synchronous call to Open-Meteo API (consider using an async approach for production bots)
    response = requests.get(url, params=params).json()

    # Extract the necessary data (adjust according to the actual response structure)
    weather_data = response['daily']
    max_temp = weather_data['temperature_2m_max'][0]
    min_temp = weather_data['temperature_2m_min'][0]
    date = weather_data['time'][0]

    # Format the message
    weather_message = f"Dubai weather for {date}:\nMax Temperature: {max_temp}°C\nMin Temperature: {min_temp}°C"

    # Send the message
    await update.message.reply_text(weather_message)

async def bitcoin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # CoinGecko API endpoint for fetching simple price information
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }
    
    # Make a synchronous call to CoinGecko API (consider using an async approach for production bots)
    response = requests.get(url, params=params).json()
    
    # Extract the BTC to USD price
    btc_price = response['bitcoin']['usd']
    
    # Format the message
    price_message = f"Current BTC to USD exchange rate: ${btc_price}"
    
    # Send the message
    await update.message.reply_text(price_message)

# def echo(update,context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

application = Application.builder().token(tg_api_token).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("tokyo", tokyo))
application.add_handler(CommandHandler("dubai", dubai))                                       
application.add_handler(CommandHandler("bitcoin", bitcoin))

# message_handler = MessageHandler(filters.text & ~filters.command,echo)

application.run_polling(allowed_updates=Update.ALL_TYPES)
