
list_of_objects = []
pet_name = []



def Intro():
    line_1 = "Once upon a time..."
    line_2 = "There was a young boy named Jack who lived on a farm with his widowed mother.\n"
    line_3 = "This was not a great farm, as they only had one old dairy cow.\n"
    line_4 = "When the cow stopped giving milk, Jack's mother asked him to sell the cow at the market.\n"
    line_5 = "On the way, Jack meets a hooded figure who offers magic beans in exchange for the cow.\n"
    line_6 = "Entranced by his story of terrifying giants and gold,\n he makes the trade and excitedly brings the magic beans home.\n"
    line_7 = "His mother is furious that Jack made such an idiotic trade and tosses the beans out the window.\n"
    line_8 = "Disheartened, Jack goes to bed.\n"
    line_9 = "The next morning, he wakes up and sees a giant beanstalk that reaches to the clouds right outside his window.\n"
    line_10 = "Remembering the hooded stranger's stories, he climbs up the beanstalk to a land high in the sky.\n"
    line_11 = "In the distance Jack sees an old castle.  He has two options.  Jack should:\n"
    line_12 = "A: Go into the castle.\n"
    line_13 = "B: Explore outside first."
    print(line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9, line_10, line_11, line_12, line_13)

def Explore():
    print("Jack decides to explore outside the castle first.")
    print("While walking around, he notices something shiny under a nearby bush.")
    print("Upon closer inspection, he discovers a golden key!")
    print("Thinking that it may prove useful later, he decides to pocket it.")
    list_of_objects.append("key")

def Door():
    print("Unfortunately Jack has chosen incorrectly!  He stumbles into the kitchen and sees a giant standing at the sink with her back towards him.")
    print("She turns around and although he tries to hide, sees him running behind the leg of one of her chairs.")
    print("Having not had any guests in a long time, she proposes, 'Foolish human! If you wish to leave this room, you must play my favorite game...'")
    print("Hangman!")
    print("Welcome to Hangman!")
    print("The game is about to begin.")
    print("You have ten tries to guess the correct word.")
    print("Go!")
    word = "GOLDEN"
    word_list = []
    guessed = []
    for char in word:
        word_list.append(char)
    for i in range (len(word)):
        guessed.append("_")
    times = 0
    while guessed != word_list and times < 10:
        print(*guessed, sep=' ')
        g = input("Enter a letter: ")
        guess = g.upper()
        if guess in word_list:
            print("Correct")
            position = [i for i, x in enumerate(word_list) if x == guess]
            for i in position:
                guessed[i] = guess
        else:
            print("Incorrect.")
            times += 1
        if times == 10:
            print("You lose: \nThe word was", word, ". Unfortunately, the giant does not let Jack proceed.")
            print("The game is over.")
        elif guessed == word_list:
            print("You won! The word was GOLDEN.")
            print("Jack was able to escape the giant! He may now continue on his way!")
            list_of_objects.append("door")
        else:
            print("You have guessed incorrectly", times, "times")
     
def Hallway():
    l1 = "Near the end of the hallway, Jack notices a frightening animal approach him."
    print(l1)
    print("A: Run away? Or\nB: Let it approach you?")
    option = input("What does Jack do?: ")
    if option == "A":
        print("Surprisingly, it doesn’t chase him. He goes on his way.")
    if option == "B":
        print("The animal nuzzles into his hand and starts following him.")
        pet = input("What should Jack name his new pet?: ")
        pet_name.append(pet)
        list_of_objects.append("pet")

def follow_noise():
    print("Jackpot! Jack has stumbled across the giant's golden goose!\nThe goose and the giant seem to be having an argument.")
    if "key" in list_of_objects and "pet" not in list_of_objects:
        print("The giant turns to you and smiles.  'You have found the key!  Solve this riddle to pass me.  If you do, you can open the cage, and keep the goose'.")
    elif "pet" in list_of_objects and "key" not in list_of_objects:
        print("The giant turns to you and smiles.  'You have returned my lost pet!  Solve this riddle to pass me.  If you do, you can open the cage, and keep the goose'.")
    elif "pet" and "key" in list_of_objects:
        print("The giant turns to you and smiles.  'You have found the key and returned to me my lost pet!  Solve this riddle to pass me.  If you do, you can open the cage, and keep the goose'.")

def Ignore_Noise():
    print("Jack continues down the hallway and stumbles across a door leading outside. He opens the door.")
    if "pet" in list_of_objects: #pet rolls in grass
        print(pet_name[0], "bounds outside excitedly and rolls around in the grass.") 
    if "key" in list_of_objects: #if you already have the key, nothing happens
        print("Jack sees a familiar bush. \n 'Well that was pointless.'")
    else: #you find the key
        print("Jack finds a golden key in a bush! He decides to pocket it.")
        list_of_objects.append("key")
    print("Jack heads back inside.")
    if "pet" in list_of_objects: #pet follows
        print(pet_name[0], "follows, happily covered in grass stains.")
    

def Riddle():
    print("The giant asks, 'What has six faces and twenty-one eyes, but cannot see?'")
    answer = input("Answer: ")
    if answer == "dice" or "die":
        print("The giant scratches his chin. 'Hmmm not what I was thinking, but I guess you are correct.'")
        print("Congratulations! You have proven yourself to be worthy of this Golden Goose.")
        print("The giant sends Jack home. Upon seeing the Golden Goose, Jack's mom becomes overwhelmed with Joy.\nProud of having brought his family prosperity, Jack sleeps well that night.")
    elif answer == pet_name[0]:
        print("The giant grins. 'Exactly! Poor ", pet_name[0]," here lost his sight when he was just 46 years old.'")
        print("Congratulations! You have proven yourself to be worthy of this Golden Goose.")
        print("The giant sends Jack home. Upon seeing the Golden Goose, Jack's mom becomes overwhelmed with Joy.\nProud of having brought his family prosperity, Jack sleeps well that night.")
    else:
        print("'Sorry, you are wrong. I am afraid that you are undeserving of my golden goose.'")
        


def Story():
    Intro()
    castle_or_explore = input("enter A or B: ")
    if castle_or_explore == "B":
        Explore()
    if castle_or_explore == "A" or "B":
        print("Jack enters the castle.  On his left, he notices a big door.  In front of him, there is a long hallway.")
        print("Which way does Jack go?\nA: Through the big door or\nB: Down the long hallway?")
        door_or_hallway = input("enter A or B: ")
        if door_or_hallway == "A":
              Door()
        elif door_or_hallway == "B":
            Hallway()
    if "door" or "pet" in list_of_objects:
        print("As he continues on his way, he hears a noise down the West Wing.\nHe is met with another decision.")
        print("Does he\nA: Follow the noise or\nB: Ignore the noise.")
        noise = input("Enter A or B: ")
        if noise == "A":
            follow_noise()
        elif noise == "B":
            Ignore_Noise()
            follow_noise()
        if "key" or "pet" in list_of_objects:
            Riddle()
        else:
            print("Unfortunately Jack has not acquired enough objects throughout his journey to recieve the golden goose.  The giant sends him home empty handed./nJack comes home to see his mother's face riddled with worry. He does not sleep well that night.")
        

    
        
        
    
Story()
    
