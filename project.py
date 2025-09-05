import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import os
import subprocess


recognizer = sr.Recognizer()
engine=pyttsx3.init()

def say(x):
    engine.say(x)
    engine.runAndWait()
def speak(text):
    engine.say(text)
    engine.runAndWait()




def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com") 
    elif "open mocktail" in c.lower():
        webbrowser.open("https://moctale.in")
    elif "open music" in c.lower():
        webbrowser.open("https://music.youtube.com")
    elif "open ai" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://x.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "open mail" in c.lower():
        webbrowser.open("https://mail.google.com")


    elif "open files" in c.lower():
        os.startfile("explorer.exe")
    elif "open bin" in c.lower():
        os.startfile("shell:RecycleBinFolder")
    elif "open vs code" in c.lower():
      subprocess.Popen([r"C:\Users\ADMIN\AppData\Local\Programs\Microsoft VS Code\code.exe"])
    elif "open game" in c.lower():
        subprocess.Popen([r"D:\Game\Grand Theft Auto - San Andreas\gtasa.exe"])
    elif "open movies" in c.lower():
        subprocess.Popen({r"D:\HDD Data"})
    elif "start notes" in c.lower():
        os.startfile("notepad.exe")
    elif "open browser" in c.lower():
        subprocess.Popen([r"C:\Users\ADMIN\AppData\Local\Programs\Opera\opera.exe"])
    elif "open control panel" in c.lower():
        subprocess.Popen([r"control.exe"])
    #elif "open settings" in c.lower():
        #subprocess.Popen([r"C:\Windows\ImmersiveControlPanel\SystemSettings.exe"])
    elif "open powerpoint" in c.lower():
            subprocess.Popen([r"POWERPNT.EXE"])

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)


    else :
        print("Sorry, I can't help you with that. Please try again.. ")


if __name__ ==  "__main__" :
        speak("Hi I am Friday , how can i help you today  ...")
        print("Hi I am Friday , how can i help you today ...")
while True:

        r = sr.Recognizer()
       
        print ("recognizing...")
        try :
                with sr.Microphone() as source:
                    print("listening...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=2 )
                word = r.recognize_google(audio)
                if word.lower() == "friday":
                    say("Yes boss..")
                    print("Friday active...")
                with sr.Microphone() as source:
                     audio = r.listen(source)
                     command = r.recognize_google(audio)

                     processcommand(command)   

       
        except Exception as e:
            print("Error; {0}" .format(e) )