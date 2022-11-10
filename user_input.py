import function_module as f

print("1. create a account      2. deposit      3. withdraw     4. balance check        5. Users Information        6. Exit")
user = int(input('What do u want: '))

while(user != 6):
    if (user == 1):
        f.create_acc()

        print("\n1. create a account      2. deposit      3. withdraw     4. balance check        5. Users Information        6. Exit")
        user = int(input('What do u want: '))

    elif(user == 2):
        account_no = input('Enter acc number: ')

        for i in f.data:
            if (i == account_no):
                f.deposit(i)

        print("\n1. create a account      2. deposit      3. withdraw     4. balance check        5. Users Information        6. Exit")
        user = int(input('What do u want: '))

    elif(user == 3):
        account_no = int(input('Enter acc number: '))
        password = int(input('Enter password: '))

        for i in f.data:
            if (f.data[i]['account_no'] == account_no and f.data[i]['password'] == password):
                f.withdraw(i)

        print("\n1. create a account      2. deposit      3. withdraw     4. balance check        5. Users Information        6. Exit")
        user = int(input('What do u want: '))

    elif(user == 4):
        account_no = int(input('Enter acc number: '))
        password = int(input('Enter password: '))

        for i in f.data:
            if (f.data[i]['account_no'] == account_no and f.data[i]['password'] == password):
                f.balance_check(i)

        print("\n1. create a account      2. deposit      3. withdraw     4. balance check        5. Users Information        6. Exit")
        user = int(input('What do u want: '))

    elif(user == 5):
        account_no = input('Enter acc number: ')

        for i in f.data:
            if (i == account_no):
                f.user_info(i)

        print("\n1. create a account      2. deposit      3. withdraw     4. balance check        5. Users Information        6. Exit")
        user = int(input('What do u want: '))