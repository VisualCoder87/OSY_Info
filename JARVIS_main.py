import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
# print(voices) 

engine.setProperty('voice',voices[0].id)
print(voices[0].id)

# speak function :  it takes a string as an argument and converts the text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# WishMe function : Wishing To you according  to the time of day: Morning, Afternoon or Night.
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12 :
        speak("Good Morning Sir")
    if hour>12 and hour<18 :
        speak("Good Afternoon Sir")
    if hour>18 and hour<24:
        speak("Good Evening Sir")
        
    speak("I am your virtual assistent. How can i  help you?")
    
# Take Command() : it take  the command from the user using microphone and returns output in form of string.
def TakeCommand():
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again !")
        return "None"
    return query

def SendMail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("patelsmeet871@gmail.com", "SpA@17jul2003")
    server.sendmail( "patelsmeet871@gmail.com", to , content)
    server.close()

# Main function :  Calling the WishMe() function & Listening for voice commands
if __name__ == '__main__':
    # speak('Smeet is Good Boy')
    WishMe()
    
    while True :
    # if 1:
        query = TakeCommand().lower()
    
        # Tasks :
        if 'wikipedia' in query:
            speak("searching  Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query :
            webbrowser.open("youtube.com")
            
        elif 'open google' in query :
            webbrowser.open("google.com")
        
        elif 'open chat gpt' in query :
            webbrowser.open('https://chat.openai.com/')
        
        elif 'play music' in query:
            music_path = 'C:\\Users\\ASHOK PATEL\\Music'
            songs = os.listdir(music_path)
            print(songs)
            os.startfile(os.path.join(music_path, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("TIME :",strTime)
            speak(f"Sir, the current time is {strTime}")
            
        elif 'open vs code' in query:
            VS_code = 'C:\\VS Code\\Code.exe'
            os.startfile(VS_code)
        
        elif 'open github' in query:
            git = 'C:\\Users\\ASHOK PATEL\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe'
            os.startfile(git)
            
        elif 'email' in query:
            try :
                speak('What should i say ?')
                content = TakeCommand()
                speak("Please enter email id of recipent:")
                to = input("To :")
                SendMail(to,content)
                speak("Email has been sent.")
                
            except Exception as e:
                print(e)
                speak("Sorry sir , I am unable to send this email.")