import random
#Part 1
class GameParticipant:
    #This is the game participant class
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    #function for updating balance after user places their bets
    def update_balance(self, amount):
        self.balance += amount

#Part 2
#Here im making sure Player class inherits from GameParticipant
class Player(GameParticipant):
    def place_bet(self, bet_amount, choice):
        if bet_amount > self.balance:#If user is placing more than they have
            raise ValueError("Insufficient balance for the bet.")
        return {"amount": bet_amount, "choice": choice}
    #the comparison between user input and the random choice
    def result(self, bet, outcome):
        return bet["choice"] == outcome
#Part 3
class DiceCup:
    #roll the dice and getting the sum of both dices
    def roll_dice(self):
        self.die1 = random.randint(1, 6)
        self.die2 = random.randint(1, 6)
        sum = self.die1 + self.die2
        #if even the outcome is cho else it is ho
        if sum % 2 == 0:
            outcome = "Cho"
        else:
            outcome = "Ho"
        return sum, outcome

#Part 4
#Player info
name = input("Enter your name: ")
balance = float(input("Enter your starting balance: "))
player = Player(name, balance)
#rolling the dice class
dice_cup = DiceCup()
print(f"Your current balance is: {player.balance}")
bet_amount = float(input("Enter your bet amount: "))
choice = input("Choose 'cho' (even) or 'han' (odd): ").lower()
if choice not in ["cho", "han"]:#if the user input is not any of these two options
    print("Invalid choice. Please choose 'cho' or 'han'.")
# user places the bet
bet = player.place_bet(bet_amount, choice)
# Roll the dice
sum, outcome = dice_cup.roll_dice()
print(f"The dice rolled: {sum} ({outcome})")

# the result
if player.result(bet, outcome):
    print("You won!")
    player.update_balance(bet_amount)
else:
    print("You lost.")
    player.update_balance(-bet_amount)

print(f"Your updated balance is: {player.balance}")

