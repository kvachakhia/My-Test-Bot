import speech_recognition as sr
from gtts import gTTS
import os
import win32gui
import win32con


r = sr.Recognizer()

while True:

    with sr.Microphone() as source:
        print("Speak")
        audio_text = r.listen(source)
        print(".....")

        try:
            print("Text: "+r.recognize_google(audio_text, language="ka-GE"))
            speak = r.recognize_google(audio_text, language="ka-GE")
            if(speak == "გამარჯობა"):

                mytext = 'Gamarjoba Dimitri!'
                language = 'en'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("gamarjoba.wav")
                os.system("gamarjoba.wav")

                hwnd = win32gui.FindWindow(None, 'Groove Music')
                win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE) 

                print("Done")

            if(speak == "როგორ ხარ"):

                mytext = 'Kargad Shen rogor khar ?'
                language = 'en'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("rogor_khar.wav")
                os.system("rogor_khar.wav")

                hwnd = win32gui.FindWindow(None, 'Groove Music')
                win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE) 


                print("Done")
        except:
            print("Sorry, I did not get that")
