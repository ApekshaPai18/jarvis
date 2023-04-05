import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice',voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
    
def WishMe():
    hour=int(datetime.datetime.now().hour)    
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("hey dear")
    else:
        speak("Good evening")
        
    # speak("Hey apeksha i know you are single so here is something for you     apeksha you are one of the strongest people i know you need nobody to rely on so be the same as u r now  ")         
    speak("iam hinata how can i help you")

def takeCommand():
    #it takes voice from the user and returns the string
    
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognising....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        # print("user said:", query)
        
    except Exception as e:
        # print(e)
        print("say that again please....")
        return "None"   
    return query 
            
def sendEmail(do,content):
    server=smtplib.SMTP('smtp.gamil.com',587)
    server.eclo()
    server.starttls()
    server.login('apekshapai18@gmail.com','babbanna')
    server.sendmail('apekshapai18@gmail.com',to,content)
    server.close()   
    
if __name__=="__main__":
        WishMe()
        if 1:
            query=takeCommand().lower()
        
            if 'wikipedia' in query:
                speak('Searching wikipedia....')
                query=query.replace("wikipedia", "")
                results=wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                print(results)
                speak(results)
                
                
            elif 'open youtube' in query:
                webbrowser.open('youtube.com')
                
            elif 'open google' in query:
                webbrowser.open('google.com')  
                
            elif 'open stackoverflow' in query:
                webbrowser.open('stackoverflow.com')  
                
            elif 'open music' in query:
                music_dir='D:\\Non Critical\\sonss\\Favaouriye songs2'
                songs=os.listdir(music_dir) 
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0])) 
                
            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")  
                speak(f"The time is {strTime}")
                
            elif 'open code' in query:
                codePath= "C:\\Users\\Apeksha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
                os.startfile(codePath)  
                
           
                       
                    