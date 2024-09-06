import speech_recognition as sr
import keyboard
import time
import modi_plus as md

bundle = md.MODIPlus()
led = bundle.leds[0]

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen_and_recognize():
    print("Listening for 5 seconds...")
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjusts for background noise
            audio = recognizer.listen(source, timeout=5)  # Listen for 5 seconds
            print("Recognizing...")
            try:
                text = recognizer.recognize_google(audio, language='ko-KR')  # Recognize Korean
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
                return None
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return None
    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start.")
        return None

def main():
    print("Press Enter to start listening...")
    while True:
        result = None
        if keyboard.is_pressed('enter'):
            while result is None:
                result = listen_and_recognize()
            print("Press Enter to start listening again or Ctrl+C to exit.")
            # Prevent continuous listening by waiting for the key to be released
            while keyboard.is_pressed('enter'):
                pass
        if result == "에어컨 켜 줘":
          print("에어컨을 킵니다.")    
          led.set_rgb(0,0,255)
        elif result == "에어컨 꺼 줘":
          print("에어컨을 끕니다.")    
          led.turn_off()
            
    
    
        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")


