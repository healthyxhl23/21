#CS5001
#Fall 2023
#Final Project
#Herry Li & Nengjui Yu

#demo version - guite

import random

class Blackjack:
    def __init__(self):
        self.deck = self.create_deck()
        self.dealer_hand = []
        self.player_hand = []

    #deal card into a hand
    def deal_card(self, hand):
        card = self.deck.pop()
        hand.append(card)
        return card
    
    #creates card deck
    def create_deck(self) -> list:
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        game_deck = []

        for suit in suits:
            for rank in ranks:
                card = {'suit': suit, 'rank': rank} # {'suit': 'Hearts', 'rank': 'Ace'}
                game_deck.append(card)
        
        random.shuffle(game_deck)

        return game_deck

   
    #calculates hand value

    def calculate_hand_value(self, hand):
        value = 0
        ace_count = 0

        for card in hand:
            rank = card['rank']
            if rank in ['Jack', 'Queen', 'King']:
                value += 10

            elif rank == 'Ace':#ace can be 1 or 11
                ace_count += 1
                value += 11
            else:
                value += rank

        #avoid bust by counting ace 1
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
            
        return value

    
    #who wins>?

    def who_wins(self, player_value, dealer_value):
        #win:
        if player_value > dealer_value and player_value <= 21:
            print(f'Dealer has {dealer_value} \nYou Win')
            return f'Dealer has {dealer_value} \nYou Win'
        elif dealer_value > 21:
            print(f'Dealer has {dealer_value} \nYou Win')
            return f'Dealer has {dealer_value} \nYou Win'
        
        #lose
        elif player_value > 21:
            print(f'Dealer has {dealer_value} \nYou Lose')
            return f'Dealer has {dealer_value} \nYou Lose'
        elif dealer_value > player_value:
            print(f'Dealer has {dealer_value} \nYou Lose')
            return f'Dealer has {dealer_value} \nYou Lose'
        
        else:
            print('Tie')
            return 'Tie'
    

    #game
    

    #start game
    def start_game(self):
         # 2 cards per player to start
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        # Show hands
        # hide one of the dealer's cards
        # print(f'Your hand: {self.player_hand}')
        
        # #dealer randomly choose which card to show
        # num = random.randint(0, 1)
        # print(f"Dealer's hand: [[***], {self.dealer_hand[num]}]")

    
    def hit(self):
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)

   
    # def play_game(self):

    #     # 2 cards per player to start
    #     self.deal_card(self.player_hand)
    #     self.deal_card(self.dealer_hand)
    #     self.deal_card(self.player_hand)
    #     self.deal_card(self.dealer_hand)

    #     # Show hands
    #     # hide one of the dealer's cards
    #     # print(f'Your hand: {self.player_hand}')
        
    #     #dealer randomly choose which card to show
    #     num = random.randint(0, 1)
    #     print(f"Dealer's hand: [[***], {self.dealer_hand[num]}]")


    #     # Player's turn
    #     while True:
            
    #         player_value = self.calculate_hand_value(self.player_hand)
    #         print(f'Your Hand: {self.player_hand}\nHand value: {player_value}')

    #         #bust over 21
    #         if player_value > 21:
    #             print('Bust! Game over')
    #             return False
            
    #         #ask again if not hit or stand
    #         hit = input("Hit or Stand? ").lower()
    #         if hit == 'hit':
    #             self.deal_card(self.player_hand)
    #         elif hit == 'stand':
    #             break
            

    #     # Dealer's turn
    #     #dealer has to hit if under 17
    #     #can't have over 5 cards
        
    #     while self.calculate_hand_value(self.dealer_hand) < 17 and len(self.dealer_hand) < 6:
    #         self.deal_card(self.dealer_hand)

    #     #if dealer value over 21, bust
    #     dealer_value = self.calculate_hand_value(self.dealer_hand)
        
    #     print(f"Dealer's Hand: {self.dealer_hand}\nDealer's Hand value: {dealer_value}")

    #     return self.who_wins(player_value, dealer_value)
        


def main():
    pass
 



if __name__== "__main__":
    main()


