'''try:
    a=10/0
    
except ZeroDivisionError:
    print("you cannot divide a number by zero")

else:
    print("division successful")

finally:
    print("execution completed")'''

import speech_recognition as sr



import pyttsx3

engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1

        audio = recognizer.listen(source)


        try:
            command = recognizer.recognize_google(audio,language='en-in')
            print("🗣️ You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Sorry, I didn't understand.")
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("❌ Speech service error.")
            speak("Sorry, my speech service is down.")
            return ""