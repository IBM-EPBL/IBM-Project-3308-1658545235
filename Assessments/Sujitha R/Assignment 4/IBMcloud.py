import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

#Provide your IBM Watson Device Credentials
organization = "j0mda0"
deviceType = "Sujitha"
deviceId = "2301"
authMethod = "token"
authToken = "Sujitha@2301"

# Initialize GPIO



def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data['command'])
    print(cmd)
    status=cmd.data['command']
    if status=="lighton":
        print("led is on")
    else:
        print("led is off")
       


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

        duration=random.randint(117,23547)
        distance=duration*0.034/2;
        d=round(distance,2);
        print("distance",d,"cm");
        if(distance<100):
            message="Alert";
        else:
            message="No problem";





       
        data = {"d":{ 'distance' : d,'message':message}}
        #print data
        def myOnPublishCallback():
            print ("Published distance = %d " %d, "Message = %s " % message, "to IBM Watson")

        success = deviceCli.publishEvent("Data", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
       
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
