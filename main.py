usd = 72.42
eur = 83.83

def rub_to_usd(amount):
    try:
        return amount / usd
    except ZeroDivisionError:
        return "The USD exchange rate cannot be zero."

def rub_to_eur(amount):
    try:
        return amount / eur
    except ZeroDivisionError:
        return "The EUR exchange rate cannot be zero."

print("1. Convert to USD:\n2. Convert to EUR:")
action = int(input("Enter action(number): "))

if action == 1:
    enter = int(input("Enter number: "))
    result = rub_to_usd(enter)
    print(result)

elif action == 2:
    enter = int(input("Enter number: "))
    result = rub_to_eur(enter)
    print(result)