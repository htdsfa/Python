import random
from enum import Enum

gameLength = 5

Event = Enum("Event", ["chest", "nothing"])
loot = {Event.chest: 0.6, Event.nothing: 0.4}
lootlist = list(loot.keys())
lootProbability = list(loot.values())

chestEvent = Enum("chest",["greenChest", "orangeChest", "purpleChest", "goldChest"])
chest3 = {chestEvent.greenChest: 0.75, chestEvent.orangeChest: 0.20, chestEvent.purpleChest: 0.04, chestEvent.goldChest: 0.01}
chestList = list(chest3.keys())
chestProbability = list(chest3.values())



while gameLength > 0:
    gameQuestion = input("Do You want to move?: ")
    if (gameQuestion == "yes"):
        drawnEvent = random.choices(lootlist,lootProbability)[0]
        if (drawnEvent == Event.chest):
            print("You found a chest!")

        elif (drawnEvent == Event.nothing):
            print("You found nothing. We should move on.")

    gameLength = gameLength - 1