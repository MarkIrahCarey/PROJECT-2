import random
import time

class miiEvent:
    def __init__(self):
        """By default no event has occured, this is just to create the object"""
        self.lingo = ["Mii Island"]

    def createLingo(self, newLingo):
        self.lingo.append(newLingo)

    def textWriter(self, text, delay=100, end="\n"):
        # uses the time.sleep to type out each word per second
        words = text.split(" ")
        for word in words:
            print(word, end=" ", flush=True)
            time.sleep(delay / 1000)
        print(end=end)

    def mii_talking_event(self, mii1, mii2):
        """ There are many scenarios when mii's interact with each other
        We will do a simple mii1 and mii2 say hi and talk about a topic"""
        miis = [mii1, mii2]

        features = ['head', 'hair', 'eyebrows', 'nose', 'lips', 'eyes', 'ears']
        # randomly choose who is first to talk
        random_mii = random.randint(0, 1)
        other_mii = miis[1 - random_mii]

        """choose between three different scenarios
        1: Talking about the weather
        2: Talking about how good the other looks
        3: Talking about a lingo
        """
        random_event_num = random.randint(1, 3)
        
        if random_event_num == 1:
            # Weather conversation
            weather = random.choice(["sunny", "rainy", "cloudy", "windy"])

            self.textWriter(f"{miis[random_mii].getName()}: Hello {other_mii.getName()}!")
            self.textWriter(f"{other_mii.getName()}: Hi! Beautiful weather we're having today!")
            self.textWriter(f"{miis[random_mii].getName()}: I know, right? It is very {weather}. Perfect day for an adventure!")

        elif random_event_num == 2:
            # Compliment conversation

            # choose a random feature
            random_feature = random.choice(features)

            self.textWriter(f"{miis[random_mii].getName()}: Hey {other_mii.getName()}! Looking good today!")
            self.textWriter(f"{other_mii.getName()}: Thanks! You too!")
            self.textWriter(f"{miis[random_mii].getName()}: Did you do something different with your {random_feature}?")
            self.textWriter(f"{other_mii.getName()}: Yes {miis[random_mii].getName()}, I changed my {random_feature} to {other_mii.getFeature(random_feature)}.")
        
        else:
            lingo = random.choice(self.lingo)
            self.textWriter(f"{miis[random_mii].getName()}: Hey {other_mii.getName()}! Do you want to talk about", end="")
            self.textWriter(f". . .", 500, end="")
            self.textWriter(f"{lingo}", 300) 
            self.textWriter(f"{other_mii.getName()}: Ah", 1000)  
            self.textWriter(f"{other_mii.getName()}: Yes {miis[random_mii].getName()}, I would love to talk about {lingo}.", 250)