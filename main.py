enter = int(input("Enter number: "))
usd = 72.42  #rub

def rub_to_usd(amount):
    try:
        number = amount / usd
        return number
    except ZeroDivisionError:
        return "The USD exchange rate cannot be zero."

result = rub_to_usd(enter)
print(result)

