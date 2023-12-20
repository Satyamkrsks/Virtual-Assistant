import pyttsx3  #pip install pyttsx3 == text data into speech using python
import datetime
import speech_recognition as sr  #pip install SpeechRecongnition == speech d=from mic to text 
import smtplib
from secrets import senderemail , epwd , to
from email.message import EmailMessage 
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia 
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random
import psutil

engine = pyttsx3.init()

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def getvoices(voice):
   voices = engine.getProperty('voices')
   #print(voices[1].id)
   if voice == 1:
      engine.setProperty('voice',voices[0].id)
      speak("hello this is jarvis ")
   
   if voice == 2:
      engine.setProperty('voice',voices[1].id)
      speak("hello this is jarvis ")

def time():
   Time = datetime.datetime.now().strftime("%I:%M:%S") # hour=I minute=M seconds=S
   speak("the current time is:")
   speak(Time)

def date():
   year = int(datetime.datetime.now().year)
   month = int(datetime.datetime.now().month)
   date = int(datetime.datetime.now().day)
   speak("the current date is:")
   speak(date)
   speak(month)
   speak(year)

def greeting():
   hour = datetime.datetime.now().hour
   if hour >= 6 and hour <12:
      speak("Good Morning Sir!")
   elif hour >= 12 and hour <18:
      speak("Good Afternoon Sir!")
   elif hour >= 18 and hour <24:
      speak("Good Evening Sir!")
   else:
      speak("Good Night Sir!")

def wishme():
   speak("Welcome back sir!")
   time()
   date() 
   greeting()
   speak("jarvis at your service , please tell me how can i help u")


def takecommandCMD():
   query = input("please tell me how can i help you ?\n")
   return query

def takecommandMic():
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 1
      audio = r.listen(source)
   try:
      print("recognizning...")
      query = r.recognize_google(audio , language="en-IN")
      print(query)
   except Exception as e:
      print(e)
      speak("Say that again Please...")
      return"None"
   return query

def sendEmail(receiver, subject, content):
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.starttls()
   server.login(senderemail, epwd)
   email = EmailMessage()
   email['From'] = senderemail
   email['To'] = receiver
   email['Subject'] = subject
   email.set_content(content)
   server.send_message(email)
   server.close()

def sendwhatsmsg(phone_no, message):
   Message = message
   wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
   sleep(10)
   pyautogui.press('enter')

def searchgoogle():
   speak('what should i search for?')
   search = takecommandMic()
   wb.open('https://www.google.com/search?q='+search)

def news():
   newsapi = NewsApiClient(api_key='6aec414a904d44b19bc452223b2d58b3')
   speak('what topic you need the news about?')
   topic = takecommandMic()
   data = newsapi.get_top_headlines(q=topic,
                                    language='en',
                                    page_size=5)
   newsdata = data['articles']
   for x,y in enumerate(newsdata):
      print(f'{x}{y["description"]}')
      speak(f'{x}{y["description"]}')
   
   speak("that's it for now i'll update you in some time ")

def text2speech():
   text = clipboard.paste()
   print(text)
   speak(text)

def covid():
   r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
   data = r.json()
   covid_data = f'confirmed cases :{data["cases"]} \n Deaths :{data["deaths"]} \n Recovered :{data["recovered"]}' 
   print(covid_data)
   speak(covid_data)

def screenshot():
   name_img = tt.time()
   name_img = 'D:\\jarvis 2.0\\screenshot\\{name_img}.png'
   img = pyautogui.screenshot(name_img)
   img.show()

def passwordgen():
   s1 = string.ascii_uppercase
   s2 = string.ascii_lowercase
   s3 = string.digits
   s4 = string.punctuation

   passlen = 8
   s = []
   s.extend(list(s1))
   s.extend(list(s2))
   s.extend(list(s3))
   s.extend(list(s4))

   random.shuffle(s)
   newpass = ("".join(s[0:passlen]))
   print(newpass)
   speak(newpass)

def flip():
   speak('okay sir, flipping a coin')
   coin = ['heads','tails']
   toss = []
   toss.extend(coin)
   random.shuffle(toss)
   toss = ("".join(toss[0]))
   speak('i flipped the coin and you got'+toss)

def roll():
   speak("okay sir , rolling a die for you")
   die = ['1','2','3','4','5','6']
   roll = []
   roll.extend(die)
   random.shuffle(roll)
   roll = ("".join(roll[0]))
   speak("i rolled the die and you get "+roll)

def cpu():
   usage = str(psutil.cpu_percent())
   speak('CPU is at'+ usage)
   battery = psutil.sensors_battery()
   speak("Battery is at")
   speak(battery.percent)

if _name_ == "_main_":

   getvoices(0)
   wishme()
   while True:
      query = takecommandMic().lower()
      if 'time' in query:
         time()

      elif 'date' in query:
         date()
      
      elif 'email' in query:
         email_list = {
             'test email':'sk3345164@gmail.com'
         }
         try:
            speak("To whom you want to send the mail?")
            name = takecommandMic()
            receiver = email_list[name]
            speak("what is the subject of the mail?")
            subject = takecommandMic()
            speak('what shoud i say?')
            content = takecommandMic()
            sendEmail(receiver,subject,content)
            speak("Email has been send")
         
         except Exception as e:
            print(e)
            speak("unable to send the email")
      
      elif 'message' in query:
         user_name = {
            'Jarvis':'9709938257'
         }
         try:
            speak("To whom you want to send the whats App message?")
            name = takecommandMic()
            phone_no = user_name[name]
            speak("what is the subject of the message?")
            message = takecommandMic()
            sendwhatsmsg(phone_no, message)
            speak("Message has been send")
         except Exception as e:
            print(e)
            speak("unable to send the message")
      
      elif 'wikipedia' in query:
         speak("Searching on wikipedia...")
         query = query.replace("wikipedia","")
         result = wikipedia.summary(query, sentences=2)
         print(result)
         speak(result)

      elif 'search' in query:
         searchgoogle()
      
      elif 'youtube' in query:
         speak("what should i search on youtube?")
         topic = takecommandMic()
         pywhatkit.playonyt(topic)

      elif 'weather' in query:
         city = 'new york'
         url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=94a61c105d390b85e26661f189a10832'
         res  = requests.get(url)
         data = res.json()

         weather = data['weather'] [0] ['main']
         temp = data['main']['temp']
         desp = data['weather'] [0]['description']
         temp = round((temp-32 * 5/9))
         print(weather)
         print(temp)
         print(desp)
         speak(f'weather in {city} city is like')
         speak('Temperature : {} degree'.format(temp))
         speak('weather is {}'.format(desp))

      elif 'news' in query:
         news()
      
      elif 'read' in query:
         text2speech()

      elif 'covid' in query:
         covid()
      
      elif 'open code' in query:
         codepath = 'C:\\Users\\abhishek kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
         os.startfile(codepath)

      elif 'open' in query:
         os.system('explorer c://{}'.format(query.replace('open','')))

      elif 'joke' in query:
         speak(pyjokes.get_joke())

      elif 'screenshot' in query:
         screenshot()
         speak("done!")

      elif 'remember that' in query:
         speak("what should i remember?")
         data = takecommandMic()
         speak("you said me to remember that"+data)
         remember = open('data.txt','w')
         remember.write(data)
         remember.close()

      elif 'do you know anything' in query:
         remember = open('data.txt','r')
         speak('you said me to remember that'+remember.read())
      
      elif 'password' in query:
         passwordgen()

      elif 'flip' in query:
         flip()

      elif 'roll' in query:
         roll() 

      elif 'cpu' in query:
         cpu()

      elif 'offline' in query:
         quit()
