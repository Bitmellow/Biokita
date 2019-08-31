import pyttsx3

botname = "Servidor Biokita"
engine = pyttsx3.init()

def msg(text):
    print(botname + ":", text)
    engine.say(text)
    engine.runAndWait()
    