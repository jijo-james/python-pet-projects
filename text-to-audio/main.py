from gtts import gTTS
import os

text = ""

with open("data/sample_text.txt", "r") as f:
    for s in f:
        text += str(s)

    text = text.replace("\n", "")
    print(text)

audio = gTTS(text, slow=False, lang="en")
audio.save("data/audio_file.mp3")

os.system("rhythmbox " + "audio_file.mp3")
