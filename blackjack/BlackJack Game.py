
import random

class Card():


    def __init__(self, rank, suit):

        card_dict = {'A': 1,
              'K': 10,
              'Q': 10,
              'J': 10,
              '10':10,
              '9': 9,
              '8': 8,
              '7': 7,
              '6': 6,
              '5': 5,
              '4': 4,
              '3': 3,
              '2': 2
                    }

        self.rank = rank
        self.card_value = card_dict[rank]
        self.suit = suit


        #card = Card("4","hearts")
        #print(card.rank, card.suit, card.card_value)
        card_suits =["hearts", "diamonds", "spades", "clubs"]

class Deck():

    def __init__(self, suit, value):
        random_deck = []
        for suit in card_suits:
            for value in card_dict.keys():
                self.random_deck.append(Card(suit,value))

        #for suit in card_suits:
            #for value in card_dict.keys():
                #print(suit,value)


class Hands():

    def __init__(self):

    def player_one_hand(self):
        player_one_hand = []
        first_player_one_card = self.random_deck.pop()
        second_player_one_card = self.random_deck.pop()
        self.player_one_hand.append(first_player_one_card, second_player_one_card)

    def computer_hand(self):
        computer_hand = []
        first_computer_card = self.random_deck.pop()
        second_computer_card = self.random_deck.pop()
        self.computer_hand.append(first_computer_card, second_computer_card)

class Dealer():



    def hit_function(self):

        #player_one_total = first_player_one_card + second_player_one_card

    #Responsibilites:
    #deals 2 random cards from deck to player and self(possibly one to player one to dealer, and repeat?)
    #deals an additional card if player asks to "hit"
    #if player asks to "stay", dealer then deals himself a card if the sum of his cards is less than 17.
    #dealer will continue to "hit" until the value of his cards is greater than or equal to 17.
    #dealer will stop "hitting" when the value of his cards is greater than 21("bust") or between 17-21.

    #Collaborators:
    #Game
    #Card
    #Deck

class Game():
    game = False


    def start_game(self):
        self.game = True

    def


    def stop_game(self):
        self.game = False




    #Responsibilities:
    #starts game, do you want to play black jack?
    #player starts with $100 and can bet $5 or $10 dollars before each hand is dealt
    #if player gets a total of 21 on the first 2 random cards and Dealer does not have 21, Player Wins! + your bet and amount bet
      ##check to see if players cards equal 21 and if dealers cards equal 21
    ##if both dealer and player have 21, Dealer Wins!  - player bet
    #if player gets a total value greater then the dealer and it does not exceed 21, then Player Wins! + your bet...
    #if dealer exceeds 21, Player Wins!+ your bet...
    #if player exceeds 21, Dealer Wins! - your bet
    #if dealer gets a total value greater then the player and it does not exceed 21, the Dealer Wins! - your bet
    #if player sum of cards is equal to the dealers sum of cars <= 20 a "push" occurs no money is taken or given
    #if dealer or player win, ask to play another round or quit

    #Collaborators:
    #Dealer
    #Deck
    
