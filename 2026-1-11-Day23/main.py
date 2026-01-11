import random
Best_One_word = ["Every thing will be fine",
                "Let's convey love",
                "It's going to be a great day"]

Good_One_word = ["It works pretty well",
                "Talk to people you care about",
                "Let's try something new"]

Bad_One_word = ["Stay home as much as possible",
                "Be careful not to fall",
                "let's refrain from challenges"]

fortune = {"Best":lambda:random.choice(Best_One_word),
           "Good":lambda:random.choice(Good_One_word),
           "Bad":lambda:random.choice(Bad_One_word)}


key,value = random.choice(list(fortune.items()))

print(key,":",value())
