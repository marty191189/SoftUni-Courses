cards = input().split(" ")
shuffles = int(input())

# create a deck without the first and last card
shuffled_cards = cards.copy()
shuffled_cards.pop(0)
shuffled_cards.pop(len(shuffled_cards) - 1)

first_half = []
second_half = []

# shuffle
for k in range(shuffles):

    # splitting the cards in 2 piles
    for i in range(len(shuffled_cards)):
        if i < len(shuffled_cards) / 2:
            first_half.append(shuffled_cards[i])
        else:
            second_half.append(shuffled_cards[i])

    shuffled_cards.clear()

    # merging the two piles into one shuffled pile
    for j in range(len(first_half)):
        shuffled_cards.append(second_half[j])
        shuffled_cards.append(first_half[j])

    first_half.clear()
    second_half.clear()

# putting back the fist and last card
shuffled_cards.insert(0, cards[0])
shuffled_cards.append(cards[len(cards) - 1])

print(shuffled_cards)

# 2

# deck = input().split(" ")
# shuffles = int(input())
# new_deck = []
#
# for i in range(shuffles):
#     new_deck = []
#     first_half = deck[:len(deck)//2]
#     second_half = deck[len(deck)//2:]
#
#     first_half.pop(0)
#     second_half.pop(-1)
#
#     for (a, b) in zip(second_half, first_half):
#         new_deck.append(a)
#         new_deck.append(b)
#
#     new_deck.insert(0, deck[0])
#     new_deck.append(deck[-1])
#     deck = new_deck
#
# print(new_deck)

# 3

# deck = input().split(" ")
# shuffles = int(input())
# for _ in range(shuffles):
#     shuffle_deck = []
#     left_half = deck[0:int(len(deck) / 2)]
#     right_half = deck[int(len(deck) / 2)::]
#     for i in range(int(len(deck) / 2)):
#         shuffle_deck.append(left_half[i])
#         shuffle_deck.append(right_half[i])
#     deck = shuffle_deck
# print(deck)
