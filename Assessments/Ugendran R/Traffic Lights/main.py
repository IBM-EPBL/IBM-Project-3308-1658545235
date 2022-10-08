import random

from pyautogui import sleep

class LightController:
    def __init__(self,LightStates):
        self.LightStates = LightStates

    def Showvalues(self):
        print(self.LightStates)

    def IsGreen(State):
        if State=="Green":
            return True
    def IsOrange(State):
        if State=="Orange":
            return True

    def SetOrange(self,State):
        self.LightStates[State]="Orange"

    def SetGreen(self,Indices):
        index = random.choice(Indices)
        self.LightStates[index]="Green"
        
    def ChangeOrangetoRed(self):
        for LightState in range(len(self.LightStates)):
            if(LightController.IsOrange(self.LightStates[LightState])):
                self.LightStates[LightState]="Red"


    def FindGreen(self):
        for LightState in range(len(self.LightStates)):
            if(LightController.IsGreen(self.LightStates[LightState])):
                StateIndex=[0,1,2]
                #print(LightState)
                LightController.SetOrange(self,LightState)
                StateIndex.remove(LightState)
                #print(StateIndex)
        return StateIndex 
    def getLightStates(self):
        return self.LightStates    

        

    




def assignInitialState(LightStates):
    L1=LightStates[0]
    L2=LightStates[1]
    L3=LightStates[2]
    states=["Red","Green","Red"]
    L1=random.choice(states)
    states.pop(states.index(L1))
    L2=random.choice(states)
    states.pop(states.index(L2))
    L3=random.choice(states)
    states.pop(states.index(L3))
    LightStates=[L1,L2,L3]
    return LightStates


# Controller main
LightStates=[None,None,None]
LightStates=assignInitialState(LightStates)
L1=LightStates[0]
L2=LightStates[1]
L3=LightStates[2]
i=0
while(i<10):
    TrafficController = LightController(LightStates)
    TrafficController.Showvalues()          #red red green
    RedIndex=TrafficController.FindGreen()  #Implicitly Set Orange. ORR
    sleep(3)
    TrafficController.Showvalues()
    TrafficController.SetGreen(RedIndex) # Now Orange green Red  --> Orange to Red
    sleep(3)
    TrafficController.Showvalues()
    TrafficController.ChangeOrangetoRed()
    sleep(3)
    TrafficController.Showvalues()
    LightStates=TrafficController.getLightStates()
    i=i+1
