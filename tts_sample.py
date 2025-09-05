import pyttsx3

class _TTS:

    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()


    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()


tts = _TTS()
tts.start("text")
del(tts)

tts2 = _TTS()
tts2.start("hello")
del(tts2)