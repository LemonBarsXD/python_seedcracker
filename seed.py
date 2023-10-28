import random

SEARCH_DEPTH = 0xFFFF         # How many seeds do you want to search?
MAX_RANINT = 0xFFFF             # This variable will change the max rng value, default is 0xFFFF or 65535 or 0b1111111111111111
uinput = []

#    Amount of inputs    #
a = int(input("Amount: "))
# ---------------------- #

for i in range(0, a):
    print(i+1, end="")
    uinput.append(int(input(": ")))

# magic
print("\nProgress is in percent")
for i in range(0, SEARCH_DEPTH):
    random.seed(i)
    for items in uinput:
        if random.randint(0, MAX_RANINT) == items:
            print("Seed: ", i)
        else: 
            print(round((i/SEARCH_DEPTH)*100, 1), end="\r ")
