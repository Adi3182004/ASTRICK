import os
import re
is_listening = True
is_awake = False
WAKE_COOLDOWN = 2.0
import time
import shutil
import winshell          # pip install winshell
import sqlite3
import struct
import subprocess
import requests
import webbrowser
from playsound import playsound
import eel
import pyaudio
from datetime import datetime
import pyautogui
import pywhatkit as kit
import pvporcupine
import json
from engine.command import speak
from engine.config import ASSISTANT_NAME
from engine.helper import extract_yt_term, remove_words, replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

con = sqlite3.connect("astrick.db")
cursor = con.cursor()

@eel.expose
def playAssistantSound():
    music_dir = "www/assets/audio/start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower().strip()

    # Let chatbot handle recycle bin completely
    if "recycle bin" in query:
        return  # Let chatBot() route it via action

    
    if query.strip() == "youtube":
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return

    if query != "":
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (query,))
            results = cursor.fetchall()
            if results:
                speak("Opening " + query)
                os.startfile(results[0][0])
            else:
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (query,))
                results = cursor.fetchall()
                if results:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Searching for " + query)
                    webbrowser.open(f"https://www.google.com/search?q={query}")
        except Exception as e:
            print(f"[openCommand Error]: {e}")
            speak("Something went wrong")




def PlayYoutube(query):
    print(">>> PlayYoutube CALLED")

    try:
        search_term = extract_yt_term(query)

        if not search_term:
            search_term = query

        search_term = re.sub(
            r"\b(open|on youtube|youtube|video|song|please|play|and)\b",
            "",
            search_term,
            flags=re.IGNORECASE
        ).strip()

        if not search_term:
            speak("What should I play on YouTube?")
            return

        kit.playonyt(search_term)

        time.sleep(3)

        try:
            pyautogui.press('f')
        except:
            pass

    except Exception as e:
        print(f"[PlayYoutube Error]: {e}")
        speak("Something went wrong while trying to play the video.")

    finally:
       global is_listening, is_awake
       is_listening = True
       is_awake = False
        
        



def list_recycle_bin():
    files = []
    with winshell.recycle_bin() as rb:
        for item in rb:
            files.append(item.original_filename())
    return files

def delete_all_from_recycle_bin():
    return force_delete_recycle_bin()



def restore_all_from_recycle_bin():
    try:
        import win32com.client

        shell = win32com.client.Dispatch("Shell.Application")
        rb = shell.Namespace(10)

        if rb is None:
            speak("Recycle bin not accessible.")
            return "Recycle bin error"

        items = list(rb.Items())
        if not items:
            msg = "Recycle bin is already empty."
            speak(msg)
            return msg

        restored_count = 0

        for item in items:
            try:
                verbs = item.Verbs()
                restored_here = False

                for v in verbs:
                    verb_name = v.Name.replace("&", "").lower()
                    if "restore" in verb_name:
                        v.DoIt()
                        restored_here = True
                        restored_count += 1
                        break

                if not restored_here:
                    print(f"[Restore Skip]: No restore verb for {item.Name}")

                time.sleep(0.15)

            except Exception as e:
                print("[Restore Skip]:", e)

        msg = f"Restored {restored_count} file(s) from recycle bin."
        print("[Recycle]:", msg)
        speak(msg)
        return msg

    except Exception as e:
        print(f"[Restore All Error]: {e}")
        speak("Failed to restore files.")
        return f"Error: {e}"
    
def restore_file_by_name(file_keyword):
    file_keyword = file_keyword.lower().strip()

    try:
        import win32com.client
        shell = win32com.client.Dispatch("Shell.Application")
        rb = shell.Namespace(10)

        if rb is None:
            speak("Recycle bin not accessible.")
            return "Recycle bin error"

        restored = False

        for item in rb.Items():
            name = item.Name.lower()

            if file_keyword in name:
                try:
                    verbs = item.Verbs()
                    for v in verbs:
                        verb_name = v.Name.replace("&", "").lower()
                        if "restore" in verb_name:
                            v.DoIt()
                            restored = True
                            break

                    if restored:
                        msg = f"Restored {name} from recycle bin."
                        print("[Recycle]:", msg)
                        speak(msg)
                        
                        break
                    else:
                        print("[Restore]: No restore verb found")

                except Exception as e:
                    print("[Restore Invoke Error]:", e)

        if not restored:
            msg = f"No file matching {file_keyword} found in recycle bin."
            print("[Recycle]:", msg)
            speak(msg)
            
            return msg

        return "Done"

    except Exception as e:
        print(f"[Restore Error]: {e}")
        speak("Error restoring file.")
        return f"Error: {e}"


def toggle_bluetooth_like_user(desired_state):
    import subprocess
    
   

    try:
        x, y = 1703, 676  # Bluetooth toggle coordinates

        # Step 1: Open Quick Settings ONCE
        pyautogui.hotkey('win', 'a')
        time.sleep(1.5)

        # Step 2: Check visual toggle color
        pixel = pyautogui.pixel(x, y)
        is_toggle_on = pixel[2] > 150 and pixel[0] < 100  # bluish = ON
        is_toggle_off = pixel[0] > 150 and pixel[1] > 150 and pixel[2] > 150  # gray = OFF

        # Step 3: Check adapter status (optional extra layer)
        result = subprocess.run(
            ['powershell', '-Command',
             "Get-PnpDevice | Where-Object { $_.Class -eq 'Bluetooth' -and $_.FriendlyName -like '*Adapter*' } | Select-Object -ExpandProperty Status"],
            capture_output=True, text=True
        )
        adapter_status = result.stdout.strip().lower()
        adapter_ok = "ok" in adapter_status

        # Step 4: Decide what to do
        if desired_state == "on":
            if adapter_ok and is_toggle_on:
                speak("Bluetooth is already on.")
            else:
                speak("Turning Bluetooth on.")
                pyautogui.moveTo(x, y, duration=0.3)
                pyautogui.click()
        elif desired_state == "off":
            if adapter_ok and is_toggle_off:
                speak("Bluetooth is already off.")
            else:
                speak("Turning Bluetooth off.")
                pyautogui.moveTo(x, y, duration=0.3)
                pyautogui.click()

        # Step 5: Close Quick Settings
        time.sleep(0.3)
        pyautogui.press('esc')

    except Exception as e:
        print(f"[Bluetooth Toggle Error]: {e}")
        speak("Something went wrong while toggling Bluetooth.")

def toggle_quick_setting(feature, desired_state):
    
    

    try:
        positions = {
            "wifi": {"x": 1612, "y": 676, "label": "Wi-Fi"},
            "airplane": {"x": 1770, "y": 679, "label": "Airplane mode"}
        }

        if feature not in positions:
            speak("Unknown feature.")
            return

        x, y = positions[feature]["x"], positions[feature]["y"]
        label = positions[feature]["label"]

        pyautogui.hotkey('win', 'a')  # Open quick settings
        time.sleep(1.5)

        pixel = pyautogui.pixel(x, y)
        is_on = pixel[2] > 150 and pixel[0] < 100    # Blue color
        is_off = pixel[0] > 150 and pixel[1] > 150 and pixel[2] > 150  # Light grey

        if desired_state == "on":
            if is_on:
                speak(f"{label} is already on.")
            else:
                speak(f"Turning {label} on.")
                pyautogui.moveTo(x, y, duration=0.3)
                pyautogui.click()
        elif desired_state == "off":
            if is_off:
                speak(f"{label} is already off.")
            else:
                speak(f"Turning {label} off.")
                pyautogui.moveTo(x, y, duration=0.3)
                pyautogui.click()

        time.sleep(0.4)
        pyautogui.press('esc')

    except Exception as e:
        print(f"[{feature} Toggle Error]: {e}")
        speak(f"Something went wrong while toggling {label}.")

def set_brightness_level(user_input):
  
    

    try:
        # STEP 1: Clean and extract integer percentage
        value = str(user_input).replace('%', '').strip()
        if not value.replace('.', '', 1).isdigit():
            speak("Please provide a valid brightness percentage.")
            print("[LocalBot]: Invalid input for brightness.")
            return

        percentage = float(value)

        # STEP 2: Clamp value and give feedback
        if percentage > 100:
            percentage = 100
            speak("Maximum limit is 100 percent. Adjusting brightness to 100.")
        elif percentage < 0:
            percentage = 0
            speak("Minimum limit is 0 percent. Adjusting brightness to 0.")
        else:
            percentage = int(percentage)
            message = f"Adjusting brightness to {percentage} percent."
            speak(message)
            print(f"[LocalBot]: {message}")

        # STEP 3: Calculate position based on your saved coordinates
        x_start = 1607
        x_end = 1840
        y_pos = 882
        slider_width = x_end - x_start
        target_x = x_start + int((slider_width * percentage) / 100)

        # STEP 4: Move and click
        pyautogui.hotkey('win', 'a')
        time.sleep(1.4)
        pyautogui.moveTo(target_x, y_pos, duration=0.3)
        pyautogui.click()
        pyautogui.press('esc')

    except Exception as e:
        print(f"[Brightness Error]: {e}")
        speak("Something went wrong while adjusting brightness.")

                      # Close Quick Settings

def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    last_wake_time = 0
    WAKE_COOLDOWN = 1.5

    try:
        porcupine = pvporcupine.create(
            keyword_paths=[r"C:\Users\adity\ASTRICK\engine\astrick.ppn"],
            access_key="YOUR_ACCESS_KEY_HERE"
        )

        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print("Hotword engine running (always listening)...")

        while True:
            pcm = audio_stream.read(
                porcupine.frame_length,
                exception_on_overflow=False
            )
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                now = time.time()

                if now - last_wake_time < WAKE_COOLDOWN:
                    continue

                last_wake_time = now
                print("Hotword detected!")

                pyautogui.keyDown("win")
                pyautogui.press("j")
                pyautogui.keyUp("win")

                time.sleep(0.25)

    except Exception as e:
        print(f"[Hotword Error]: {e}")

    finally:
        if porcupine:
            porcupine.delete()
        if audio_stream:
            audio_stream.close()
        if paud:
            paud.terminate()

def extract_city(user_input, patterns):
    for pattern in patterns:
        if "*" in pattern:
            regex = re.escape(pattern).replace("\\*", "(.+)")
            match = re.match(regex, user_input)
            if match:
                return match.group(1).strip()
    return None
def force_delete_recycle_bin():
    try:
        recycle_bin = os.path.join(os.environ["SystemDrive"] + "\\$Recycle.Bin")
        for root, dirs, files in os.walk(recycle_bin, topdown=False):
            for name in files:
                try:
                    os.remove(os.path.join(root, name))
                except:
                    pass
            for name in dirs:
                try:
                    shutil.rmtree(os.path.join(root, name), ignore_errors=True)
                except:
                    pass
        speak("Recycle bin has been emptied.")
        return "Recycle bin cleared."
    except Exception as e:
        speak("Failed to empty recycle bin.")
        print(f"[Force Recycle Error]: {e}")
        return f"Error: {e}"

def chatBot(query):
    global is_listening, is_awake

    user_input = query.strip().lower()
    json_path = "engine/cookies.json"

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for entry in data:
            patterns = entry.get("user_input", [])
            exact_match = any(user_input == p.lower() for p in patterns if "*" not in p)
            wildcard_match = None

            for p in patterns:
                if "*" in p:
                    pattern_regex = re.escape(p).replace("\\*", "(.+)")
                    match = re.match(pattern_regex, user_input)
                    if match:
                        wildcard_match = match.group(1).strip()
                        break

            if exact_match or wildcard_match:
                response = entry.get("response") or "Okay."
                action = entry.get("action")

                if "{city}" in response and wildcard_match:
                    response = response.replace("{city}", wildcard_match)
                if "{yt_term}" in response and wildcard_match:
                    response = response.replace("{yt_term}", wildcard_match)
                if "{folder_name}" in response and wildcard_match:
                    response = response.replace("{folder_name}", wildcard_match)
                if "{percent}" in response and wildcard_match:
                    response = response.replace("{percent}", wildcard_match)
                if "{file}" in response and wildcard_match:
                    response = response.replace("{file}", wildcard_match)

                print("[LocalBot]:", response)
                speak(response)
                

                if action == "shutdown":
                    os.system("shutdown /s /t 1")
                    return response

                elif action == "open_app":
                    path = entry.get("path")
                    if path:
                        os.startfile(path)
                        return response
                    fallback = "Sorry, I don't understand that yet."
                    print("[LocalBot]:", fallback)
                    speak(fallback)
                    
                    return fallback

                elif action == "weather":
                    return getWeather(wildcard_match or entry.get("city", "Mumbai"))

                elif action == "play_youtube":
                    PlayYoutube(wildcard_match or query)
                    return response

                elif action == "get_time":
                    getTime()
                    return response

                elif action == "bluetooth_on":
                    toggle_bluetooth_like_user("on")
                    return response

                elif action == "bluetooth_off":
                    toggle_bluetooth_like_user("off")
                    return response

                elif action == "wifi_on":
                    toggle_quick_setting("wifi", "on")
                    return response

                elif action == "wifi_off":
                    toggle_quick_setting("wifi", "off")
                    return response

                elif action == "airplane_on":
                    toggle_quick_setting("airplane", "on")
                    return response

                elif action == "airplane_off":
                    toggle_quick_setting("airplane", "off")
                    return response

                elif action == "brightness_control":
                    if wildcard_match:
                        set_brightness_level(wildcard_match)
                        return response

                elif action == "open_folder":
                    folder_path = f"C:\\Users\\{os.getlogin()}\\{wildcard_match}"
                    if os.path.exists(folder_path):
                        os.startfile(folder_path)
                        return response
                    else:
                        error_msg = "That folder doesn't exist."
                        print("[LocalBot]:", error_msg)
                        speak(error_msg)
                        
                        return error_msg

                elif action == "read_pdf":
                    pdf_name = wildcard_match.strip() if wildcard_match else ""
                    if not pdf_name.lower().endswith(".pdf"):
                        pdf_name += ".pdf"

                    speak(f"Sure, reading {pdf_name} from your Downloads folder.")
                    

                    try:
                        path_to_pdf = os.path.join(os.path.expanduser("~"), "Downloads", pdf_name)
                        if os.path.exists(path_to_pdf):
                            os.startfile(path_to_pdf)
                    except:
                        pass

                    reply = read_pdf_file(pdf_name)
                    print("[LocalBot]:", reply)
                    speak(reply)
                   
                    return reply

                elif action == "restart":
                    os.system("shutdown /r /t 1")
                    return response

                elif action == "check_rain":
                    return getRainForecast(wildcard_match or "Mumbai")

                elif action == "check_temp":
                    return checkTemperatureFeeling(wildcard_match or "Mumbai")

                elif action == "recycle_bin":
                    recycle_bin_prompt()
                    return response

                elif action == "empty_recycle_bin":
                    return delete_all_from_recycle_bin()

                elif action == "restore_recycle_bin_all":
                    return restore_all_from_recycle_bin()

                elif action == "restore_recycle_file":
                    if wildcard_match:
                        return restore_file_by_name(wildcard_match)
                    else:
                        speak("Please tell me the name of the file to restore.")
                        return "File name not provided."

                elif action == "delete_all_recycle_bin":
                    return delete_all_from_recycle_bin()

                elif action == "delete_recycle_file":
                    if wildcard_match:
                        return delete_file_by_name(wildcard_match)
                    else:
                        speak("Please tell me the name of the file to delete.")
                        return "File name not provided."

                return response

        fallback = "Sorry, I don't understand that yet."
        print("[LocalBot]:", fallback)
        speak(fallback)
        
        return fallback

    except Exception as e:
        error_msg = f"LocalBot Error: {e}"
        print(error_msg)
        speak("Something went wrong while processing.")
        return error_msg

    finally:
     global is_listening, is_awake
     is_listening = True
     is_awake = False



#change api key for weather API
import requests

def getWeather(city="Mumbai"):
    try:
        # For now, we hardcode Mumbai's coordinates
        coordinates = {
            "Mumbai": {"lat": 19.0760, "lon": 72.8777},
            "Pune": {"lat": 18.5204, "lon": 73.8567},
            "Delhi": {"lat": 28.6139, "lon": 77.2090},
            "Bangalore": {"lat": 12.9716, "lon": 77.5946},
            "Chennai": {"lat": 13.0827, "lon": 80.2707}
        }

        location = coordinates.get(city.title(), coordinates["Mumbai"])
        lat = location["lat"]
        lon = location["lon"]

        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url)
        data = response.json()

        if "current_weather" not in data:
            print("[Weather Error]: No data found")
            return "Sorry, I couldn't get the weather at the moment."

        weather = data["current_weather"]
        temperature = weather["temperature"]
        windspeed = weather["windspeed"]
        winddirection = weather["winddirection"]

        report = f"The current temperature in {city} is {temperature}°C with windspeed {windspeed} km/h."
        print(report)
        speak(report)
        return report
 

    except Exception as e:
        print(f"[Weather Error]: {e}")
        return "There was a problem getting the weather."

def getRainForecast(city="Mumbai"):
    try:
        latlon = {
            "Mumbai": {"lat": 19.0760, "lon": 72.8777},
            "Pune": {"lat": 18.5204, "lon": 73.8567},
            "Delhi": {"lat": 28.6139, "lon": 77.2090},
            "Bangalore": {"lat": 12.9716, "lon": 77.5946},
            "Chennai": {"lat": 13.0827, "lon": 80.2707}
        }

        location = latlon.get(city.title(), latlon["Mumbai"])

        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={location['lat']}&longitude={location['lon']}"
            f"&hourly=precipitation_probability&forecast_days=1&timezone=auto"
        )

        data = requests.get(url).json()
        times = data['hourly']['time']
        rain = data['hourly']['precipitation_probability']

        rain_lines = []
        speak_lines = []

        for t, r in zip(times, rain):
            if r > 20:
                time_only = t.split('T')[1]
                rain_lines.append(f"{time_only} → {r}%")
                speak_lines.append(f"{time_only}, {r} percent")

        if rain_lines:
            ui_forecast = f"Here is the rain forecast for {city.title()}:\n" + "\n".join(rain_lines[:6])
            speak_forecast = f"Here is the rain forecast for {city.title()}. " + ". ".join(speak_lines[:6])
        else:
            ui_forecast = f"No rain is expected today in {city.title()}."
            speak_forecast = ui_forecast

        print("[Rain Forecast]:\n", ui_forecast)
        speak(speak_forecast)
        
        return ui_forecast

    except Exception as e:
        print(f"[Rain Forecast Error]: {e}")
        speak("I couldn't get the rain forecast.")
        return "Rain forecast failed."



def checkTemperatureFeeling(city="Mumbai"):
    try:
        latlon = {
            "Mumbai": {"lat": 19.0760, "lon": 72.8777},
            "Pune": {"lat": 18.5204, "lon": 73.8567},
            "Delhi": {"lat": 28.6139, "lon": 77.2090},
            "Bangalore": {"lat": 12.9716, "lon": 77.5946}
        }

        location = latlon.get(city.title(), latlon["Mumbai"])
        url = f"https://api.open-meteo.com/v1/forecast?latitude={location['lat']}&longitude={location['lon']}&current_weather=true"

        data = requests.get(url).json()
        temp = data['current_weather']['temperature']

        if temp < 18:
            msg = f"It's {temp}°C. That's why it feels cold today."
        elif temp > 30:
            msg = f"It's {temp}°C. That's why it feels hot today."
        else:
            msg = f"It's {temp}°C. The temperature is quite pleasant."

        print(msg)
        speak(msg)
        return msg

    except Exception as e:
        print(f"[Temperature Check Error]: {e}")
        speak("Unable to check the temperature right now.")

def read_pdf_file(filename=None):
    import os
    import pyttsx3
    import PyPDF2
    import tkinter as tk
    from tkinter import scrolledtext
    import threading
   

    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    if not filename:
        return "No PDF filename provided."

    file_path = os.path.join(downloads_path, filename)

    if not os.path.exists(file_path):
        return f"File '{filename}' not found in Downloads."

    try:
        with open(file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        if not text.strip():
            return "This PDF has no readable text."

        # Setup TTS engine
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        for v in voices:
            if "male" in v.name.lower() or "david" in v.name.lower():  # adjust if needed
                engine.setProperty('voice', v.id)
                break
        engine.setProperty('rate', 160)

        # Setup GUI
        root = tk.Tk()
        root.title(f"Reading: {filename}")
        root.geometry("800x600")

        txt = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Segoe UI", 14))
        txt.pack(fill=tk.BOTH, expand=True)
        txt.insert(tk.END, text)
        txt.configure(state='disabled')

        lines = text.splitlines()

        def read_line_by_line():
            for i, line in enumerate(lines):
                if line.strip():
                    def highlight(index=i, content=line):
                        txt.configure(state='normal')
                        txt.tag_remove("highlight", "1.0", tk.END)
                        start = f"{index + 1}.0"
                        end = f"{index + 1}.end"
                        txt.tag_add("highlight", start, end)
                        txt.tag_config("highlight", background="yellow", foreground="black")
                        txt.see(start)
                        txt.configure(state='disabled')

                    root.after(0, highlight)  # Schedule in GUI thread
                    engine.say(line)
                    engine.runAndWait()
                    time.sleep(0.2)

            txt.tag_remove("highlight", "1.0", tk.END)  # Clear highlight at end

        threading.Thread(target=read_line_by_line).start()

        root.mainloop()
        return "Reading complete."

    except Exception as e:
        return f"Failed to read PDF: {e}"



def getTime():
    try:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        message = f"The current time is {current_time}"
        print("[Time]:", message)
        speak(message)
    except Exception as e:
        speak("There was a problem getting the time.")
        print(f"[Time Error]: {e}")

def findContact(query):
    query = remove_words(query, [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']).strip().lower()
    try:
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",
                       ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str
        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0


def whatsApp(mobile_no, message, flag, name):
   
    import subprocess
    import pyperclip
    from urllib.parse import quote
    import pygetwindow as gw

    try:
        pyautogui.PAUSE = 0.25
        pyautogui.FAILSAFE = True

        mobile_no = mobile_no.replace(" ", "")

        if flag == 'message':
            astrick_message = f"Message sent successfully to {name}"
        elif flag == 'call':
            astrick_message = f"Calling {name} on WhatsApp"
        else:
            astrick_message = f"Starting video call with {name}"

        encoded_message = quote(message)
        whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
        subprocess.run(f'start "" "{whatsapp_url}"', shell=True)

        time.sleep(9)

        try:
            wins = gw.getWindowsWithTitle("WhatsApp")
            if wins:
                wins[0].activate()
                time.sleep(1)
        except:
            pass

        if flag == 'message':
            sent = False
            retries = 3

            for _ in range(retries):
                try:
                    pyautogui.click(520, 1180)
                    time.sleep(0.7)

                    pyperclip.copy(message)
                    pyautogui.hotkey("ctrl", "v")
                    time.sleep(0.9)

                    pyautogui.click(1890, 995)
                    time.sleep(1.5)

                    sent = True
                    break
                except:
                    time.sleep(2)

            if not sent:
                speak("I could not send the WhatsApp message")
                return

            speak(astrick_message)
            return

        if flag == 'call':
            time.sleep(2)

            try:
                wins = gw.getWindowsWithTitle("WhatsApp")
                if wins:
                    wins[0].activate()
                    time.sleep(0.8)
            except:
                pass

            pyautogui.click(1753, 78)
            time.sleep(1.2)
            pyautogui.click(1546, 192)
            speak(astrick_message)
            return

        if flag == 'video call':
            time.sleep(2)

            try:
                wins = gw.getWindowsWithTitle("WhatsApp")
                if wins:
                    wins[0].activate()
                    time.sleep(0.8)
            except:
                pass

            pyautogui.click(1753, 78)
            time.sleep(1.2)
            pyautogui.click(1717, 188)
            speak(astrick_message)
            return

    except Exception as e:
        print(f"[WhatsApp Error]: {e}")
        speak("WhatsApp operation failed")

def makeCall(name, mobileNo):
    import subprocess
    mobileNo = mobileNo.replace(" ", "")
    speak("Calling " + name)

    command = [
        'adb',
        'shell',
        'am',
        'start',
        '-a',
        'android.intent.action.CALL',
        '-d',
        f'tel:{mobileNo}'
    ]

    try:
        subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
    except subprocess.CalledProcessError as e:
        speak("Failed to make the call. Please check the connection.")
        print(f"Error: {e}")

def sendMessage(message, mobileNo, name):
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    tapEvents(136, 2220)
    tapEvents(819, 2192)
    adbInput(mobileNo)
    tapEvents(601, 574)
    tapEvents(390, 2270)
    adbInput(message)
    tapEvents(957, 1397)
    speak("message send successfully to " + name)


def delete_file_by_name(file_keyword):
    file_keyword = file_keyword.lower().strip()

    try:
        import win32com.client
        import winshell

        shell = win32com.client.Dispatch("Shell.Application")
        rb = shell.Namespace(10)

        if rb is None:
            speak("Recycle bin not accessible.")
            return "Recycle bin error"

        deleted = False

        for item in list(rb.Items()):
            name = item.Name.lower()

            if file_keyword in name:
                try:
                    winshell.delete_file(item.Path, no_confirm=True)
                    deleted = True

                    msg = f"Deleted {name} from recycle bin."
                    print("[Recycle]:", msg)
                    speak(msg)
                    
                    break

                except Exception as e:
                    print("[Delete Force Error]:", e)

        if not deleted:
            msg = f"No file matching {file_keyword} found in recycle bin."
            print("[Recycle]:", msg)
            speak(msg)
            
            return msg

        return "Done"

    except Exception as e:
        print(f"[Delete Error]: {e}")
        speak("Error deleting file.")
        return f"Error: {e}"


def recycle_bin_prompt():
    try:
        speak("Opening Recycle Bin.")
        subprocess.run(["explorer", "shell:RecycleBinFolder"], check=True)
        time.sleep(2)

        prompt = "Recycle bin is open. Would you like to delete all, restore all, or restore a specific file?"
        print("[LocalBot]:", prompt)
        speak(prompt)
        

        try:
            eel.startListening()
            eel.playAssistantSound()
        except Exception as e:
            print(f"[Eel Listening Error]: {e}")

        return prompt
    except Exception as e:
        print(f"[Recycle Bin Prompt Error]: {e}")
        speak("Something went wrong while opening recycle bin.")
        return "Recycle Bin failed to open."
