from gtts import gTTS
import pyttsx3
import os

def female_voice(input_text, filepath):

    # Generate the audio file
    myobj = gTTS(text=input_text, lang='en', slow=False)
    
    # Extract filename without extension
    filename = os.path.splitext(os.path.basename(filepath))[0]
    
    # Add "chatbot_to_" as a prefix
    output_filename = f"chatbot_to_{filename}.wav"

    # Replace backslashes with forward slashes
    output_dir = os.path.dirname(filepath).replace("\\", "/").replace("user", "chatbot")
    
    # Make directories if they don't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Construct the output filepath
    output_filepath = os.path.join(output_dir, output_filename)

    # Save the audio file
    myobj.save(output_filepath)

def male_voice(input_text, filepath):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)

    # Extract filename without extension
    filename = os.path.splitext(os.path.basename(filepath))[0]

    # Add "chatbot_to_" as a prefix
    output_filename = f"chatbot_to_{filename}.wav"

    # Replace backslashes with forward slashes
    output_dir = os.path.dirname(filepath).replace("\\", "/").replace("user", "chatbot")

    # Make directories if they don't exist
    os.makedirs(output_dir, exist_ok=True)

    # Construct the output filepath
    output_filepath = os.path.join(output_dir, output_filename)

    # Convert text to speech and save to file
    engine.save_to_file(input_text, output_filepath)
    engine.runAndWait()