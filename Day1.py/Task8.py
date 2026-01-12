balance=10000
amoumt=int(input("Enter amount to withdraw:"))
if amount <= balance:
    bal=balance - amount
    print("amount withdrawn:",amount,",available balance:",bal)
else:
    print("Insufficient balance")
