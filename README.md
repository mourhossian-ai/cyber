import speech_recognition as sr
import pyttsx3
import datetime

# ইঞ্জিন ইনিশিয়ালাইজ করা
engine = pyttsx3.init()

def speak(text):
    print(f"Zinia: {text}")
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("শুভ সকাল রনি ভাই!")
    elif hour >= 12 and hour < 18:
        speak("শুভ দুপুর রনি ভাই!")
    else:
        speak("শুভ সন্ধ্যা রনি ভাই!")
    speak("আমি জিনিয়া, আপনার ভয়েস অ্যাসিস্ট্যান্ট। বলুন আপনাকে কীভাবে সাহায্য করতে পারি?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='bn-BD')
        print(f"User said: {query}\n")
    except Exception as e:
        print("আবার বলুন প্লিজ...")
        return "None"
    return query

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        if 'time' in query or'সময়' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"এখন সময় হলো {strTime}")
        
        elif 'exit' in query or 'বন্ধ করো' in query:
            speak("বিদায় রনি ভাই, ভালো থাকবেন!")
            break
