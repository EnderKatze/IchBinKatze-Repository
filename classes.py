import json
import os


class Money:
    def __init__(self):
        pass

    @staticmethod
    def getMoney(targetID):
        with open("Money.json", "r") as f:
            moneyList = json.load(f)
        try:
            return str(moneyList[str(targetID)])
        except Exception as exception:
            del exception
            return 0

    @staticmethod
    def modifyMoney(targetID, modifyValue):
        with open("Money.json", "r") as f:
            moneyList = json.load(f)
        try:
            moneyList[str(targetID)] = int(modifyValue) + moneyList[str(targetID)]
        except Exception as exception:
            del exception
            moneyList[str(targetID)] = int(modifyValue)
        with open("Money.json", "w") as f:
            json.dump(moneyList, f)
