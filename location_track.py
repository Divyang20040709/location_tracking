import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("#Enter your number")

print("\nPhone number location\n")
print(geocoder.description_for_number(phone_number1,"en"))
