import time
import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from openai import OpenAI
from text_to_speech import male_voice, female_voice
from speech_to_text import Listen2User

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

def chat_with_llm(prompt, system_message):
    response = client.chat.completions.create(
        model="local-model",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

class JSONHandler(FileSystemEventHandler):
    processed = False  # Add a flag to track whether the file has been processed

    def on_modified(self, event):
        if not self.processed and event.src_path.endswith("voice_to_process.json"):
            # print("Detected modification in voice_to_process.json")
            self.process_json()
            self.processed = True  # Set the flag to True after processing

    def process_json(self):
        with open("voice_to_process.json", 'r') as file:
            data = file.read().strip()
            if data:
                try:
                    json_data = json.loads(data)
                    if json_data:
                        latest_key = max(json_data.keys(), key=lambda x: x.lower())
                        latest_value = json_data[latest_key]
                        username = latest_key[:-16]  # Extracting username from the key
                        return username, latest_value
                except json.JSONDecodeError:
                    print("Error: Invalid JSON data in voice_to_process.json")
            return None, None  # Return None if the file is empty or contains invalid JSON

def get_voice_choice(username):
    with open("users_voice_choice.json", 'r') as file:
        data = json.load(file)
        return data.get(username)
    
def log_conversation(username, user_input, response):
    user_folder = os.path.join("saved_audio", username)
    os.makedirs(user_folder, exist_ok=True)
    log_file_path = os.path.join(user_folder, "conversation_log.txt")
    
    with open(log_file_path, 'a', encoding='utf-8') as log_file:  # Specify encoding='utf-8'
        log_file.write(f"You: {user_input}\n")
        log_file.write(f"Chatbot: {response}\n")

def main():
    # Define the system message with the placeholder for the username
    system_message = (
        "Be nice and friendly to user. "
        "All your responses should be brief and short. "
        "You, the assistant, are an expert in all general topics. "
        "Your primary job and role as the ASSISTANT is to help user give detailed, but brief answers to his questions. "
        "Be concise and specific in responses. Avoid unnecessary details. Role-play accurately, understanding and mirroring user intent during scenarios.\n"
        "Emphasize honesty, candor, and precision. Avoid speculation except when explicitly prompted to. "
    )

    observer = Observer()
    observer.schedule(JSONHandler(), path=".")
    observer.start()

    try:
        while True:
            time.sleep(1)
            username, latest_value = JSONHandler().process_json()
            if username is not None and latest_value is not None:
                voice_choice = get_voice_choice(username)
                
                user_input = Listen2User(latest_value)
                if user_input.lower() in ["quit", "exit", "bye"]:
                    break
                
                print(f"You: {user_input}")  # Print user input
                response = chat_with_llm(user_input, system_message)
                print(f"Chatbot: {response}")
                
                log_conversation(username, user_input, response)

                if voice_choice == "male":
                    male_voice(response, latest_value)
                elif voice_choice == "female":
                    female_voice(response, latest_value)
                # Clear the file
                with open("voice_to_process.json", 'w') as file:
                    file.write("{}")
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
