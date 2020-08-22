import pyttsx3
import os

# pyttsx3.speak("Welcome to my tools")


pyttsx3.speak("please tell me yor name first")
print("Please tell me yor name first : ", end='')
nme= input()
pyttsx3.speak("may i help you ")
pyttsx3.speak(nme)
while True:
	print("\n May I help you " , end='' ) 
	print (nme, end='')
	print ("? : ", end='' )
	p = input()

	#print(p)
	#os.system(p)

	if (("open" in p) or ("run" in p))  and (("notepad" in p) or ("editer" in p)) :
	    print("Notepad is opening " , end='')
	    print (nme, end='')
	    pyttsx3.speak("Notepad is opening")
	    pyttsx3.speak(nme)
	    os.system("notepad")

	elif (("open" in p) or ("run" in p)) and ("chrome" in p):
	    print("Chrome is opening " , end='' ) 
	    print (nme, end='')
	    pyttsx3.speak("Chrome is opening")
	    pyttsx3.speak(nme)
	    os.system("start chrome")

	elif (("open" in p) or ("run" in p)) and ("windows meada player" in p):
	    print("Windows media player is opening " , end='' ) 
	    print (nme, end='')
	    pyttsx3.speak("Windows Media Player is opening")
	    pyttsx3.speak(nme)
	    os.system("start wmplayer")

	elif (("open" in p) or ("run" in p)) and ("vlc" in p) :
	    print("vlc is opening " , end='' ) 
	    print (nme, end='')
	    pyttsx3.speak("vlc is opening")
	    pyttsx3.speak(nme)
	    os.system("start vlc")

	elif (("open" in p) or ("run" in p)) and ("itunes" in p) :
	    print("iTunes is opening " , end='' ) 
	    print (nme, end='')
	    pyttsx3.speak("itunes is opening")
	    pyttsx3.speak(nme)
	    os.system("start itunes")

	elif (("open" in p) or ("run" in p)) and (("explorer" in p) or (("my computer" in p) or ("this pc" in p))) :
	    print("My Computer is opening " , end='' ) 
	    print (nme, end='')
	    pyttsx3.speak("my computer is opening")
	    pyttsx3.speak(nme)
	    os.system("start explorer")

	elif (("open" in p) or ("run" in p)) and ("syncios" in p) :
	    print("Syncios is opening " , end='' ) 
	    print (nme, end='')
	    pyttsx3.speak("syncios is opening")
	    pyttsx3.speak(nme)
	    os.system("start syncios")

	elif (("open" in p) or ("run" in p)) and ("telegram" in p) :
	    print("Telegram is opening " , end='' ) 
	    print (nme, end='')
	    pyttsx3.speak("telegram is opening")
	    pyttsx3.speak(nme)
	    os.system("start telegram")

	elif (("open" in p) or ("run" in p)) and (("internet explorer" in p) or (("iexplore" in p))) :
	    print("Internet Explorer is opening " , end='' ) 
	    print (nme, end='')
	    pyttsx3.speak("internet explorer is opening")
	    pyttsx3.speak(nme)
	    os.system("start iexplore")

	elif (("open" in p) or ("run" in p)) and ("icloud" in p) :
	    print("iCloud is opening " , end='' ) 
	    print (nme, end='')
	    pyttsx3.speak("icloud is opening")
	    pyttsx3.speak(nme)
	    os.system("start icloud")

	elif (("bye" in p) or ("exit" in p) or ("quit" in p)):
	    print("Bye " , end='' ) 
	    print (nme, end='')
	    pyttsx3.speak("Bye")
	    pyttsx3.speak(nme)
	    break

	elif ("no " in p):
	    print("Okay then bye " , end='' ) 
	    print (nme, end='')
	    pyttsx3.speak ("okay then bye")
	    break

	elif ("yes" in p):
	    print("okay then go ahead")
	    pyttsx3.speak("okay then go ahead")

	elif ("how are you" in p):
	    print("I am fine. you say?") 
	    pyttsx3.speak("I am fine. you say?") 

	elif (nme in p):
	    print("I know your name " , end='' )
	    print(nme)
	    pyttsx3.speak("I know your name" )
	    pyttsx3.speak(nme)

	else:
	 print("Hmmmm...is there something else I can help with?") 
	 pyttsx3.speak("hmmmm...is there something else I can help with?")
	

