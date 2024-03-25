from selenium import webdriver
import time
from datetime import datetime

def print_seconds_remaining(seconds):
    while seconds > 0:
        print(f"Message will be sent in {seconds} seconds.", end="\r")
        time.sleep(1)
        seconds -= 1

def save_message_log(phone_number, message):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    day = now.strftime("%A")
    with open("message_log.txt", "a") as file:
        file.write(f"Date: {timestamp}, Day: {day}, Phone Number: {phone_number}, Message: {message}\n")

phone_number = input("Enter the phone number (include country code): ")
message = input("Enter the message you want to send: ")
hours = int(input("Enter the hour (in 24-hour format): "))
minutes = int(input("Enter the minutes: "))

try:
    current_time = time.localtime()
    hours_remaining = hours - current_time.tm_hour
    minutes_remaining = minutes - current_time.tm_min
    seconds_remaining = hours_remaining * 3600 + \
        minutes_remaining * 60 - current_time.tm_sec

    buffer_time = 30
    seconds_remaining -= buffer_time

    if seconds_remaining <= 0:
        print(
            "Call Time must be greater than Wait Time as Whatsapp Web takes Time to Load!")

    print_seconds_remaining(seconds_remaining)

    # Open WhatsApp Web
    driver = webdriver.Edge()
    driver.get("https://web.whatsapp.com/")
    print("Scan the QR code and press Enter when logged in")
    input()

    # Wait for 5 seconds
    time.sleep(5)

    # Find the chat input field and send the message
    chat_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
    chat_box.send_keys(message)
    time.sleep(1)
    chat_box.send_keys('\n')

    print(f"Message sent to {phone_number} successfully!")
    save_message_log(phone_number, message)

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Close the browser window after sending the message or in case of error
    if 'driver' in locals():
        driver.quit()
