from gtts import gTTS
import os
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib


def speaktext(command):
    language = 'en'
    myobj = gTTS(text=command, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("start welcome.mp3")


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour < 13:
        text = "Good Morning"
        speaktext(text)
    else:
        text = "Good Evening"
        speaktext(text)
    speaktext("I am Jarvis, how may i help you sir..")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        print(e)
        print("Please say again...")
        return "None"
    return query


def sendmail(to, content):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    # with open("ps.txt", "r") as f:
    #     pas = f.read()
    s.login("prataapmengu51437@gmail.com", "************")
    s.sendmail("prataapmengu51437@gmail.com", to, content)
    s.quit()


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "wikipedia" in query:
            speaktext("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speaktext("According to wikipedia")
            speaktext(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:&S")
            speaktext(f"Sir, The time is {strTime}")

        elif "open office" in query:
            os.system('start Office:')

        elif "open calculator" in query:
            os.system('start Calculator:')

        elif "open calender" in query:
            os.system('start Calender:')

        elif "open camera" in query:
            os.system('start Camera:')

        elif "open pycharm" in query:
            path = 'P:\\python files\\PyCharm Community Edition 2019.3\\bin\\pycharm64.exe'
            os.startfile(path)

        elif "open ip scanner" in query:
            path = "C:\\Program Files (x86)\\Advanced IP Scanner\\advanced_ip_scanner.exe"
            os.startfile(path)

        elif "send email" in query:
            speaktext("sir, What should i send")
            content = takecommand()
            speaktext("sir, whom should i send the mail")
            to = takecommand()
            sendmail(to, content)
            speaktext("Email has been send")

        else:
            speaktext("Sorry Sir i am not able to read or execute your command, please try something else")








