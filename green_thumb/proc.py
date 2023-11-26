from numpy import average
from redis import WatchError
from green_thumb.db.models import Plant, PlantDataPoint
#This file should conver the current data into extracted information

def analyzeTemp(averageTemp, maxTemp, minTemp):
    tempRange = (maxTemp - minTemp) / 2

    if averageTemp < minTemp - tempRange:
        #Plant is WAY too cold!
        tempState = ("FROZEN",2)
    elif averageTemp < minTemp:
        #Plant is cold
        tempState = ("TOO COLD",1)
    elif  minTemp < averageTemp < maxTemp:
        #Plant temp is okay!
        tempState = ("PERFECT", 0)
    elif maxTemp + tempRange > averageTemp > maxTemp:
        #Plant is too hot!
        tempState = ("TOO HOT", 1)
    else:
        tempState = ("BOILING", 2)
    
    return tempState

def analyzeHumi(averageHumi, maxHumi, minHumi):
    humiRange = (maxHumi - minHumi) / 2

    if averageHumi < minHumi - humiRange:
        #Plant is WAY too dry!
        humiState = ("INCREDIBLY DRY", 2)
    elif averageHumi < minHumi:
        #Plant is cold
        humiState = ("TOO DRY", 1)
    elif  minHumi < averageHumi< maxHumi:
        #Plant temp is okay!
        humiStatete = ("PERFECT", 0)
    elif maxHumi + humiRange > averageHumi > maxHumi:
        #Plant is too hot!
        humiState = ("TOO HUMID", 1)
    else:
        humiState = ("EXTREMELY HUMID", 2)
    
    return humiState

def analyzeWater(averageWater, maxW, minW):
    waterRange = (maxW - minW) / 2

    if waterRange < minW - waterRange:
        averageWater = ("EXTREMELY THIRSTY", 2)
    elif waterRange < minW:
        averageWater = ("THIRSTY", 1)
    elif minW < averageWater < maxW:
        averageWater = ("PERFECT", 0)
    elif maxW + waterRange < averageWater > maxW:
        averageWater = ("TOO MUCH WATER", 1)
    else:
        averageWater = ("DROWNING", 2)

def analyzeVitals(plant:Plant):
    tempState = ''
    humiState = ''
    lightState = ''
    waterState = ''


    # First analyze plant vitals.
    data = Plant.data

    if len(data) > 100:
        recent = data[:-100] # In future use last 24h, not last 100 samples
    else:
        recent = data

    # Check Temperature:

    averageTemp = [x.temperature for x in recent] / 100

    averageHumi = [x.humidity for x in recent] / 100

    tempState = analyzeTemp(averageTemp, Plant.maxTemperature, Plant.minTemperature)
    humiState = analyzeHumi(averageHumi, Plant.maxHumididty, Plant.minHumididty)

    totalWater = sum([x.water_level - Plant.baseWaterLevel for x in recent])
    totalLight = sum([x.light_level for x in recent])
    
    waterState = analyzeWater(totalWater, Plant.waterMax, Plant.waterMin)
    lightState = ("TOO DARK", 1) if totalLight < Plant.lightRequirment else ("PERFECT", 0)

    return [tempState,humiState,waterState,lightState]

def analyze(plant:Plant):

    vitals = analyzeVitals(plant)

    data = Plant.data

    # Check if plant is currently being watered!
    if len(data) > 10:
        isWatering = sum([x.water_level for x in data[:3]]) > sum([x.water_level for x in data[3:10]])
    else:
        isWatering = False
    
    penalty = sum([x[1] for x in vitals])
    problems = [x[0] for x in vitals if x[1] != 0]

    return (penalty, problems)