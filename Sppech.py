import sounddevice
import wavio
from scipy.io.wavfile import write
import speech_recognition as sr
from textblob import TextBlob

fs = 44100
second = 10
print("recording")
record_voice = sounddevice.rec(int(second * fs), samplerate = fs, channels = 2)
sounddevice.wait()
wavio.write("AudioSample.wav", record_voice, fs ,sampwidth=2)

filename = "AudioSample.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)

f = open("Speech_to_text.txt", "w")
f.write(text)
f.close()

f = open("Speech_to_text.txt", "r")
txt = f.read()

edu = TextBlob(txt)
x = edu.sentiment.polarity
if x < 0:
    print("negative")
elif(x == 0):
    print("nuternel")
elif(x > 0 and x <= 1):
    print("positive")



