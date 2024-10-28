import random

SEARCH_DEPTH = 0xFFFFFF           # Amount of seeds to search.
MAX_RANINT = 0x7FFF               # Max RNG value.
uinput = []                       # User input

a = int(input("Amount: "))

uinput = [int(input(f"{i + 1}: ")) for i in range(a)]

print(f"\nUser input: {uinput} \nSearch depth: {SEARCH_DEPTH} \nMax RNG value: {MAX_RANINT}")      # Debug info
print("\nProgress is in percent")

# Convert uinput to a tuple for faster comparisons
uinput_tuple = tuple(uinput)

for i in range(SEARCH_DEPTH):
    random.seed(i)
    
    generated = tuple(random.randint(0, MAX_RANINT) for _ in range(a))
    
    if generated == uinput_tuple:
        print(uinput, generated, "Seed:", i)
        break
    
    # print progress without clearing buffer
    if i % (SEARCH_DEPTH // 1000) == 0:  # print progress every 0.1%
        print(f"{round((i / SEARCH_DEPTH) * 100, 1)}%", end="\r")
