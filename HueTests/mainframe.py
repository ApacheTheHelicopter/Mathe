from phue import Bridge
import time



b = Bridge("192.168.1.100")

if (b != "0"): 
    print("Bridge is connected.")
else: 
    print("Error: Bridge not connected. Will try to connect now, press the Button!")
    b.connect()

print(b.get_light(1, "on"))


print(b.set_light(1, "on", True))