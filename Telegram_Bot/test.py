from telegram.ext import CommandHandler, Application, ContextTypes
from telegram import ForceReply, Update
from telegram_api_token import tg_api_token
import aiohttp

async def tokyo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = 'https://www.worldtimeapi.org/api/timezone/Asia/Tokyo.txt'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                text = await response.text()
                # Extract the datetime line
                datetime_line = next((line for line in text.split('\n') if line.startswith('datetime')), None)
                if datetime_line:
                    datetime_info = datetime_line.split(' ', 1)[1]
                    await update.message.reply_text(f"Current time in Tokyo: {datetime_info}")
            else:
                await update.message.reply_text("Failed to retrieve time information.")

print(tokyo())