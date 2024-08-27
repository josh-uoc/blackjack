import math
import numpy as np
import random
import time


# Define cards and values
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


# Strategy chart here?


# Initialize for six decks
def initialize_deck():
    return cards * 6


# Create function to deal a card
def deal_card(deck):
    return deck.pop(random.randint(0, len(deck)-1))


# Create function to calculate hand value
def calculate_hand_value(hand):
    total_value = sum(card_values[card] for card in hand)
    # Aces
    num_aces = hand.count("A")
    while total_value > 21 and num_aces:
        total_value -= 10
        num_aces -= 1
    return total_value


# Create function to play Blackjack
def play_blackjack():
  player_win = 0
  dealer_win = 0
  push = 0
  #bankroll = int(input("Starting bankroll: "))

  while True:

    print("________________________")
    print()
    print("*000* | NEW GAME | *000*\n")
    # Initialise for each game (SkyBet rules)
    deck = initialize_deck()
    random.shuffle(deck)

    # Deal
    player_hand = [deal_card(deck), deal_card(deck)]  ##   HARDCODED FOR TESTING
    dealer_hand = [deal_card(deck), deal_card(deck)]


    # Check if player has blackjack
    if calculate_hand_value(player_hand) == 21 and calculate_hand_value(dealer_hand) != 21:
      print("Players hand: ", player_hand)
      print("Dealers hand: ", [dealer_hand[0], "??"])
      print("Player has blackjack, dealer does not. Player win.\n")
      player_win += 1
      print("Player wins: ", player_win)
      print("Dealer wins: ", dealer_win)
      print("Number of pushes: ", push)
      print()
      continue

    elif calculate_hand_value(dealer_hand) == 21 and calculate_hand_value(player_hand) != 21:
      print("Players hand: ", player_hand)
      print("Dealers hand: ", dealer_hand)
      print("Dealer has blackjack, player does not. Dealer win.\n")
      dealer_win += 1
      print("Player wins: ", player_win)
      print("Dealer wins: ", dealer_win)
      print("Number of pushes: ", push)
      print()
      continue

    # Show cards
    print("Players hand: ", player_hand)
    print("Dealers hand: ", [dealer_hand[0], "??"])

    # Check for pair
    if player_hand[0] == player_hand[1]:
      action = input("Split the pair? : ").strip().lower()

      if action == "yes":
        player_hand_split = [player_hand[0], deal_card(deck)]
        player_hand = [player_hand[1], deal_card(deck)]

        print("\nSPLIT HANDS")
        print("Players first hand: ", player_hand)
        print("Players second hand: ", player_hand_split)

        # Play each split hand
        for hand in [player_hand, player_hand_split]:
           print("\nCURRENT HAND")
           print("Current hand: ", hand)

           # Game loop for current split hand
           while True:
              if calculate_hand_value(hand) == 21:
                print("Player has 21.")
                break

              action = input("Hit or stand? : ").strip().lower()

              if action == "hit":
                hand.append(deal_card(deck))
                print("Players hand: ", hand)
                if calculate_hand_value(hand) > 21:
                    print("\nBust. Hand: ", hand)
                    break
              elif action == "stand":
                break

        # Compare each split hand against the dealer's hand
        for hand in [player_hand, player_hand_split]:
            player_total = calculate_hand_value(hand)
            print("\nHAND VALUE")
            print("Hand value: ", player_total)

            if player_total > 21:
              print("Bust: ", hand)
              dealer_win += 1
            else:
                while calculate_hand_value(dealer_hand) < 17:
                    dealer_hand.append(deal_card(deck))
                    print("Dealer hits: ", dealer_hand)
                dealer_total = calculate_hand_value(dealer_hand)
                print("Dealer value: ", dealer_total)

                if dealer_total > 21 or player_total > dealer_total:
                    print("Player win.\n")
                    player_win += 1
                elif player_total < dealer_total:
                    print("Dealer win.\n")
                    dealer_win += 1
                else:
                    print("Push.\n")
                    push += 1

        print("Player wins: ", player_win)
        print("Dealer wins: ", dealer_win)
        print("Number of pushes: ", push)
        print()
        continue
        
  # Game loop
    while True:  
      player_total = calculate_hand_value(player_hand)
      
      # Players turn
      if player_total > 21:
        print("Player bust. Dealer wins.\n")
        dealer_win += 1
        break

      if player_total == 21:
        print("Player has 21.")
        break
      
      while player_total < 21:
        action = input("Hit or stand? : ").strip().lower()
  
        if action == "hit":
            player_hand.append(deal_card(deck))
            print("Players hand: ", player_hand)

            player_total = calculate_hand_value(player_hand)
  
            if player_total > 21:
              print("\nBust. Dealers hand: ", dealer_hand)
              dealer_win += 1
              break
  
        elif action == "stand":
          print()
          break
      if player_total <=21:
        # Dealers turn
        print("Dealers hand: ", dealer_hand)
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))
            print("Dealer hits: ", dealer_hand)
    
            if calculate_hand_value(dealer_hand) > 21:
                break
    
        # Compare for winner
        player_total = calculate_hand_value(player_hand)
        dealer_total = calculate_hand_value(dealer_hand)
    
        if player_total == 21 or (player_total < 21 and (player_total > dealer_total)):
          print("\nPlayer win.\n")
          player_win += 1
    
        elif player_total < dealer_total and dealer_total <= 21:
          print("\nDealer stands; Dealer win.\n")
          dealer_win += 1
        elif player_total == dealer_total:
          print("\nPush.\n")
          push += 1
        elif player_total > 21:
          print("\nPlayer bust. Dealer win.\n")
          dealer_win += 1
        elif dealer_total > 21:
          print("\nDealer bust. Player win.\n")
          player_win += 1
    
        print("Player wins: ", player_win)
        print("Dealer wins: ", dealer_win)
        print("Number of pushes: ", push)
        print()
        print()
        break

# Function for split ?
  



play_blackjack()

