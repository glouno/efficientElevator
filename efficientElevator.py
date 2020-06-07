import time
import random
'''
import things

I wrote liftSimulation.py but it's way too complicated at first, trying to put physics and shit like this
I need to start small and then build up features
'''

#SIMULATION
def userInput():
    while True:
        try:
            global T
            global nbElevators
            global nbFloors
            global peopleDictionary
            global floorCount
            T=100 #runtime in seconds
            #nbElevators = int(input("Enter the number of Elevators: "))
            #nbFloors = int(input("Enter the number of Floors: "))
            nbElevators = 1
            nbFloors = 8 #Using fixed values for testing for now
            peopleDictionary = {"p0" : {"Floor" : 0, "targetFloor" : 2, "direction" : "up"}}
            floorCount = {"Floor0" : {"up": 3, "down": 2}}
        except ValueError:
            print("This is not a whole number.")
            continue
        else:
            return userInput
userInput()

def initialize():
    for n in range(nbFloors):
        floorCount["Floor"+str(n)] = {"up": 0, "down": 0}
initialize()

def randomPeople():
    probabilitySomeone = 0
    for t in range(T):
        print("t = "+str(t))
        probabilitySomeone = probabilitySomeone + random.random()
        print("probabilitySomeone is = " +str(probabilitySomeone))
        if probabilitySomeone >= 1:
            probabilitySomeone = 0
            print("Someone just popped")
            '''
            onWhichFloor = int(random.random()*nbFloors)
            print("This is onWhichFloor: " +str(onWhichFloor))
            toWhichFloor = int(random.random()*nbFloors)
            print("This is toWhichFloor" +str(toWhichFloor))
            '''
            onWhichFloor,toWhichFloor = random.sample(range(nbFloors), k=2)
            print("This is the random.sample version "+str(onWhichFloor)+" and "+str(toWhichFloor))
            if onWhichFloor<toWhichFloor:
                direction = "up"
            else:
                direction = "down"
            personNumber = int(list(peopleDictionary.keys())[-1].replace("p", "")) + 1 #[-1] take the last key in the dictionary (the person number) and gets rid of the p, converts it to an integer and adds one for the next person number
            print("This is personNumber = "+str(personNumber))
            peopleDictionary["p"+str(personNumber)] = {"Floor": onWhichFloor, "targetFloor": toWhichFloor, "direction": direction}
            
            print(type(floorCount["Floor"+str(onWhichFloor)]))

            #floorCount["Floor"+str(onWhichFloor)] = floorCount["Floor"+str(onWhichFloor)].get(direction) ##CAREFul
            print("THIS IS FLOORCOUNT BEFORE GET DIRECTION", floorCount["Floor"+str(onWhichFloor)].get(direction))
            #newDirectionNumber = floorCount["Floor"+str(onWhichFloor)].get(direction) + 1
            floorCount["Floor"+str(onWhichFloor)].update({direction: floorCount["Floor"+str(onWhichFloor)].get(direction) + 1}) #updates the number of people going "up" or "down" for every floor
            print("THIS IS FLOORCOUNT AFTER GET DIRECTION", floorCount["Floor"+str(onWhichFloor)].get(direction))

            if onWhichFloor == toWhichFloor:
                flag = True
                print("THIS IS A FLAG, they were EQUAL", flag)
                #generate again?
                break
        print(probabilitySomeone)
        time.sleep(.001)

randomPeople()

#TESTING
print(peopleDictionary)
print(floorCount)
