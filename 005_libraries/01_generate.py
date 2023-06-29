import random

heads_counter = 0
tails_counter = 0

for _ in range(1000000):
    coin = random.choice(["heads", "tails"])
    if coin == "heads":
        heads_counter += 1
    else:
        tails_counter += 1

print("results:")
print(f"heads: {heads_counter}")
print(f"tails: {tails_counter}")

