# import pyautogui
# import time

# print("Move your cursor to the target position in the next 5 seconds...")
# time.sleep(5)

# x, y = pyautogui.position()
# print(f"Captured position: Point(x={x}, y={y})")
import pyautogui
import time

print("⏳ Move your mouse over the WhatsApp Send button in 5 seconds...")
time.sleep(5)

pos = pyautogui.position()
print(f"✅ Coordinates: {pos}")
