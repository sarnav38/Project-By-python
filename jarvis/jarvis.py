import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[1].id)
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)

def wishMe():
    # time =datetime.datetime.now()
    # print(time)
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    elif hour>=17 and hour<21:
        speak("Good Evening!")
    else:
        speak("Good night!")
    speak("Hi I am Jarvis. Please tell me how may i help you")

def speak(audio):
    """It will speak what so ever string you pass to it"""
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """It will take microphone input and return string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
# // using google reconizer for said speech
    try:
        print("Reconizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say it agian....")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587,timeout=120)
    server.ehlo()
    server.starttls()
    server.login('arnavsharma35@gmail.com','adu@544806')
    server.sendmail('arnavsharma35@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # print(takeCommand.__doc__)
    # print(speak.__doc__)
    # speak('Adu is a good boy')
    while True:
        query = takeCommand().lower()

        if 'exit' in query:
            exit(0)

        elif 'wikipedia' in query:
            speak("Searching wikipedia....")
            query =query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences =2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak('Opening youtube')
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            speak('Opening youtube')
            webbrowser.open('google.com')
        
        elif 'play videos' in query:
            fdir ='G:\\l'
            videos = os.listdir(fdir)
            # print(len(videos))
            rand_num =random.randint(0,(len(videos)-1))
            # print(rand_num)
            video = os.path.join(fdir,videos[rand_num])
            os.startfile(video)

        elif 'open code' in query:
            t_dir = "C:\\Users\\Arnav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(t_dir)
        
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir, the time is {strtime}")

        elif 'today date' in query:
            strdate = datetime.datetime.now().strftime('%d:%B:%Y')
            speak(f"sir, the date is {strdate}")
        
        elif 'send email' in query:
            try:
                speak('What should i say')
                content = takeCommand()
                to ="sarnav38@gmail.com"
                sendEmail(to,content)
                speak('Email has been sent successfully!')
            except Exception as e:
                print (e)
                speak('sorry my freind i am not able to send email')


        
        



