import pyttsx3

# create an event loop
while True:

    text_speech = pyttsx3.init()

    # open the text file
    with open("sample.txt", "r", encoding="utf-8") as f:
        answer = f.read()

    # if the text file is not empty will proceed with text to speech
    if answer != "":
        text_speech.say(answer)
        text_speech.runAndWait()
    
        with open("sample.txt", "w", encoding="utf-8") as f:
            pass
