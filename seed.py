import random

SEARCH_DEPTH = 0xFFFFFF         # Amount of seeds to search. Will also be used to get progress in %.
MAX_RANINT = 0x7FFF             # This variable will change the max rng value.
uinput = []                     # User input
buffer = []

#    Amount of inputs    #
a = int(input("Amount: "))
# ---------------------- #

for i in range(0, a):
    print(i+1, end="")
    uinput.append(int(input(": ")))


print(f"\nUser input: {uinput} \nSearch depth: {SEARCH_DEPTH} \nMax RNG value: {MAX_RANINT}")      # Debug, remove if you want
print("\nProgress is in percent")                                                                  # --||--

for i in range(0, SEARCH_DEPTH):
    random.seed(i)
    for j in range(0, a):
        buffer.append(random.randint(0, MAX_RANINT))
    if uinput == buffer:
        print(uinput, buffer, "Seed:", i)
    else:
        buffer.clear()
        print(round((i/SEARCH_DEPTH)*100, 1), end="\r ") 
