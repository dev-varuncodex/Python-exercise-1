
accounts = []
a = ''
while a != '5':
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Account")
    print("5. Exit")

    a = input("Choose (1-5): ")
    if a == '1':
        name = input("Store Name: ")
        number = input("Account Number: ")
        acc = 0
        for i in accounts:
            if i['number'] == number:
                acc = 'yes'

        if acc == 'yes':
            print("Account number already exists")
        else:
            balance = float(input("Initial Balance: "))
            accounts.append({'name': name, 'number': number, 'balance': balance})
            print("Account created")

    elif a == '2':
        number = input("Account Number: ")
        b = 0
        for i in accounts:
            if i['number'] == number:

                amount = float(input("Deposit Amount: "))
                if amount > 0:
                    i['balance'] += amount
                    print("Amount Deposited")
                else:
                    print("Enter positive number!")
            if b == 0:
                print("Account not available!")

    elif a == '3':
        number = input("Account Number: ")
        b = 0
        for i in accounts:
            if i['number'] == number:
                amount = float(input("Withdraw Amount: "))
                if amount > 0:
                    if amount <= i['balance']:
                        i['balance'] -= amount
                        print("Amount Withdrawn")
                    else:
                        print("Not enough balance")
                else:
                    print("Enter positive number")
            if b == 0:
                print("Account not available")

    elif a == '4':
        number = input("Account Number: ")
        b = 0
        for i in accounts:
            if i['number'] == number:
                print("Name:", i['name'])
                print("Account Number:", i['number'])
                print("Balance:", i['balance'])
            if b == 0:
                print("Account not available")

    elif a == '5':
        print("Exit")

    else:
        print("Invalid a!")
