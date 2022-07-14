import json
import os


class Money:
    def __init__(self):
        pass

    @staticmethod
    def getMoney(targetID):
        with open("Money.json", "r") as f:
            moneyList = json.load(f)
        if str(targetID) in moneyList:
            return str(moneyList[targetID])
        else:
            return 0

    @staticmethod
    def addMoney(targetID, moneyToAdd):
        with open("Money.json", "r") as f:
            moneyList = json.load(f)
        if str(targetID) in moneyList:
            moneyList[str(targetID)] = int(moneyToAdd) + moneyList[targetID]
        else:
            moneyList[str(targetID)] = int(moneyToAdd)
        with open("Money.json", "w") as f:
            json.dump(moneyList, f)
