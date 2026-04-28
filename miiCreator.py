class miiCreator:
    def __init__(self, name, birthday, personality, features = {'head' : 1, 
        'hair' : 1, 'eyebrows': 1, 'nose': 1, 'lips': 1, 'eyes': 1, 'ears': 1,
        'accessory' : None}):
        self.name = name
        self.birthday = birthday
        self.food_bar = 50
        self.friends = []
        self.personality = personality
        # features of mii
        self.features = features

        # a variable to describe features
        self.feature_map = {
            "head": ["Circle", "Oval", "Chad", "Triangle", "Square", "Heart", "Star"],
            "hair": ["Normal", "Wacky", "Bald", "Pompadour", "Long", "Spiky", "Curly", "Bowl Cut"],
            "eyebrows": ["Normal", "Thick", "Thin", "Angry", "Happy", "Surprised", "None"],
            "nose": ["Normal", "Small", "Big", "Round", "Pointy", "Button"],
            "lips": ["Normal", "Smile", "Frown", "Open", "Thin", "Full", "Pursed"],
            "eyes": ["Normal", "Big", "Small", "Happy", "Angry", "Sleepy", "Round", "Almond"],
            "ears": ["Normal", "Small", "Big", "Pointy", "Round", "None"],
            "accessory": ["None", "Glasses", "Sunglasses", "Hat", "Headphones", "Mask", "Bow", "Mustache"]
        }

    # setters and getters
    def setBirthday(self, birthday):
        self.birthday = birthday 

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def addFriend(self, mii):
        self.friends.append(mii)
    
    def removeFriend(self, mii):
        self.friends.remove(mii)

    # toString
    def __str__(self):
        return f"""
Name: {self.name}
Birthday: {self.birthday}
Personality: {self.personality}
Food Bar: {self.food_bar}/100
===Features===
{self.returnFeatures()}
"""
    
    # helper function to describe features
    def getFeature(self, feature_type):
        """
        The features are a bunch of lists that describe something from the mii, 
        structure is a dictionary that maps the feature followed by the index

        for example, for head: ["Circle", "Oval", "Chad"]
        you have Circle mapped with 1, Oval with 2, and Chad with 3
        """
        if feature_type in self.feature_map:
            feature_index = self.features.get(feature_type, 0)
            # Handle None for accessory
            if feature_type == "accessory" and feature_index is None:
                return "None"
            # Ensure index is within bounds
            if 0 <= feature_index < len(self.feature_map[feature_type]):
                return self.feature_map[feature_type][feature_index - 1]
        return "Unknown"

    # this is to display all features, returned as a string
    def returnFeatures(self):
        features = ""
        for feature in self.features:
            features += f"{feature}: {self.getFeature(feature)}\n"
        return features
    

