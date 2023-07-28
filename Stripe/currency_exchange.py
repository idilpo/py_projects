

def currency_converter(a, b, c):
    EUR_to_USD = 0.9591
    GBP_to_USD = 1.0719
    SPK_to_USD = 1.1052

    if b == "USD":
        if c == "EUR":
            a *= EUR_to_USD
        elif c == "GBP":
            a *= GBP_to_USD
        elif c == "SPK":
            a *= SPK_to_USD
        else:
            print("Currency is not valid.")
    elif b == "EUR":
        if c == "EUR":
            pass
        elif c == "GBP":
            a = (a/GBP_to_USD) * EUR_to_USD
        elif c == "SPK":
            a = (a/SPK_to_USD) * EUR_to_USD
        elif c == "USD":
            a = a * EUR_to_USD
        else:
            print("Currency is not valid.")
    elif b == "GBP":
        if c == "EUR":
            a = (a/EUR_to_USD) * GBP_to_USD
        elif c == "GBP":
            pass
        elif c == "SPK":
            a = ( a/SPK_to_USD) * GBP_to_USD
        elif c == "USD":
            a = a * GBP_to_USD
        else:
            print("Currency is not valid.")
    elif b == "SPK":
        if c == "EUR":
            a = (a/EUR_to_USD) * SPK_to_USD
        elif c == "GBP":
            a = (a/GBP_to_USD) * SPK_to_USD
        elif c == "SPK":
            pass
        elif c == "USD":
            a = a * SPK_to_USD
        else:
            print("Currency is not valid.")
    else:
        print("Bank is not valid.")
    return a


def given_func(part, availableBanks, charges):
    money = charges[11:18]
    currency = charges[len(charges)-3:len(charges)]

    bank = availableBanks[0]
    if currency == bank:
        amount = currency + ", " + money
    else:
        amount = float(money)
        money = currency_converter(amount, bank, currency)
        amount = currency + ", " + str(round(money))
    return amount


#print(given_func("part_one", ["USD", "EUR", "GBP"], "2022-12-21_1308.02_EUR"))
#print(given_func("part_one", ["USD", "EUR", "GBP"], "2022-12-21_1308.02_EUR"))


def transaction_time(charges):
    date = charges[:10]
    currency = charges[len(charges)-3:len(charges)]

    if currency == "USD":
        days = 0
    elif currency == "EUR":
        days = 1
    elif currency == "GBP":
        days = 2
    elif currency == "SPK":
        days = 3
    else:
        print("Invalid currency.")
    return days

# print(transaction_time("2022-12-21_1308.02_EUR"))
