import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()
m =  sr.Microphone(device_index= 1)
import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
def record_volume():
    r = sr.Recognizer()
    with m as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
        #print('Слушаю...')
        audio = r.listen(source)
    #print('Услышала.')

    query = r.recognize_google(audio, language = 'ru-RU')

    print(f'Вы сказали: {query.lower()}')



record_volume()