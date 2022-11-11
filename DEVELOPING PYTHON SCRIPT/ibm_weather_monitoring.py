import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

#Provide your IBM Watson Device Credentials
organization = "j0mda0"
deviceType = "Weather_monitoring_Device"
deviceId = "weather_today"
authMethod = "token"
authToken = "1@2@3@4@"

# Initialize GPIO
temp=random.randint(0,50)
pulse=random.randint(0,90)
oxygen=random.randint(0,100)
latitude=random.randint(0,100)
longitude=random.randint(0,100)



def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data['command'])
    print(cmd)
   
       


try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)
#..............................................

except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        #Get Sensor Data from DHT11

        data={"d":{'temperature':temp,'pulse':pulse,'oxygen':oxygen,'lattitude':latitude,'longitude':longitude}}
        #print data

        def myOnPublishCallBack():
            print("Published Temperature = %s C" %temp ,"Humidity = %s %%" %pulse)

        success=deviceCli.publishEvent("IotSensor","json",data,qos=0,on_publish=myOnPublishCallBack)
        if not success:
            print("not connected to IOTF")
        time.sleep(1)

       
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()