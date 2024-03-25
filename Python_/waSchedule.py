import pywhatkit
import time


def print_seconds_remaining(seconds):
    while seconds > 0:
        print(f"Message will be sent in {seconds} seconds.", end="\r")
        time.sleep(1)
        seconds -= 1


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

    pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)
    print(f"Message sent to {phone_number} successfully!")
except Exception as e:
    print(f"Error: {str(e)}")
