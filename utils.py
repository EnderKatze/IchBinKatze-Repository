import json

'''
Various Utilities down here!
'''


class Level:
    def __init__(self):
        pass

    @staticmethod
    def getLevel(targetID):
        with open("./Json/Experience.json", "r") as f:
            expList = json.load(f)
        try:
            returnList = list()

            level = round(int(expList[str(targetID)]) / 100 / 1.25)+1

            returnList.append(level)
            returnList.append(int(expList[str(targetID)]))

            return returnList
        except Exception as exception:
            del exception
            return [1, 0]

    # Not finished
    @staticmethod
    def modifyLevel(targetID, modifyValue):
        with open("./Json/Experience.json", "r") as f:
            expList = json.load(f)
        try:
            expList[str(targetID)] = int(modifyValue) + expList[str(targetID)]
        except Exception as exception:
            del exception
            expList[str(targetID)] = int(modifyValue)
        with open("./Json/Experience.json", "w") as f:
            json.dump(expList, f)

