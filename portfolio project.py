
from pyfiglet import figlet_format 

# The title
print(figlet_format("Movie Trivia", font = "big"))


class Game:
    def __init__(self):
        # The score
        self.highscore = 0
        self.score = 0

    # The game screen
    def games(self):
        while True:
            print("1) Start Game? \n2) Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("Starting Game...")
            if choice == "2":
                print("Exiting Game...")
                break
            
            # Choices!
            print(figlet_format("Pick one!", font = "ogre"))
            print("1) Marvel")
            print("2) DC")
            print("3) Movies/TV_Shows")
            print("4) Disney")
            
            
            # Game Starting!   
            choice = input("Choose a category: ")
            if choice == "1":
                self.play_marvel()
                self.Highscore()
                print("You chose 'Marvel'")
                print(f"Your current high score is: {self.highscore}")
            elif choice == "2":
                self.play_DC()
                self.Highscore()
                print("You chose 'DC'")
                print(f"Your current high score is: {self.highscore}")
            elif choice == "3":
                self.play_Movies_TV_Shows()
                self.Highscore()
                print("You chose 'Movies/TV_Shows'")
                print(f"Your current high score is: {self.highscore}")
            elif choice == "4":
                self.play_Disney()
                self.Highscore()
                print("You chose 'Disney'")
                print(f"Your current high score is: {self.highscore}")
            else:
                print("Invalid choice, please try again")
                
    # Marvel Questions
    def play_marvel(self):
        
        
        # Question 1
        print("Which avenger gave Thanos the time stone?")
        print("1) Dr. Stange")
        print("2) Iron Man")
        print("3 Captain Marvel")
        print("4) Star Lord")
        choice = input("Choose the correct answer (1-4): ")

        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 2
        print("Where did Thanos sacrifice Gamora?")
        print("1) Wakanda")
        print("2) Morag")
        print("3) Vormir")
        print("4) Tesseract")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "3":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 3
        print("Why does sylvie want kill the time keepers?")
        print("1) She grew hatred for the TVA kidnapping her and never got to experience life normally")
        print("2) They killed her Father in Asgard")
        print("3) The TVA wanted to experiement on her brother")
        print("4) Thor was manipulated by the TVA")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 4
        print("Why did thor become super depressed in endgame?")
        print("1) Jane Foster broke up with Thor")
        print("2) Thor failed to prevent the destruction of Asgard")
        print("3) Couldn't stop Thanos in infinity war and lost Loki")
        print("4) All of the above")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 5
        print("Why did wanda try to kill america chavez?")
        print("1) She plans to steal America's power, killing her to get what she wants (which is her children)")
        print("2) America chavez threatens to kill her children")
        print("3) America chavez possesses the reality stone and time stone")
        print("4) She can control her variant that can get her children back")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 6
        print("How many Infinity Stones are there?")
        print("1) Six")
        print("2) Twelve")
        print("3) Thirteen")
        print("4) Eight")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 7
        print("Where is Captain America from?")
        print("1) Chicago")
        print("2) Brooklyn")
        print("3) Washington")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "2":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 8
        print("Who is Tony Starks father?")
        print("1) Clark Stark")
        print("2) Steve Stark")
        print("3) Lenel Stark")
        print("4) Howard Stark")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 9
        print("What does S.H.I.E.L.D. stand for?")
        print("1) Super human extraterrestrial leading and dimension")
        print("2) Super human education leading and Division")
        print("3) Strategic Homeland Intervention, Enforcement and Logistics Division")
        print("4) Strategic HomeInvasion, Enforcement and Law Division")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "3":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")
        
        # Question 10
        print("What type of doctor is Doctor Strange?")
        print("1) Plastic surgeon")
        print("2) General surgeon")
        print("3) Obstetrician")
        print("4) Neurosurgeon")

    # DC Questions
    def play_DC(self):
        
        # Question 1
        print("What is supermans real name?")
        print("1) Kael-el")
        print("2) Kal-el")
        print("3) Kalieth")
        print("4) Karl")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "2":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")
        
        # Question 2
        print("Which marvel actor starred in 2022 'The Batman?'")
        print("1) Chris Hemsworth")
        print("2) Robert Pattinson")
        print("3) Christian Bale")
        print("4) Micheal Keaton")
        print("5) Ben Affleck")
        choice = input("Choose the correct answer (1-5): ")
        if choice == "2":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 3
        print("Which actor played riddler in the 1995 Batman movies?")
        print("1) Paul Dano")
        print("2) Cory Micheal Smith")
        print("3) Jim Carrey")
        print("4) Matthew Gray Gubler")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "3":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")
        
        # Question 4
        print("This actor played in both Marvel and DC movies.")
        print("1) Chris Evans")
        print("2) Chris Hemsworth")
        print("3) Tom Hiddleston")
        print("4) Anthony Mackie")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 5
        print("What is the true identity of Two-Face?")
        print("1) Johathan Crane")
        print("2) Antonio Diego")
        print("3) Edward Nigma")
        print("4) Harvey Dent")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Questipn 6
        print("What is Batman's favorite food?")
        print("1) Chicken Noodle soup")
        print("2) Mulligatawny soup")
        print("3) Miso soup")
        print("4) Tomato soup")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "2":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 7
        print("Which DC character use to go by, 'Captain Marvel'?")
        print("1) Superman")
        print("2) Deadshot")
        print("3) Homelander")
        print("4) Shazam")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 8
        print("Who is the only superhero that was a member of both the Justice League and the Avengers?")
        print("1) Captain America")
        print("2) Green Lantern")
        print("3) Green Arrow")
        print("4) Hawkeye")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 9
        print("Which famous superhero originally had no flight ability?")
        print("1) Supergirl")
        print("2) Wonder Woman")
        print("3) Starfire")
        print("4) Superman")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 10
        print("Which planet is Superman from")
        print("1) Namek")
        print("2) Morag")
        print("3) Krypton")
        print("4) Vormir")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "3":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

    # Movies and TV Show Questions       
    def play_Movies_TV_Shows(self):
       
        # Question 1
        print("Which action movie beat out 2013's The Hunger Games: Catching Fire box office opening?")
        print("1) Black panther 2")
        print("2) Top Gun Marvericl")
        print("3) Avator 1")
        print("4) Star Wars: The Force Awakens")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 2
        print("Which movie won 7 Oscars in 2023?")
        print("1) Black panther 2")
        print("2) Elvis")
        print("3) The Way Of Water Avator")
        print("4) Everything Everywhere All at Once")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 3
        print("Which actor played in salt, kung fu panda, and shark tale?")
        print("1) Emily Blunt")
        print("2) Angelia Jolie")
        print("3) Angela Bassett")
        print("4) Salme Hyek")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "2":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")
        
        # Question 4
        print("What time period does Stranger Things take place in?")
        print("1) Mid - 1980s")
        print("2) Mid - 2000s")
        print("3) Mid - 1700s")
        print("4) Mid - 1850s")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 5
        print("What new Netflix show took the world by storm in 2021?")
        print("1) Umbrella Academy")
        print("2) Outer Banks")
        print("3) You")
        print("4) Squid Game")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 6
        print("In Cobra Kai, What motto is written on the walls of the Cobra Kai Dojo?")
        print("1) Strike First, Strike Hard, No Mercy")
        print("2) Please wash your hands")
        print("3) Fire Exit")
        print("4) Sign up for, 'Sweep the leg Saturdays'")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 7
        print("For what movie did Tom Hanks score his first Academy Award nomination?")
        print("1) Forest Gump")
        print("2) Toy Story")
        print("3) Big")
        print("4) Polar express")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "3":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 8
        print("Who is the only actor to receive an Oscar nomination for acting in a Lord of the Rings movie?")
        print("1) Ian Mckellen")
        print("2) Elijah Wood")
        print("3) Orlando Bloom")
        print("4) Sean Astin")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 9
        print("What is the highest-grossing R-rated movie of all time?")
        print("1) Joker")
        print("2) The Batman")
        print("3) Queen and Slim")
        print("4) Once Upon A Time In Hollywood")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 10
        print("What does Michael Scott eat for lunch on The Office that makes him fall asleep?")
        print("1) Apple Pie")
        print("2) Jamican Beef Patty")
        print("3) Chow Mein")
        print("4) A whole chicken pot pie")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")


    # Disney Questions
    def play_Disney(self):
     
        # Question 1
        print("In Frozen, why does Elsa sing “let it go!”?")
        print("1) She didnt want anything to do with her family")
        print("2) Ana doesnt accept her for who she is")
        print("3) She's frustrated at the way she's been forced to hide what she is capable of")
        choice = input("Choose the correct answer (1-3): ")
        if choice == "3":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 2
        print("What is the name of Wendys dog in Peter Pan?")
        print("1) Nana")
        print("2) Sandy")
        print("3) Gutrumb")
        print("4) Nona")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 3
        print("What famous actor voiced Lightning McQueen in Cars?")
        print("1) William Dafoe")
        print("2) Ben Affleck")
        print("3) Keau Reeves")
        print("4) Owen Wilson")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            self.score += 1
            print("Next question")
        
        # Question 4
        print("What was the first Pixar movie?")
        print("1) Cars")
        print("2) Wall-E")
        print("3) Incredibles")
        print("4) Toy Story")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 5
        print("Who said, 'Fish are friends, not food', in Finding Nemo?")
        print("1) Bruce")
        print("2) Steve")
        print("3) Sherman")
        print("4) Walter")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 6
        print("What did Aladdin steal from the marketplace?")
        print("1) Blanket")
        print("2) A loaf of Bread")
        print("3) Noodles")
        print("4) Money")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "2":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 7
        print("How many sisters does Ariel have?")
        print("1) Eight")
        print("2) Six")
        print("3) Five")
        print("4) Three")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "2":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 8
        print("Which music legend 'refused' to audition for Princess and the Frog?")
        print("1) Beyonce")
        print("2) Brandy")
        print("3) Mariah Carrey")
        print("4) Missy Elliot")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")
        else: 
            print("Wrong")
            print("Next question")

        # Question 9
        print("True or false: Sleeping Beauty was a box office flop.")
        print("1) True")
        print("2) False")
        choice = input("Choose the correct answer: ")
        if choice == "1":
            print("Correct")
            self.score += 1
            print("Next question")

        # Question 10
        print("Which rock band was originally meant to voice the vultures in The Jungle Book?")
        print("1) Rolling Stone")
        print("2) Pink Floyd")
        print("3) Backstreet Boys")
        print("4) The Beatles")
        choice = input("Choose the correct answer (1-4): ")
        if choice == "4":
            print("Correct")
            self.score += 1
            print("Next question")

    def Highscore(self):
        if self.score > self.highscore:  # Compares the scores
            self.highscore = self.score
        self.score = 0  # This reset the user's scorce for the next round
    
        



c = Game()
c.games()
c.Highscore()

              
            
        


