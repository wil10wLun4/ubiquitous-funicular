from random import randint

amount = int(input("How many coins?: "))

flips = []

heads = (0)

tails = (0)

for i in range(amount):
    HorT = randint(0, 2)
    if HorT == 0:
        flips.append("Heads")
    else:
        flips.append("Tails")

for x in flips:
    if x == "Heads":
        heads += 1
    else:
        tails += 1

print(f"You fliped {amount} coins and got {heads} heads and {tails} tails:")
print(flips)
