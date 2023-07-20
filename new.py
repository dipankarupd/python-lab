# import random

# def shuffle():
#     cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
#     types = ['heart','club','spade','diamond']

#     card_deck = [(cards,types) for card in cards for typ in types]
#     random.shuffle(card_deck)
#     return card_deck

# def chooseCard(deck):
#     card = random.choice(deck)
#     return card

# def createSample(deck):
#     new_sample = random.sample(deck,2)
#     return new_sample


# def main():
#     deck = shuffle()
    
#     single_card = chooseCard(deck)
#     print('the card drawn is: ', single_card)

#     sample = createSample(deck,2)
#     print('sample is: ', sample)

# main()