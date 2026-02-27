import pyttsx3
import speech_recognition as sr
import eel
import time
from engine.sms_controller import send_sms

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 174)


@eel.expose
def speak(text):
    global engine
    text = str(text)

    print(f"[LocalBot]: {text}")

    try:
        eel.addAssistantMessage(text)
    except Exception as e:
        print(f"[EEL UI ERROR]: {e}")

    engine.say(text)
    engine.runAndWait()
    


@eel.expose
def forceStopTTS():
    global engine
    try:
        engine.stop()
    except:
        pass


@eel.expose
def update_recognized_text(text):
    print(f"Sending to frontend: {text}")
    eel.DisplayRecognizedText(text)


@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            eel.DisplayMessage("Timeout: I didn't hear anything.")
            speak("I didn't hear anything. Please try again.")
            return ""

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        update_recognized_text(query)
        time.sleep(2)
        return query.lower()
    except Exception:
        update_recognized_text("Sorry, I couldn't understand. Please try again.")
        return ""


@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message.lower().strip()
        eel.senderText(query)

    query = query.lower().strip()

    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query or ("play" in query and "youtube" in query):
            from engine.features import PlayYoutube
            PlayYoutube(query)

        # =========================================================
        # 🔥 FIXED COMMUNICATION ROUTER
        # =========================================================
        elif (
            "send message" in query
            or "send sms" in query
            or "phone call" in query
            or "video call" in query
            or "call" in query
        ):

            from engine.features import findContact, whatsApp, makeCall

            contact_no, name = findContact(query)

            if contact_no != 0:

                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                # ================= MOBILE =================
                if "mobile" in preferance:

                    if "send message" in query or "send sms" in query:
                        speak("what message to send")
                        msg = takecommand()

                        if msg:
                            send_sms(contact_no, msg)
                        else:
                            speak("message was empty")

                    elif "call" in query:
                        makeCall(name, contact_no)

                    else:
                        speak("please try again")

                # ================= WHATSAPP =================
                elif "whatsapp" in preferance:

                    # ---------- WHATSAPP MESSAGE ----------
                    if "send message" in query:
                        speak("what message to send")
                        msg = takecommand()

                        if msg:
                            whatsApp(contact_no, msg, "message", name)
                        else:
                            speak("message was empty")

                    # ---------- WHATSAPP CALL ----------
                    elif "call" in query:

                        speak("Do you want voice call or video call")
                        call_type = takecommand()
                        print(call_type)

                        if "video" in call_type:
                            whatsApp(contact_no, "", "video call", name)
                        else:
                            whatsApp(contact_no, "", "call", name)

                    else:
                        speak("please try again")

                else:
                    speak("please say whatsapp or mobile")

            else:
                speak("Contact not found")

        else:
            from engine.features import chatBot
            chatBot(query)

    except Exception as e:
        print(f"[allCommands Error]: {e}")

    eel.ShowHood()