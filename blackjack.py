import random

# Data Structures for Suits, ranks, and values
suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}

# Define class objects: Card, Deck, Player, and Hand
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)
        print("\nThe deck is shuffled")

    def deal(self):
        return self.cards.pop()


class Player:
    def __init__(self, bank=100):
        self.bank = bank
        self.bet = 0

    def sub_bank(self, amount):
        self.bank -= amount
        self.bet += amount

    def add_bank(self):
        self.bank += self.bet * 2



class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0

    def draw(self, card):
        self.hand.append(card)
        if (card.rank == "Ace" and self.value < 12):
            self.value += (values[card.rank] + 10)
        else:
            self.value += values[card.rank]

    def show(self):
        for card in self.hand:
            print(card)
            print("\n")

    def __del__(self):
        pass

# functions: win_check(), replay(), game_switch()

def win_check():
    if player_hand.value == 21:
        print("\nYou have won!")
        player.add_bank()
        player_hand.__del__()
        dealer_hand.__del__()
    elif player_hand.value > 21:
        print("\nYou have busted, buster!")
        player_hand.__del__()
        dealer_hand.__del__()
    elif dealer_hand.value == 21:
        print("\nThe dealer has won!")
        print("\nThe dealer's hand was: ")
        dealer_hand.show()
        player_hand.__del__()
        dealer_hand.__del__()
    elif dealer_hand.value > 21:
        print("\nThe dealer busted, you won!")
        player.add_bank()
        player_hand.__del__()
        dealer_hand.__del__()
    elif dealer_hand.value == player_hand.value:
        print("\nYou tied with the dealer!")
        print("\nThe dealer's hand was: ")
        dealer_hand.show()
        player_hand.__del__()
        dealer_hand.__del__()
    elif dealer_hand.value < player_hand.value:
        print("\nYour hand is higher, so you won!")
        player.add_bank()
        player_hand.__del__()
        dealer_hand.__del__()
    else:
        print("\nThe dealer's hand is higher, so you lost")
        player_hand.__del__()
        dealer_hand.__del__()
        print("\nThe dealer's hand was: ")
        dealer_hand.show()


def replay_check():
    global replay, game_on
    player_replay = str(input("\nWould you like to continue playing? (Y/N): "))
    player_replay.lower()
    if player_replay[0] == "y":
        print("\nDealing next round...")
    else:
        print("\nThank you for playing, please play again soon!")
        replay = False
        game_on = False


def game_switch():
    global replay, game_on
    if player.bank  <= 0:
        print("\nYou are out of money? Get out!!!")
        replay = False
        game_on = False


# game state variables

game_on = True
replay = True

# game loop

while game_on:
    print("Welcome to willow's blackjack game!\n")

    player = Player()
    dealer = Player()

    while replay:
        game_deck = Deck()
        game_deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.draw(game_deck.deal())
        dealer_hand.draw(game_deck.deal())
        player_hand.draw(game_deck.deal())
        dealer_hand.draw(game_deck.deal())
        print(f"The dealer is showing: {dealer_hand.hand[0].__str__()}")
        print("Your hand: \n")
        player_hand.show()
        print(f"Count: {str(player_hand.value)}")
        print(f"You have ${str(player.bank)} left")
        amount = int(input("How much would you like to bet?: "))
        player.sub_bank(amount)
        hitorstay = str(input("Would you like to hit or stay? (H/S): "))
        hitorstay.lower()
        while hitorstay == "h" and player_hand.value < 21:
            player_hand.draw(game_deck.deal())
            print("Your hand: ")
            player_hand.show()
            print(f"Count: {str(player_hand.value)}")
            hitorstay = str(input("Would you like to hit or stay? (H/S): "))
            hitorstay.lower()
        while dealer_hand.value < 17:
            dealer_hand.draw(game_deck.deal())
        win_check()
        player.bet = 0
        replay_check()
        game_switch()