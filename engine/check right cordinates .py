import pyautogui
import time

pyautogui.hotkey('win', 'a')         # Open Quick Settings
time.sleep(1.5)
pyautogui.moveTo(1703, 676, duration=0.3)
pyautogui.click()
time.sleep(1)
pyautogui.press('esc')
