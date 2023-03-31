import phonenumbers
from phonenumbers import geocoder, carrier, timezone
print("x" * 50)
enter_num = input("Please enter a phone number: ")
phone_num = phonenumbers.parse(enter_num,None)
print(phone_num)
ge=("The State Key : " + geocoder.description_for_number(phone_num,"en"))
ca=("The Telecom Company :" + carrier.name_for_number(phone_num,"en"))
tz=timezone.time_zones_for_number(phone_num)
print("The number: "+ str(phone_num)+"The State Key: "+ str(ge) +"The Telecom Company: "+ str(ca) +"The Time zone: "+str(tz))