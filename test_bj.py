#CS5001
#Fall 2023
#Final Project
#Herry Li & Nengjui Yu

#tests of demo version 

import unittest
from blackjack import Blackjack
class Test_BlackJack(unittest.TestCase):
    def test_create_deck(self):

        game = Blackjack()
        deck = game.create_deck()
        self.assertEqual(len(deck), 52)
        self.assertTrue({'suit': 'Hearts', 'rank': 7} in deck)
    
        game = Blackjack()
        deck = game.create_deck()
        self.assertEqual(len(deck), 52)
        self.assertTrue({'suit': 'Hearts', 'rank': 'Ace'} in deck)

        game = Blackjack()
        deck = game.create_deck()
        self.assertEqual(len(deck), 52)
        self.assertTrue({'suit': 'Hearts', 'rank': 8} in deck)



    def test_deal_card(self):

        game = Blackjack()
        hand = []
        game.deal_card(hand)
        self.assertEqual(len(game.deck), 51)
        self.assertEqual(len(hand), 1)

        game = Blackjack()
        hand = []
        game.deal_card(hand)
        game.deal_card(hand)
        self.assertEqual(len(game.deck), 50)
        self.assertEqual(len(hand), 2)

        game = Blackjack()
        d_hand = []
        p_hand = []
        game.deal_card(d_hand)
        game.deal_card(p_hand)
        self.assertEqual(len(game.deck), 50)
        self.assertEqual(len(d_hand), 1)
        self.assertEqual(len(p_hand), 1)



    def test_calculate_hand_value(self):
        game = Blackjack()
        hand = []
        game.deal_card(hand)
        self.assertTrue(type(game.calculate_hand_value(hand)), int)

        game = Blackjack()
        d_hand = []
        p_hand = []
        game.deal_card(d_hand)
        game.deal_card(p_hand)
        self.assertTrue(type(game.calculate_hand_value(d_hand)), int)
        self.assertTrue(type(game.calculate_hand_value(p_hand)), int)

        game = Blackjack()
        hand = [{'suit': 'Hearts', 'rank': 'Ace'}]
        self.assertEqual(game.calculate_hand_value(hand), 11)

        game = Blackjack()
        hand = [{'suit': 'Hearts', 'rank': 'Ace'},{'suit': 'Hearts', 'rank': 10}]
        self.assertEqual(game.calculate_hand_value(hand), 21)

        game = Blackjack()
        hand = [{'suit': 'Hearts', 'rank': 'Ace'},{'suit': 'Hearts', 'rank': 10},{'suit': 'Hearts', 'rank': 'Jack'}]
        self.assertEqual(game.calculate_hand_value(hand), 21)


        game = Blackjack()
        p_hand = [{'suit': 'Hearts', 'rank': 'Ace'},{'suit': 'Hearts', 'rank': 5},{'suit': 'Hearts', 'rank': 'Jack'}]
        d_hand = [{'suit': 'Hearts', 'rank': 'Ace'},{'suit': 'Hearts', 'rank': 10},{'suit': 'Hearts', 'rank': 'Jack'}]
        self.assertEqual(game.calculate_hand_value(p_hand), 16)
        self.assertEqual(game.calculate_hand_value(d_hand), 21)

        game = Blackjack()
        p_hand = [{'suit': 'Hearts', 'rank': 'Ace'},{'suit': 'Hearts', 'rank': 5},{'suit': 'Hearts', 'rank': 'Jack'}]
        d_hand = [{'suit': 'Hearts', 'rank': 10},{'suit': 'Hearts', 'rank': 10},{'suit': 'Hearts', 'rank': 'Jack'}]
        self.assertEqual(game.calculate_hand_value(p_hand), 16)
        self.assertEqual(game.calculate_hand_value(d_hand), 30)



    def test_who_wins(self):
        game = Blackjack()
        self.assertEqual(game.who_wins(21,10), 'Dealer has 10 \nYou Win')
        self.assertEqual(game.who_wins(1, 10), 'Dealer has 10 \nYou Lose')
        self.assertEqual(game.who_wins(10, 10), 'Tie')


        game = Blackjack()
        p_hand = [{'suit': 'Hearts', 'rank': 'Ace'},{'suit': 'Hearts', 'rank': 5},{'suit': 'Hearts', 'rank': 'Jack'}]
        d_hand = [{'suit': 'Hearts', 'rank': 'Ace'},{'suit': 'Hearts', 'rank': 10},{'suit': 'Hearts', 'rank': 'Jack'}]
        p = game.calculate_hand_value(p_hand) #16
        d = game.calculate_hand_value(d_hand) #21
        self.assertEqual(game.who_wins(p, d), 'Dealer has 21 \nYou Lose')


        game = Blackjack()
        p_hand = [{'suit': 'Hearts', 'rank': 'Ace'},{'suit': 'Hearts', 'rank': 5},{'suit': 'Hearts', 'rank': 'Jack'}]
        d_hand = [{'suit': 'Hearts', 'rank': 10},{'suit': 'Hearts', 'rank': 10},{'suit': 'Hearts', 'rank': 'Jack'}]
        p = game.calculate_hand_value(p_hand) #16
        d = game.calculate_hand_value(d_hand) #30
        self.assertEqual(game.who_wins(p, d), 'Dealer has 30 \nYou Win')


        game = Blackjack()
        p_hand = [{'suit': 'Hearts', 'rank': 10},{'suit': 'Diamonds', 'rank': 10},{'suit': 'Hearts', 'rank': 'Jack'}]
        d_hand = [{'suit': 'Hearts', 'rank': 1},{'suit': 'Hearts', 'rank': 10},{'suit': 'Hearts', 'rank': 'Jack'}]
        p = game.calculate_hand_value(p_hand)
        d = game.calculate_hand_value(d_hand) 
        self.assertEqual(p, 30)
        self.assertEqual(d, 21)
        self.assertEqual(game.who_wins(p, d), 'Dealer has 21 \nYou Lose')


    def test_start_game(self):
        game = Blackjack()
        game.start_game()
        self.assertEqual(len(game.deck), 48)
        self.assertEqual(len(game.player_hand), 2)
        self.assertEqual(len(game.dealer_hand), 2)


    def test_hit(self):
        game = Blackjack()
        game.start_game()
        game.hit()
        self.assertEqual(len(game.deck), 46)
        game.hit()
        self.assertEqual(len(game.deck), 44)

        game = Blackjack()
        count = 0
        while len(game.deck) > 0:
            game.hit()
            count += 1
        self.assertEqual(count, 26)
        self.assertEqual(len(game.dealer_hand), 26)
        self.assertEqual(len(game.player_hand), 26)

unittest.main()