
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from datetime import date



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    nowtime = datetime.datetime.now().strftime("%H:%M:%S")    
    if hour>=0 and hour<12:
        speak("Good Morning  Sarthak!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon  Sarthak! ")   

    else:
        speak("Good Evening sarthak!") 
       
    speak("I am baemax. its")
    speak(nowtime) 
    speak("Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
       
        print(f"You said: {query}\n")
       
    

    except Exception:
        # print(e)    
        print("Say that again please...")  
        speak("sorry,  i am not able to understand, please say that again")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mailid@gmail.com', 'your password')
    server.sendmail('mail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe() 
    while True:
    # if 1:
        query = takeCommand().lower()

       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            break

        elif 'open google' in query:
            webbrowser.open("google.com")
            break

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            break


        elif 'play music' in query:
            speak("okay lets start with your favorate song  ")
            music_dir = 'F:/mysong'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            break

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'edit yourself' in query:
            speak("Okay Opening my code")
            codePath = "C:/Users/Hp/Desktop/python/speech.py"
            os.startfile(codePath)
        elif 'birthday' in query:
            bday= "12th september" 
            speak("I remember you previously said that your birthday is on ")
            speak(bday)

        elif 'mail to sarthak' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sarthakmd12@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")   
                speak(e)
        elif 'quit' in query:
            speak("Okay, happy to help you, take care will meet soon")
            break
        elif 'date' in query:
                            today = (date.today())
                            print("Today's date:", today)
                            speak("today's date is")
                            speak(today)

        elif 'happy' in query:
            speak("I  am glad u liked it, happy to help you ") 
        elif 'antimatter' in query:
            try :
                f = open("C:/Users/Hp/Desktop/antimatter.txt", "r")
                filecontent = f.read()
                print(filecontent)
                speak(filecontent)
            except Exception as err:
                print(err)
                speak(err)

        elif 'about yourself' in query:
    
            try :
                f = open("myfile.txt", "r")
                filecontent = f.read()
                print(filecontent)
                speak(filecontent)
            except Exception as err:
                print(err)
                speak(err)
        elif 'online mode' in query:
            speak("running online mode")
            speak("what u want me to search?")
            query = takeCommand()
            try: 
                from googlesearch import search 
            except ImportError as e:  
                print("No module named 'google' found") 
            speak("heres what i found on google")
            webbrowser.open(query)
        elif 'that note' in query:
            try :
                f = open("that note.txt", "r")
                filecontent = f.read()
                print(filecontent)
                speak(filecontent)
            except Exception as err:
                print(err)
                speak(err)
        elif 'global warming' in query:
            speak("Global warming is the long-term rise in the average temperature of the Earth's climate system It is a major aspect of current climate change, and has been demonstrated by direct temperature measurements and by measurements of various effects of the warming.[1][2] The term commonly refers to the mainly human-caused increase in global surface temperatures and its projected continuation. In this context, the terms global warming and climate change are often used interchangeably, but climate change includes both global warming and its effects, such as changes in precipitation and impacts that differ by region.There were prehistoric periods of global warming, but observed changes since the mid-20th century have been much greater than those seen in previous records covering decades to thousands of years")



            

                   
        
    

   