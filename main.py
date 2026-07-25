import speech_recognition as sr
import os
import time

def speak(text):
    print(f"Jarvis: {text}")
    os.system(f'termux-tts-speak -l si-LK "{text}"')

def listen():
    print("සවන් දෙමින් පවතී (Listening for 5 seconds)...")
    os.system("termux-microphone-record -f voice.wav -l 5 > /dev/null 2>&1")
    time.sleep(5)
    os.system("termux-microphone-record -q > /dev/null 2>&1")

    r = sr.Recognizer()
    try:
        with sr.AudioFile("voice.wav") as source:
            audio = r.record(source)
            print("තේරුම් ගනිමින් පවතී (Recognizing)...")
            query = r.recognize_google(audio, language='si-LK')
            print(f"You said: {query}")
            return query.lower()
    except Exception as e:
        return ""

if __name__ == "__main__":
    speak(" දිනිත්! නෝවා ආවා. මොනවා හරි වෙන්න ඕනිද මගෙන්?")
    
    while True:
        query = listen()
        
        if "හෙලෝ" in query or "කොහොමද" in query:
            speak("මම හොඳින් ඉන්නවා, ඔබට කොහොමද?")
        elif "නම මොකක්ද" in query:
            speak("මගේ නම ජාවීස්.")
        elif "නවත්වන්න" in query or "ගොස් එන්නම්" in query:
            speak("සුබ දවසක්! මම නවතිනවා.")
            break