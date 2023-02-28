import speech_recognition as sr
import os
import soundfile as sf   #   pip install pysoundfile


import pyttsx3
def main():
    #path = "Sound_20140.wav"
    data, samplerate = sf.read('Sound_20140.ogg')
    sf.write('new_file.wav', data, samplerate)


    sound="new_file.wav"
    r = sr.Recognizer()
    with sr.AudioFile(sound) as source:
            r.adjust_for_ambient_noise(source)
            print('Convert.')
            audio = r.listen(source)


            query = r.recognize_google(audio, language='ru-RU')
            print (query)


if __name__=="__main__":
    main()


