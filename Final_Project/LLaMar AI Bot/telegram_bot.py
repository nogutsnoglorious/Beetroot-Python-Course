from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update, ReplyKeyboardMarkup
import logging
import os
import aiohttp
from datetime import datetime
import subprocess
import asyncio
import json
import random
from transformers import GPT2Tokenizer

# Load environment variables (assuming BOT_TOKEN is stored in a .env file)
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Define the directory to save audio files
SAVE_DIR = "saved_audio"

chat_date = datetime.now().strftime("%Y-%m-%d")

# Create the save directory if it doesn't exist
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Configure logging
logging.basicConfig(filename="bot_log.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

async def get_user_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
  """
  Retrieves the user's nickname or ID depending on availability.
  """
  user = update.effective_user
  if user.username:
    return user.username  # Use nickname if available
  else:
    return str(user.id)     # Fallback to user ID

async def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Greets the user and introduces the bot."""
    # Record default voice choice (male) for the user in the JSON file if not already recorded
    user_info = await get_user_info(update, context)
    user_voice_choice_file = "users_voice_choice.json"
    if os.path.exists(user_voice_choice_file):
        with open(user_voice_choice_file, "r") as file:
            user_voice_choice_data = json.load(file)
    else:
        user_voice_choice_data = {}

    # Check if the user already has a voice choice recorded
    if user_info not in user_voice_choice_data:
        # Send the default picture (male.png)
        default_picture_path = "avatars/male.png"
        if os.path.exists(default_picture_path):
            with open(default_picture_path, 'rb') as photo:
                await context.bot.send_photo(chat_id=update.message.chat_id, photo=photo)
        else:
            await update.message.reply_text("Default picture not found.")

        user_voice_choice_data[user_info] = "male"  # Default voice choice is male

        # Write the updated data back to the JSON file
        with open(user_voice_choice_file, "w") as file:
            json.dump(user_voice_choice_data, file, indent=4)

                # Modify the default greeting to include information about default male voice
        await update.message.reply_text(
            "Hi! I'm your audio message saving bot. Send me an audio message to have it saved. "
            "By default, your voice will be saved as male. You can change this later using the /change_voice command."
        )
    else:
        # User already has a voice choice recorded, send a customized message
        current_voice_choice = user_voice_choice_data[user_info]
        await update.message.reply_text(f"Welcome back! Your current voice choice is {current_voice_choice}.")

async def send_audio_file_to_user(update: Update, context: ContextTypes.DEFAULT_TYPE, file_path: str) -> None:
    """Sends the specified audio file to the user."""
    await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(file_path, 'rb'))

async def save_user_voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Downloads and saves received voice messages from the user in the user's directory.
    Converts the voice message from OGG to WAV format.
    """
    # Get user info
    user_info = await get_user_info(update, context)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_name = f"{user_info}-{timestamp}"

    # Create directories for user messages if they don't exist
    user_dir = f"saved_audio/{user_info}/{chat_date}/user"
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)

    # Create directories for chatbot messages if they don't exist
    chatbot_dir = f"saved_audio/{user_info}/{chat_date}/chatbot"
    if not os.path.exists(chatbot_dir):
        os.makedirs(chatbot_dir)

    voice_file_id = update.message.voice.file_id
    ogg_user_file_path = f"{user_dir}/{file_name}.ogg"
    wav_user_file_path = f"{user_dir}/{file_name}.wav"

    # Use aiohttp to download the voice file asynchronously
    async with aiohttp.ClientSession() as session:
        file_info = await context.bot.get_file(voice_file_id)
        async with session.get(file_info.file_path) as resp:
            if resp.status == 200:
                # Save the received .ogg file
                with open(ogg_user_file_path, 'wb') as fd:
                    while True:
                        chunk = await resp.content.read(1024)
                        if not chunk:
                            break
                        fd.write(chunk)

                # Convert the received .ogg file to .wav format
                try:
                    subprocess.run(['ffmpeg', '-i', ogg_user_file_path, wav_user_file_path], check=True)
                    logging.info(f"Voice message saved to: {wav_user_file_path}")

                    # Delete the original .ogg file
                    os.remove(ogg_user_file_path)
                    logging.info(f"Original .ogg file deleted: {ogg_user_file_path}")

                    # Store the path to the saved .wav file in a JSON file
                    path_to_saved_wav_file = wav_user_file_path.replace("/", "\\")

                    # Load existing JSON data if the file exists
                    json_data = {}
                    json_file_path = "voice_to_process.json"
                    if os.path.exists(json_file_path):
                        with open(json_file_path, "r") as json_file:
                            json_data = json.load(json_file)

                    # Update the JSON data with the new entry
                    json_data[file_name] = path_to_saved_wav_file

                    # Write the updated JSON data back to the file, appending the new entry
                    with open(json_file_path, "w") as json_file:
                        json.dump(json_data, json_file, indent=4)  # Optionally, you can use indent for pretty printing

                    logging.info(f"Path to saved .wav file stored: {path_to_saved_wav_file}")

                    # Write the new entry to the voice_to_process.json file
                    voice_to_process_data = {file_name: path_to_saved_wav_file}
                    voice_to_process_file_path = "voice_to_process.json"
                    with open(voice_to_process_file_path, "w") as voice_to_process_file:
                        json.dump(voice_to_process_data, voice_to_process_file, indent=4)

                    logging.info(f"New entry written to voice_to_process.json: {voice_to_process_data}")

                    # Update chat_history.json with the new entry
                    chat_history_file_path = "chat_history.json"
                    chat_history_data = {}
                    if os.path.exists(chat_history_file_path):
                        with open(chat_history_file_path, "r") as chat_history_file:
                            chat_history_data = json.load(chat_history_file)

                    # Append the new entry to the chat history
                    chat_history_data[file_name] = path_to_saved_wav_file

                    # Write the updated chat history back to the file
                    with open(chat_history_file_path, "w") as chat_history_file:
                        json.dump(chat_history_data, chat_history_file, indent=4)

                    logging.info(f"New entry written to chat_history.json: {chat_history_data}")


                    # Start checking for new .wav files in chatbot directory
                    while True:
                        specific_wav_file = f"chatbot_to_{file_name}.wav"
                        specific_wav_file_path = os.path.join(chatbot_dir, specific_wav_file)
                        if os.path.exists(specific_wav_file_path):
                            # Wait to ensure the file is no longer being written to
                            initial_size = os.path.getsize(specific_wav_file_path)
                            await asyncio.sleep(1)  # Wait for a second before checking the size again
                            if os.path.getsize(specific_wav_file_path) == initial_size:
                                # File size has not changed, proceed with conversion and sending
                                ogg_output_path = os.path.join(chatbot_dir, f"chatbot_to_{file_name}.mp3")
                                subprocess.run(['ffmpeg', '-i', specific_wav_file_path, ogg_output_path], check=True)
                                logging.info(f"Converted .ogg file: {ogg_output_path}")

                                # Send the converted .ogg file back to user
                                with open(ogg_output_path, 'rb') as ogg_file:
                                    await context.bot.send_voice(update.message.chat_id, ogg_file)

                                logging.info(f"Converted .ogg file sent back to user: {ogg_output_path}")

                                # Clean up the files
                                # os.remove(ogg_output_path)
                                os.remove(specific_wav_file_path)
                                break  # Exit loop once file is detected and sent
                        await asyncio.sleep(1)  # Check every 1 second for new files

                except subprocess.CalledProcessError as e:
                    logging.error(f"Error occurred during conversion: {e}")

            else:
                logging.error(f"Failed to download the voice message: {voice_file_id}")

async def change_voice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Allows the user to change their preferred voice."""
    # user_info = await get_user_info(update, context)
    keyboard = [["Male", "Female"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

    await update.message.reply_text(
        "Please choose your preferred voice:",
        reply_markup=reply_markup
    )

# Store the choice in the database after the user selects it
async def store_voice_choice(update, context):
    user_info = await get_user_info(update, context)
    user_choice = update.message.text.lower()  # Extract the choice
    if user_choice in ['male', 'female']:
        # Create or load the JSON file
        user_voice_choice_file = "users_voice_choice.json"
        if os.path.exists(user_voice_choice_file):
            with open(user_voice_choice_file, "r") as file:
                user_voice_choice_data = json.load(file)
        else:
            user_voice_choice_data = {}

        # Update the user's choice
        user_voice_choice_data[user_info] = user_choice

        # Write the updated data back to the JSON file
        with open(user_voice_choice_file, "w") as file:
            json.dump(user_voice_choice_data, file, indent=4)

        # Send picture before sending the voice message
        avatars_folder = "avatars"
        if os.path.exists(avatars_folder):
            # Assuming the picture has the same name as the user's choice with a .jpg extension
            picture_path = os.path.join(avatars_folder, f"{user_choice}.png")
            if os.path.exists(picture_path):
                with open(picture_path, 'rb') as photo:
                    await context.bot.send_photo(chat_id=update.message.chat_id, photo=photo)
            else:
                await update.message.reply_text("No picture found for the selected choice.")
        else:
            await update.message.reply_text("Avatars folder not found.")

        await update.message.reply_text(f"Your voice choice has been set to {user_choice}.")
    else:
        await update.message.reply_text("Invalid choice. Please choose between 'male' and 'female'.")

# Define a function to handle the "fact" command
async def get_random_fact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random fact to the user."""
    try:
        # Load the JSON file containing facts
        with open("interesting_facts.json", "r") as file:
            facts = json.load(file)
        
        # Get a random fact
        random_fact = random.choice(list(facts.values()))
        
        # Send the random fact to the user
        await update.message.reply_text(random_fact)
    except Exception as e:
        logging.error(f"Error retrieving random fact: {e}")

# Define a function to handle the "meme" command
async def send_random_meme(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random meme image to the user."""
    try:
        memes_folder = "memes"
        # Check if memes folder exists
        if os.path.exists(memes_folder) and os.path.isdir(memes_folder):
            # List all files in the memes folder
            meme_files = [f for f in os.listdir(memes_folder) if os.path.isfile(os.path.join(memes_folder, f))]
            # Select a random meme file
            random_meme = random.choice(meme_files)
            # Get the file path
            meme_path = os.path.join(memes_folder, random_meme)
            # Send the meme image to the user
            with open(meme_path, 'rb') as photo:
                await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo)
        else:
            await update.message.reply_text("No memes found.")
    except Exception as e:
        logging.error(f"Error sending meme: {e}")

# Define a function to handle the "stats" command
async def get_chat_stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Calculate and send chat statistics to the user."""
    """Calculate and send chat statistics to the user."""
    try:
        user_info = await get_user_info(update, context)
        conversation_log_path = f"saved_audio/{user_info}/conversation_log.txt"
        
        # Check if the conversation log file exists
        if os.path.exists(conversation_log_path):
            # Read the conversation log file with UTF-8 encoding
            with open(conversation_log_path, "r", encoding="utf-8") as file:
                conversation_lines = file.readlines()
            
            # Concatenate all lines from the conversation log
            all_text = "".join(line.strip()[6:].strip() if line.startswith(("You:", "Chatbot:")) else line.strip() for line in conversation_lines)
            
            # Tokenize the text
            tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
            tokens = tokenizer.tokenize(all_text)
            
            # Calculate the number of words
            num_words = len(all_text.split())
            
            # Calculate the number of tokens
            num_tokens = len(tokens)

            # Calculate the amount of saved money
            saved_money = num_tokens/1000*0.002
            
            # Send the statistics to the user
            await update.message.reply_text(f"Number of words in the conversation: {num_words}\
                                            \nNumber of tokens: {num_tokens}\
                                            \nTotal amount of saved money: ${round(saved_money, 3)}")
        else:
            await update.message.reply_text("Conversation log file not found.")
    except Exception as e:
        logging.error(f"Error calculating chat statistics: {e}")

# Initialize the application
application = Application.builder().token(BOT_TOKEN).build()

# Add command handlers
application.add_handler(CommandHandler("start", greet_user))
application.add_handler(MessageHandler(filters.VOICE, save_user_voice_message))
application.add_handler(CommandHandler("change_voice", change_voice))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, store_voice_choice))
application.add_handler(CommandHandler("fact", get_random_fact))
application.add_handler(CommandHandler("meme", send_random_meme))
application.add_handler(CommandHandler("stats", get_chat_stats))  # New command for chat statistics


# Run the bot
if __name__ == "__main__":
    application.run_polling()
