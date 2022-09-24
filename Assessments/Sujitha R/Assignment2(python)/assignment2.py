
print("                                                                      ")
print("----------------------------------------------------------------------")
print("------------TEMPERATURE AND HUMIDITY BASED ALERT SYSTEM---------------")
print("----------------------------------------------------------------------")
print("                                                                      ")

# IMPORTING FILES

import random
from threading import Event
from playsound import playsound

# DEFINING CLASS TO GET TEMPERATURE AND HUMIDITY VALUES
class condition:
    def generateTemperature(value):
        return str(random.randrange(0, 70))

    def generateHumidity(value):
        return str(random.randrange(10, 80))

# FUNCTION TO CHECK THRESHOLD OF TEMPERATURE AND HUMIDITY

    def CheckCondition(value,temperature,humidity):
        if (int(temperature) > 50 and int(humidity) > 30):
            print("                                                                      ")
            playsound('ALERT.wav')
            print("!!!!!ALERT----ALERT!!!!!")
            Event().wait(3)
            print("                                                                      ")


sensorValue = condition()
Event().wait(3)
while (True):
    Event().wait(3)
    temperature = sensorValue.generateTemperature()
    humidity = sensorValue.generateHumidity()
    print("                                                                      ")
    print("Temperature : "+temperature+ " degree C")
    print("Humidity : "+humidity+ " %")
    print("                                                                      ")
    sensorValue.CheckCondition(temperature,humidity)
