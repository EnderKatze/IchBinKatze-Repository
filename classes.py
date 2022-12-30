import json
import os

'''
Various Utilities down here!
'''

class Level:
    def __init__(self):
        pass

    @staticmethod
    def getLevel(targetID):
        with open("./Json/Level.json", "r") as f:
            levelList = json.load(f)
        try:
            return int(levelList[str(targetID)])
        except Exception as exception:
            del exception
            return 0

    @staticmethod
    def modifyLevel(targetID, modifyValue):
        with open("Level.json", "r") as f:
            levelList = json.load(f)
        try:
            levelList[str(targetID)] = int(modifyValue) + levelList[str(targetID)]
        except Exception as exception:
            del exception
            levelList[str(targetID)] = int(modifyValue)
        with open("Money.json", "w") as f:
            json.dump(levelList, f)

