import random

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(f"number: {number}")

# shuffles in place
cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)

