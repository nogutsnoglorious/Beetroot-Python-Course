import speech_recognition as sr

def Listen2User(audio_file_link):
    r = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(audio_file_link) as source:
        audio = r.record(source)  # Read the entire audio file

        try:
            # Use Google to recognize audio
            recognized_text = r.recognize_google(audio)
            recognized_text = recognized_text.lower()
            return recognized_text
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return "Hello"
        except sr.UnknownValueError:
            print("Oops! Could not understand the audio.")
            return "Hello"

if __name__ == "__main__":
    pass
