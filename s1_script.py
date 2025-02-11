## Version 2

#import ssl
#import urllib.request

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#contents = urllib.request.urlopen("https://ipapi.co/8.8.8.8/json", context=ctx).read()
#print(contents)


## Version 4

#import ssl
#import urllib.request

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#ip = "8.8.8.8"

#url = f"https://ipapi.co/{ip}/json/"
#contents = urllib.request.urlopen(url, context=ctx).read()
#print(contents)


## Version 6

import ssl
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ip = input("Enter IP to lookup: ")

url = f"https://ipapi.co/{ip.strip()}/json/"
contents = urllib.request.urlopen(url, context=ctx).read()
print(contents)

