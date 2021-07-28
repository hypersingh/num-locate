import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder 


a = input("[+] Enter the target :")

phone_nm = phonenumbers.parse(a)

print(carrier.name_for_number(phone_nm, "en"))
print(geocoder.description_for_number(phone_nm, "en"))

