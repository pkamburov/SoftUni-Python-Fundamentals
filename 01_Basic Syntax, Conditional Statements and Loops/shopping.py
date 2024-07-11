budget = int(input())
word = input()

while word != "End":
    price = int(word)
    budget -= price
    if budget < 0:
        print(f"You went in overdraft!")
        break
    word = input()
else:
    print(f"You bought everything needed.")
