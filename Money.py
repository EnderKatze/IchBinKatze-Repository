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
            print(exception)
            return 0

    @staticmethod
    def modifyMoney(targetID, moneyToAdd):
        with open("Money.json", "r") as f:
            moneyList = json.load(f)
        try:
            moneyList[str(targetID)] = int(moneyToAdd) + moneyList[str(targetID)]
        except Exception as exception:
            print(exception)
            moneyList[str(targetID)] = int(moneyToAdd)
        with open("Money.json", "w") as f:
            json.dump(moneyList, f)
