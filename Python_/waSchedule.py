import pywhatkit
import time
from datetime import datetime, timedelta

def print_seconds_remaining(seconds):
    while seconds > 0:
        print(f"Message will be sent in {seconds} seconds.", end="\r")
        time.sleep(1)
        seconds -= 1

def save_message(phone_number, message, date_time):
    timestamp = date_time.strftime("%Y-%m-%d %H:%M:%S")
    day = date_time.strftime("%A")
    with open("message_log.txt", "a") as file:
        file.write(f"Date: {timestamp}, Day: {day}, Phone Number: {phone_number}, Message: {message}\n")

phone_number = input("Enter the phone number (include country code): ")
message = input("Enter the message you want to send: ")

# Input future date and time
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
hours = int(input("Enter the hour (in 24-hour format): "))
minutes = int(input("Enter the minutes: "))

future_date_time = datetime(year, month, day, hours, minutes)

try:
    current_time = datetime.now()
    time_difference = future_date_time - current_time

    if time_difference.total_seconds() <= 0:
        print("Specified date and time should be in the future.")
        exit()

    seconds_remaining = int(time_difference.total_seconds())

    buffer_time = 30
    seconds_remaining -= buffer_time

    print_seconds_remaining(seconds_remaining)

    pywhatkit.sendwhatmsg(phone_number, message, future_date_time.hour, future_date_time.minute)
    print(f"Message will be sent to {phone_number} at {future_date_time} successfully!")
    save_message(phone_number, message, future_date_time)
except Exception as e:
    print(f"Error: {str(e)}")
