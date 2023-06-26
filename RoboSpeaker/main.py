import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    print("Welcome to RoboSpeaker 1.1 created by Sunny")
    while True:
        x = input("Enter what you want me to pronounce: ")
        if x.lower() == "q":
            break
        engine.say(x)
        engine.runAndWait()
