import string


def luhnAlgorithm(cardInput):
    cardNumber = list(cardInput)
    cardNumber = [int(i) for i in cardNumber]
    checkDigit = cardNumber[-1]
    del cardNumber[-1]
    n = 0
    while n < len(cardNumber):
        cardNumber[n] = cardNumber[n] * 2
        n = n + 2
    for k in cardNumber:
        if k > 9:
            k = str(k)
            k = list(k)
            k = [int(j) for j in k]
            k = sum(k)
            cardNumber.append(k)
        else:
            pass
    for i in cardNumber:
        if i > 9:
            index = cardNumber.index(i)
            del cardNumber[index]
        else:
            pass
    total = sum(cardNumber)
    final = total + checkDigit
    if final % 10 == 0:
        print("Valid")
    else:
        print("Not Valid")


userInput = input("What is your card number ")
userInput = userInput.replace(" ", "")
print(luhnAlgorithm(userInput))
