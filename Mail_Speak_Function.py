import pyttsx3 as ps

def speak(text):
	engine = ps.init()
	engine.say(text)
	engine.runAndWait()

speak("Hello My Name is Harsh Raj.")