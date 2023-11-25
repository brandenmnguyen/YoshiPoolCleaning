import time
import pyotp
import qrcode
import base64
import re

key = "YoshisKey"

#totp = pyotp.TOTP(key)

#while True:
#    print(totp.verify(input("Enter code:")))

uri = pyotp.totp.TOTP(key).provisioning_uri(name="HarveyDent5",issuer_name="YoshiApp")

print(uri)

qrcode.make(uri).save("totp.png")