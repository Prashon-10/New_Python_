import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNumber = input("Enter the mobile number with Country Code (+..): ")
mobileNumber = phonenumbers.parse(mobileNumber)
if phonenumbers.is_valid_number(mobileNumber):
    print("Country: ", geocoder.description_for_number(mobileNumber, "en"))
    print("Region: ", timezone.time_zones_for_number(mobileNumber))
    print("Service Provider: ", carrier.name_for_number(mobileNumber, "en"))
else:
    print("Please Enter a Valid Number!")
