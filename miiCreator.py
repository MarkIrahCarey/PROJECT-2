class miiCreator:
    import random

    def __init__(self, name, birthday, personality):
        self.name = name
        self.birthday = birthday
        self.food_bar = 50
        self.friends = []
        self.personality = personality

    # setters and getters
    def setBirthday(self, birthday):
        self.birthday = birthday 

    def setName(self, name):
        self.name = name

    def addFriend(self, mii):
        self.friends.append(mii)
    # toString
    def __str__(self):
        return f"Name: {self.name}\nBirthday: {self.birthday}\nPersonality: {self.personality}"
    

