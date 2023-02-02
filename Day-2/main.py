import inflect
p = inflect.engine()

print("Welcome to the tip calculator.")
while True:
    try:
        bill = float(input("What was the total bill? $"))
        break
    except:
        pass
tipOptions = [10, 12, 15]
while True:
    try:
        tip = int(input(f"What percentage tip would you like to give? {p.join(tipOptions, conj='or')}? "))
        if tip in tipOptions:
            break
    except:
        pass
while True:
    try:
        people = int(input("How many people to split the bill? "))
        break
    except:
        pass

amount = (bill * (tip /100+1)) / people
print(f"Each person should pay: ${round(amount, 2):.2f}")


