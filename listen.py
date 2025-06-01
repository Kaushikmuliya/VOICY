import speech_recognition as sr
from speak import speak_text
def listen_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak_text("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not catch that.")
        speak_text("Sorry, I did not catch that")
        return None
    except sr.RequestError:
        print("Speech service Unavailable.")
        return None
    
    #The function listens through your microphone,
    #  tries to convert what you say into text using Google’s speech API,
    #  and returns that text. If it can’t understand or there’s a problem,
    #  it gracefully handles errors and returns nothing.