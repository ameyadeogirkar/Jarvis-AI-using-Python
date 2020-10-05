import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'your-password')
    server.sendmail('your_email@gmail.com', to, content)
    server.close()
    
    def takeCommand():
    print("type your command below")
    a = input("...")

    if a == "open youtube":
        print("opeaning youtube")
        webbrowser.open("youtube.com")
    elif a =="open google":
        print("opeaning google")
        webbrowser.open("google.com")
    elif a=="open white hat":
        print("opeaning WhiteHat jr")
        webbrowser.open("WhiteHatJr.com")
    elif a=="open VS code":
        print("openaing Visual studio code")
        codePath = "C:\\Users\\TAO-WSM\\AppData\\Local\\Programs\\Microsoft VS Code"
        os.startfile(codePath)

if __name__ == "__main__":
    wishMe()
    while True:

#         query = takeCommand().lower()
#         if 'wikipedia' in query:
#             speak('Searching in Wikipedia...')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=2)
#             speak("According to Wikipedia")
#             print(results)
#             speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\jarvis.exe"
            os.startfile(codePath)

        
