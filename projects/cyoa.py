"""A quiz game for sports nerds!"""
__name__ = "__main__"

from random import randint
points: int = 0
player: str = ""
sport: int 
LAUGHING_FACE = "\U0001F602"
MONEY_MOUTH = "\U0001F911"
i: int = randint(1, 5)


def main() -> None:
    global points
    global player
    global sport
    global i
    points = 0
    greet()
    sport = int(input(f"What Sport would you like to choose? 1 = Basketball, 2 = Soccer, 3 = Challenge Question and endgame. You currently have ${points}. "))
    while sport in {1, 2, 3}:
        if sport == 1:
            basketball()
        else:
            if sport == 2:
                soccer()
            else:
                print(f"You are currently sitting on ${points}. You will be randomly assigned a challenge question, but before, you must wager.")
                wager: int = int(input("How much are you willing to wager? $"))
                if wager <= points:
                    chal(points, wager)
                else:
                    print(f"You aren't that rich hahahaha{LAUGHING_FACE}{LAUGHING_FACE}{LAUGHING_FACE}")
                    print("Just for that you lose all of your money. Go back to school. Thanks for playing!")
    return None


def greet() -> None:
    name = input("Hello! What is your name? ")
    player = name
    print(f"Welcome, {player}, to Sports Millionaire! ")
    print("Similar to the TV show Who Wants to be a Millionaire, this is a money winning game where you can win money by demonstrating your sports knowledge. ")
    ready: str = input("Are you ready to play? Yes or No?  ")
    if ready == "Yes":
        print("Let's go!")
    else:
        print("Too bad, you're here. Lets go.")
    return None


def basketball() -> None:
    global points
    global sport
    print(f"So you fancy yourself a baller, {player}?  Here is your first question, for $125,000. ")
    print("Who won the NBA Finals MVP Award in 2015?")
    print("A: Draymond Green     B: Stephen Curry")
    print("C: Andre Iguodala     D: LeBron James")
    if input("Answer: ") == "C":
        points = points + 125000
        print(f"Well Done! You now have ${points}.")
        print("Question 2, for $125,000: Who holds the NBA Record for AST in a game?")
        print("A: Magic Johnson       B: Chris Paul")
        print("C: Rajon Rondo       D: Scott Skiles")
        if input("Answer: ") == "D":
            points = points + 125000
            print(f"Well Done! You now have ${points}.")
            print("Question 3, for $250,000: What is the 3rd number worn by Michael Jordan, other than 23 and 45?")
            print("A: 12       B: 18")
            print("C: 55       D: 2")
            if input("Answer:") == "A":
                points = points + 250000
                print(f"Well Done! You now have ${points}.")
                sport = int(input(f"What Sport would you like to choose? 1 = Basketball, 2 = Soccer, 3 = Challenge Question and endgame. You currently have ${points}. "))
            else:
                print("Incorrect")
                sport = int(input(f"What Sport would you like to choose? 1 = Basketball, 2 = Soccer, 3 = Challenge Question and endgame. You currently have ${points}. "))
        else:
            print("Incorrect")
            sport = int(input(f"What Sport would you like to choose? 1 = Basketball, 2 = Soccer, 3 = Challenge Question and endgame. You currently have ${points}. "))
    else:
        print("Incorrect")
        sport = int(input(f"What Sport would you like to choose? 1 = Basketball, 2 = Soccer, 3 = Challenge Question and endgame. You currently have ${points}. "))


def soccer() -> None:
    global points
    global sport
    print(f"So you know the game some call football, {player}?  Here is your first question, for $125,000. ")
    print("Which club has won the most Premier League titles?")
    print("A: Manchester United  B: Chelsea")
    print("C: Liverpool          D: Arsenal")
    if input("Answer: ") == "A":
        points = points + 125000
        print(f"Well Done! You now have ${points}.")
        print("Question 2, for $125,000: Who is currently the FC Barcelona Captain?")
        print("A: Gerard Pique       B: Sergi Roberto")
        print("C: Martin Braithwaite       D: Sergio Busquets")
        if input("Answer: ") == "D":
            points = points + 125000
            print(f"Well Done! You now have ${points}")
            print("Question 3, for $250,000: Who is the greatest player in history")
            print("A: Leo Messi           B: Lionel Andres Messi")
            print("C: PSG's Number 30     D: The little argentine magician")
            if input("Answer: ") == "A" or "B" or "C" or "D":
                points = points + 250000
                print(f"Well Done! You now have ${points}")
                sport = int(input(f"What Sport would you like to choose? 1 = Basketball, 2 = Soccer, 3 = Challenge Question and endgame. You currently have ${points}. "))
            else:
                print("Incorrect")
                sport = int(input(f"What Sport would you like to choose? 1 = Basketball, 2 = Soccer, 3 = Challenge Question and endgame. You currently have ${points}. "))
        else:
            print("Incorrect")
            sport = int(input(f"What Sport would you like to choose? 1 = Basketball, 2 = Soccer, 3 = Challenge Question and endgame. You currently have ${points}. "))

    else:
        print("Incorrect")
        sport = int(input(f"What Sport would you like to choose? 1 = Basketball, 2 = Soccer, 3 = Challenge Question and endgame. You currently have ${points}. "))


def chal(a=int, b=int) -> int:
    global points
    global sport
    global i
    print("Here is your Challenge Question:  ")
    if i == 1:
        print("Who holds the MLB Record for Stolen Bases in a Career")
        print("A: Billy Hamilton       B: Ricky Henderson")
        print("C: Ryan Braun           D: Francisco Cervelli")
        if input("Answer:") == "B":
            points = a + b
            print(f"Congrats, {player} your final earnings are ${points} {MONEY_MOUTH}. You have done better than I expected.")
        else:
            points = a - b
            print(f"Unlucky, you final winnings are ${points}. Well played.")
    else:
            
        if i == 2:
            print("Who holds the NFL Record for Single Season Rushing Yards")
            print("A: Ladanian Tomlinson       B: Derrick Henry")
            print("C: Adrian Peterson          D: Eric Dickerson")
            if input("Answer:") == "D":
                points = a + b
                print(f"Congrats, {player} your final earnings are ${points} {MONEY_MOUTH}. You have done better than I expected.")
            else:
                points = a - b
                print(f"Unlucky, you final winnings are ${points}. Well played.")
        else:
                
            if i == 3:
                print("Who won the Stanley Cup in 2018")
                print("A: Pittsburgh Penguins       B: Las Vegas Knights")
                print("C: TB Lightning              D: Washington Capitals")
                if input("Answer:") == "D":
                    points = a + b
                    print(f"Congrats, {player} your final earnings are ${points} {MONEY_MOUTH}. You have done better than I expected.")
                else:
                    points = a - b
                    print(f"Unlucky, you final winnings are ${points}. Well played.")
            else:
                    
                if i == 4:
                    print("Which of these is a sport native to the country of Ireland")
                    print("A: Hurling           B: Rugby")
                    print("C: Cricket           D: Billiards")
                    if input("Answer:") == "A":
                        points = a + b
                        print(f"Congrats, {player} your final earnings are ${points} {MONEY_MOUTH}. You have done better than I expected.")
                    else:
                        points = a - b
                        print(f"Unlucky, you final winnings are ${points}. Well played.")
                else:
                        
                    if i == 5:
                        print("Who scored the opening goal of the 2010 FIFA World Cup")
                        print("A: Diego Forlan                 B: Javier Hernandez")
                        print("C: Siphiwe Tshabalala           D: Miroslav Klose")
                        if input("Answer:") == "C":
                            points = a + b
                            print(f"Congrats, {player} your final earnings are ${points} {MONEY_MOUTH}. You have done better than I expected.")
                            
                        else:
                            points = a - b
                            print(f"Unlucky, you final winnings are ${points}. Well played.")
    sport = 4
                            
    return points


if __name__ == "__main__":
    main()