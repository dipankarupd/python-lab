# write a program to:
# a. shuffle a deck of cards
# b. to choose a single card from the deck
# b. to choose one single card form the deckc. to create a 
#     sample of size 2 from the available deck of cards

import random

# Function to shuffle the deck of cards
def shuffle_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    deck = [(rank, suit) for rank in ranks for suit in suits]
    print(deck)
    random.shuffle(deck)
    
    return deck

# Function to choose a single card from the deck
def choose_single_card(deck):
    card = random.choice(deck)
    return card

# Function to create a sample of size 2 from the available deck of cards
def create_sample(deck, sample_size):
    sample = random.sample(deck, sample_size)
    return sample

# Shuffle the deck of cards
deck = shuffle_deck()
print(deck)

# Choose a single card from the deck
single_card = choose_single_card(deck)
print("Single Card:", single_card)

# Create a sample of size 2 from the available deck of cards
sample_size = 2
sample = create_sample(deck, sample_size)
print("Sample of Size 2:", sample)
