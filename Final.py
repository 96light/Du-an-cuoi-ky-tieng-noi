from tkinter import *

import datetime
import pickle
import os.path
import os
import time
import pyttsx3
import speech_recognition as sr
import pytz
import subprocess
import webbrowser
import time
from time import ctime
from datetime import datetime



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            # search=said
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said
def note(text):
    date = datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def click():
		check ="apple"
		CHECK2=1
		speak("how can i help you")
		while CHECK2 > 0 :
			text = get_audio().lower()
			print("Listening")
			if text.count(check)>0:
				speak("i am here")
				text =get_audio().lower()
				Name_STRS = [ "what's your name", "your name is","your name" ]
				for phrase in Name_STRS:
					if phrase in text:
						speak("My name is Katalina ")
						CHECK2=0
				NOTE_STRS = ["make a note", "write this down", "remember this"]
				for phrase in NOTE_STRS:
					if phrase in text:
						speak("What would you like me to write down? ")
						write_down = get_audio()
						note(write_down)
						speak("I've made a note of that.")
						CHECK2=0
				how_STRS = [ "how are you", "your name is"]
				for phrase in how_STRS:
					if phrase in text:
						speak("I am fine thank")
				Google_STRS = [ "google", ]
				for phrase in Google_STRS:
					if phrase in text:
						speak("search for")
						print("search for")
						ggsearch= get_audio().lower()
						print(ggsearch)
						speak("Here are the search results ")
						url= ("https://google.com/search?q="+ggsearch)
						print(url)
						webbrowser.open_new_tab(url)
						CHECK2=0
				Youtube_STRS = [ "youtube","you tube","you tu be" ]
				for phrase in Youtube_STRS:
					if phrase in text:
						speak("search for")
						print("search for")
						ytsearch= get_audio().lower()
						print(ytsearch)
						url= ("https://www.youtube.com/results?search_query="+ytsearch)
						print(url)
						speak("Here are the search results ")
						webbrowser.open_new_tab(url)
						CHECK2=0
				time_STRS = [ "tell me the time","what time is it" ]
				for phrase in time_STRS:
					if phrase in text:
						now = datetime.now()
						current_time = now.strftime("%H hour %M minute")
						print("Current Time =", current_time)
						speak(current_time)
						CHECK2=0
				Facebook_STRS = [ "face book","play book","facebook" ]
				for phrase in Facebook_STRS:
					if phrase in text:
						url= ("https://www.facebook.com/")
						print(url)
						webbrowser.open_new_tab("https://www.facebook.com/")
						CHECK2=0
				mail_STRS = [ "email","gmail","mail","male","Gmail" ]
				for phrase in mail_STRS:
					if phrase in text:
						url= ("https://gmail.com/")
						print(url)
						webbrowser.open_new_tab("https://gmail.com/")
						CHECK2=0
				stackoverflow_STRS = [ "hero","get help","my hero","overflow","stack overflow" ]
				for phrase in stackoverflow_STRS:
					if phrase in text:
						url= ("https://stackoverflow.com/")
						print(url)
						webbrowser.open_new_tab("https://stackoverflow.com/")
						CHECK2=0
				Goodnight_STRS = [ "good night","go to sleep" ,"sleep" ]
				for phrase in Goodnight_STRS:
					if phrase in text:
						speak("good night sir")
						quit()
				nhaccuatoi_STRS = [ "music","mute" ]
				for phrase in nhaccuatoi_STRS:
					if phrase in text:
						speak("search for")
						print("search for")
						ytsearch= get_audio().lower()
						print(ytsearch)
						url= ("https://www.nhaccuatui.com/tim-kiem?q="+ytsearch)
						print(url)
						speak("Here are the search results ")
						webbrowser.open_new_tab(url)
						CHECK2=0
				netflix_STRS = [ "netflix" ]
				for phrase in netflix_STRS:
					if phrase in text:
						url= ("https://www.netflix.com/vn-en/")
						print(url)
						webbrowser.open_new_tab("https://www.netflix.com/vn-en/")
						CHECK2=0
				game_STRS = [ "game" ]
				for phrase in game_STRS:
					if phrase in text:
						url= ("http://game.granbluefantasy.jp/#mypage")
						print(url)
						webbrowser.open_new_tab("http://game.granbluefantasy.jp/#mypage")
						CHECK2=0
			else:
				print("say again")

				
				

			
		
		
		


root = Tk()
root.title('Voice Assistant')
root.geometry("340x340")
root.resizable(0, 0)

btnRec = Button(root, height=2, width=10, text="Rec", command=click)
btnRec.pack()
	
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill="y")

TxtBox = Text(root, height=200, width=200, yscrollcommand=scrollbar.set)
TxtBox.pack(expand=0, fill=BOTH)

scrollbar.config(command=TxtBox.yview)

root.mainloop()

