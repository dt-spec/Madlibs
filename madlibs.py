#Madlibs

def game():
#helps the user pick the three storylines possible 
    gameChoice = int(input("Please select one of the three games: "))

    if gameChoice == 1:
        MdL1()
    elif gameChoice == 2:
        MdL2()
    elif gameChoice == 3:
        MdL3()

def MdL1():
    #storyline 1
    adjective = input(" Enter adjective:  ")
    noun = input("Enter noun: ")
    pluralNoun = input("Enter a plural noun: ")
    PIR = input("Enter a person in the room(female): ")
    AOC = input(" Enter an article of clothing: ")
    city = input(" Enter a city: ")
    madlibs = f"There are many {adjective} ways to choose a {noun} to read\
    .First, you could ask for recommendations from your friends and {pluralNoun}.\
    Just don't ask Aunt {PIR} -she only reads {adjective} books with {AOC} ripping goddesses\
    on the cover. if your friend are no help, trying check out the {noun} review in The {city} \
    Times. If the {pluralNoun} featured there are too{adjective} try something diffrent "

    print(madlibs)

def MdL2():
    #storyline 2
    adjective = input(" Enter adjective:  ")
    noun = input("Enter noun: ")
    pluralNoun = input("Enter a plural noun: ")
    PIR = input("Enter a person in the room(female): ")
    AOC = input(" Enter an article of clothing: ")
    city = input(" Enter a city: ")
    madlibs = f"Ron feels {adjective} when he is playing basketball at  {noun} \
    .He was the greatest shooter on the basketball court as he could shoot threes and dunk in front of  {pluralNoun}.\
    However, he always lost to  {PIR}. One day he harnessed the abilty to  {adjective} and it was because everytime he wore {AOC} he felt like he ruled {city} \ "

    print(madlibs)

def MdL3():
    #storyline 3
    adjective = input(" Enter adjective:  ")
    noun = input("Enter noun: ")
    pluralNoun = input("Enter a plural noun: ")
    PIR = input("Enter a person in the room(female): ")
    AOC = input(" Enter an article of clothing: ")
    city = input(" Enter a city: ")
    madlibs = f" Mark would always play the guitar   {adjective} and he felt it his way of connecting to  {noun} \
    .He made beats everydays and was successful in creating {pluralNoun}.\
    He ruled the city {city}  with his unique beats and sounds. "

    print(madlibs)

game()