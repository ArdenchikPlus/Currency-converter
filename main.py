# 1. Сначала объявляем курсы валют
usd = 72.42
eur = 83.83

# 2. Объявляем функции для расчета (переменные вводим ВНЕ функций)
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

