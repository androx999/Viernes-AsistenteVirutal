import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib
import json
import datetime
import wikipedia

name='viernes'
key = 'AIzaSyBDyz2d1BqOmobH47FOi1-dbtPy0H-dnp8'
flag = 1
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',178)
engine.setProperty('volume',1)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    flag = 1
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice=listener.listen(source)
            rec = listener.recognize_google(voice,language='es-ES')
            rec = rec.lower()
            
            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
              talk("Vuelve a intentarlo, no reconozco: " + rec)
    except:
                pass
                return flag

def run():
    
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo '+music)
        pywhatkit.playonyt(music)
    elif 'Cuantos suscriptores tiene' in rec:
        name_subs = rec.replace('Cuantos suscriptores tiene', '')
        data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername='+ name_subs + '&key=' + key).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        talk(name_subs+"tiene {:,d}".format(int(subs))+" subscriptores!")        
    elif 'hora' in rec:
                hora = datetime.datetime().now().strftime('%I:%M %p')
                talk("Son las "+hora)
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        info = wikipedia.summary(order,1)
        talk(info)
    elif 'exit' in rec:
        flag = 0
        talk("Saliendo...")
    else:
       talk("Vuelve a intentarlo,no reconozco: "+rect)
       return flag
   
while flag:
    flag = listen()