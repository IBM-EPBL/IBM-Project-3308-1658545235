import random
import time
import simpleaudio as sa
class getRandom:
    def getTemp(self):
        return str(random.randint(1, 400))

    def getHumidity(self):
        return str(random.randint(1, 50))
    def CheckwithThreshold(self,temp,humidity):
        if (int(temp) > 300 or int(humidity) > 40):
            for i in range(3):
                time.sleep(1)
                wave_obj = sa.WaveObject.from_wave_file("audio.wav")
                play_obj = wave_obj.play()
                play_obj.wait_done()
                print(".......Alert.......")


sensor1 = getRandom()
while (True):
    time.sleep(1)
    temp = sensor1.getTemp()
    humidity = sensor1.getHumidity()
    print("The Temperature is : "+temp)
    print("The Humidity is : "+humidity)
    sensor1.CheckwithThreshold(temp,humidity)