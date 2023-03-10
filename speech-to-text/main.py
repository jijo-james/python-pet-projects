import speech_recognition as sr

def main():

    sound = "are-you-still-there-voicemail.wav"

    r = sr.Recognizer()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)

        print("COnverting audio file to text...")

        audio = r.listen(source)

        try:
            print('Converted audio is:\n'+ r.recognize_google(audio))

        except Exception as e:
            print("Exception: {}".format(e))


if __name__ == '__main__' :
    main()