import datetime
import pyttsx3
import random
import smtplib
import speech_recognition as sr
import sys
import webbrowser
import wikipedia
import wolframalpha

print("Initializing jarvis")

client = wolframalpha.Client('Your_App_ID')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Raghavendra')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Say that again please')
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)

    return query


if __name__ == '__main__':

    while True:

        query = myCommand()
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'open whatsapp' in query:
            speak('okay')
            webbrowser.open('www.whatsapp.com')
        
        elif 'open bad boy song in youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com/watch?v=uj3FIwVKjDo')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'send email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'Sunil Kumar' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("botlaraghava@gmail.com", 'Raghava@1808')
                    server.sendmail('botlaraghava@gmail.com', "botlasunil@gmail.com", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Raghavendra! I am unable to send your message at this moment!')

        elif 'jarvis'  in query:
            speak('okay')
            speak('Hello Raghavendra')
            sys.start()

        elif 'hello' in query:
            speak('Hello Raghavendra')

        elif 'bye' in query:
            speak('Bye Raghavendra, have a good day.')
            sys.exit()





        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Raghavendra!')
