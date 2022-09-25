print("                                                                      ")
print("------------TEMPERATURE AND HUMIDITY BASED ALERT SYSTEM---------------")
import random
import time
from threading import Event
from playsound import playsound

class setvalue:
    def getTemperature(value):
        return str(random.randint(0, 60))

    def getHumidity(value):
        return str(random.randint(10, 70))


    def Check(value,temperature,humidity):
        if (int(temperature) > 40 or int(humidity) > 40):
            print("                                                                      ")
            print("!!  ALERT  !!")
            playsound('ALERT.wav')
            time.sleep(3)
            print("                                                                      ")


sensorValue = setvalue()
time.sleep(3)
while (True):
    Event().wait(3)
    temperature = sensorValue.getTemperature()
    humidity = sensorValue.getHumidity()
    print("                                                                      ")
    print("Temperature : "+temperature+ " degree C")
    print("Humidity : "+humidity+ " %")
    print("                                                                      ")
    sensorValue.Check(temperature,humidity)

