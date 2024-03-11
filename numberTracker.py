import phonenumbers
from phonenumbers import timezone, carrier, geocoder
number = input("Enter Mobile Number with +__: ")
mob_no = phonenumbers.parse(number)
time = timezone.time_zones_for_geographical_number(mob_no)
sim_provider = carrier.name_for_number(mob_no, 'en') #en means get details in english
registered_at = geocoder.description_for_valid_number(mob_no, 'en')
print(mob_no,"\nTimezone: ",time,"\nSim Provider: ",sim_provider,"\nRegistered at: ",registered_at)
