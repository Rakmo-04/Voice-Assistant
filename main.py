import pyttsx3 as p
import speech_recognition as sr
from SeleniumWeb import infow
from Youtube import music
from News import *
import randfacts 
from joke import *
from Weather import *
from datetime import datetime
import tkinter as tk

class VoiceAssistantApp:
    def __init__(self, master):
        self.master = master
        master.title("Flora")
        master.geometry("500x400")

        self.title_label = tk.Label(master, text="Flora", font=("Helvetica", 24))
        self.title_label.pack(pady=20)

        self.activate_button = tk.Button(master, text="Activate Flora", command=self.activate_assistant, font=("Helvetica", 14), bg="#4CAF50", fg="white", padx=20, pady=10, bd=0)
        self.activate_button.pack()

        self.text_area = tk.Text(master, height=10, width=50, font=("Helvetica", 12))
        self.text_area.pack(pady=20)

        self.close_button = tk.Button(master, text="Close", command=self.quit_app, font=("Helvetica", 14), bg="#f44336", fg="white", padx=20, pady=10, bd=0)
        self.close_button.pack()

    def speak(self, text):
        self.text_area.insert(tk.END, text + "\n")
        self.text_area.see(tk.END)  # Auto-scroll to the bottom
        engine.say(text)
        engine.runAndWait()

    def get_audio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio)
            print("User said:", text)
            return text.lower()
        except Exception as e:
            print("Error:", str(e))
            return ""

    def custom_wake_word(self):
        self.speak("Say 'Hey Flora' to activate me.")
        while True:
            text = self.get_audio()
            if "hey Flora" in text:
                self.speak("How can I assist you?")
                return True

    def activate_assistant(self):
        if not self.custom_wake_word():
            return

        while True:
            text = self.get_audio()
            
            if "exit" in text or "quit" in text:
                self.speak('Exiting the program. Goodbye!')
                break

            if 'what about you' in text:
                self.speak('I am fine, thank you for asking.')

            if "information" in text:
                self.speak('You need information regarding?')
                infer = self.get_audio()
                self.speak('Searching {} in Wikipedia'.format(infer))
                assist = infow()
                assist.get_info(infer)

            elif 'play video' or 'play music' or 'play ' in text:
                self.speak('What would you like to play?')
                videoinf = self.get_audio()
                self.speak('Searching {} in YouTube'.format(videoinf))
                assist = music()
                assist.play(videoinf)
                

            elif "news" in text:
                self.speak("Sure, These are today's headlines:")
                arr = news()
                for i in range(len(arr)):
                    self.speak(arr[i])

            elif "fact" in text or "facts" in text:
                self.speak("Sure,")
                random = randfacts.getFact()
                self.speak("Did you know that " + random)

            elif "joke" in text or "jokes" in text or "funny" in text:
                self.speak("Sure, ")
                jokelist = joke()
                self.speak(jokelist[0])
                self.speak(jokelist[1])

    def quit_app(self):
        self.master.quit()

def main():
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()

if __name__ == "__main__":
    engine = p.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    main()
