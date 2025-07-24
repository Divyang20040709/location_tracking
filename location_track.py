import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+918154972029")
phone_number2 = phonenumbers.parse("+917698967219")
phone_number3 = phonenumbers.parse("+919377530775")
phone_number4 = phonenumbers.parse("+917383797894")
phone_number5 = phonenumbers.parse("+917487026589")
phone_number6 = phonenumbers.parse("+1(226)9758424")
phone_number7 = phonenumbers.parse("+1(216)9711142")

print("\nPhone number location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))
print(geocoder.description_for_number(phone_number5,"en"))
print(geocoder.description_for_number(phone_number6,"en"))
print(geocoder.description_for_number(phone_number7,"en"))