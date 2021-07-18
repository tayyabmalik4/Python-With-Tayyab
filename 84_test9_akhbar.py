def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.speak(str)
if __name__=='__main__':
    speak("how are you junaid and you all fine")