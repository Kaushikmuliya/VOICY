import pyttsx3

engine=pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

#Initializes the text-to-speech engine.
#Defines a function speak_text(text) that takes a string text,
# speaks it out loud, and waits until speaking finishes.