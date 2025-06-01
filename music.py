import os
import random
import threading
from listen import listen_command
from speak import speak_text
from musicthread import play_music

def play_music_by_language():
    speak_text("Which Language?")
    language=listen_command()
    if language :
        print(f"You chose :{language}")
    else :
        print("Sorry i didn't get the language")
        speak_text("Sorry i didn't get the language")
        return
    base_folder = r"D:\MOVIESnSONGS\SONGS"
    target_folder= os.path.join(base_folder,language)

    if os.path.exists(target_folder):
        songs=[f for f in os.listdir(target_folder) if f.endswith((".mp3",".m4a"))]

        if songs :
            file_path=os.path.join(target_folder,random.choice(songs))
            music_thread=threading.Thread(target=play_music,args=(file_path,))
            music_thread.start()
        else:
            speak_text(f"No songs found in {language}")
    else :
        speak_text(f"No folder found for {language}")

