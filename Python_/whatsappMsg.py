import pyautogui as pg
import time

print("Program will run after 2 sec.")
time.sleep(2)
print("Running...")

for i in range(100):
    pg.write("Vinaju Namaskar.")
    time.sleep(0.2)
    pg.press("Enter")

    