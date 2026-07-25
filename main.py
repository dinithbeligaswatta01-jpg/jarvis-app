mport speech_recognition as sr
import os

def speak(text):
    print(f"Jarvis: {text}")
    # Termux API එක හරහා සිංහලෙන් කියවීමට si-lk language code එක පාවිච්චි කරයි
    os.system(f'termux-tts-speak -l si-LK "{text}"')

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("සවන් දෙමින් පවතී (Listening)...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        # language='si-LK' යෙදීමෙන් සිංහල වචන තේරුම් ගනී
        command = r.recognize_google(audio, language='si-LK')
        print(f"ඔබ පැවසූ දේ: {command}")
        return command
    except sr.UnknownValueError:
        speak("කණගාටුයි, මට ඔබ කියූ දේ තේරුණේ නැහැ.")
        return ""
    except sr.RequestError:
        speak("ඉන්ටර්නෙට් සම්බන්ධතාවයේ දෝෂයක් තියෙනවා.")
        return ""

if _name_ == "_main_":
    # ඔබ ඉල්ලූ පරිදි ආරම්භක පණිවිඩය වෙනස් කරන ලදී
    speak("හේ දිනිත්! නෝවා ආවා. මොනවා හරි වෙන්න ඕනිද මගෙන්?")
    
    while True:
        query = listen()
        
        # සිංහල විධානයන් (Voice Commands)
        if "හෙලෝ" in query or "කොහොමද" in query:
            speak("මම හොඳින් ඉන්නවා, ඔබට කොහොමද?")
        elif "නම මොකක්ද" in query:
            speak("මගේ නම ජාර්විස්.")
        elif "නවත්වන්න" in query or "ගොස් එන්නම්" in query or "නවත්තන්න" in query:
            speak("සුබ දවසක්! මම නවතිනවා.")
            break
