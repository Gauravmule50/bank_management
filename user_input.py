import random

#globle variable
mainBalance = 0.0
data = dict()

def create_acc():
    name = input("Enter name: ")

    age = int(input('Enter age: '))
    if(age <= 18):
        print('You can not created acc')
    else:
        print('Account created successfully')

        account_no = random.randint(100000, 999999)
        password = random.randint(100, 999)
        print("\nAcc number: ", account_no)
        print("Password: ", password)

        data.update({str(account_no): {
                                'name': name,
                                'account_no': account_no,
                                'password': password,
                                'balance': mainBalance
                                 }
                    })
        print(data)
        print('*****'.center(60, "-"))

def deposit(index):
    deposit1 = int(input('Enter deposit amount: '))
    data[index]['balance'] = data[index]['balance'] + deposit1
    print('account balance: ', data[index]['balance'])
    print(data[index])
    print('*****'.center(60, "-"))

def withdraw(index):
    amount = int(input('\nEnter amount: '))
    data[index]['balance'] = data[index]['balance'] - amount
    print('account balance: ', data[index]['balance'])
    print(data[index])
    print('*****'.center(60, "-"))

def balance_check(index):
    print("\nBalance: ", data[index]['balance'])
    print(data[index])
    print('*****'.center(60, "-"))

def user_info(index):
    print(data[index])
    print('*****'.center(60, "-"))


print("1. create a account \n2. deposit \n3. withdraw \n4. balance check \n5. Users Information \n6. Exit")
user = int(input('What do u want: '))

while(user != 6):
    if (user == 1):
        create_acc()

        print("\n1. create a account \n2. deposit \n3. withdraw \n4. balance check \n5. Users Information \n6. Exit")
        user = int(input('What do u want: '))

    elif(user == 2):
        account_no = input('Enter acc number: ')

        for i in data:
            if (i == account_no):
                deposit(i)

        print("\n1. create a account \n2. deposit \n3. withdraw \n4. balance check \n5. Users Information \n6. Exit")
        user = int(input('What do u want: '))

    elif(user == 3):
        account_no = int(input('Enter acc number: '))
        password = int(input('Enter password: '))

        for i in data:
            if (data[i]['account_no'] == account_no and data[i]['password'] == password):
                withdraw(i)

        print("\n1. create a account \n2. deposit \n3. withdraw \n4. balance check \n5. Users Information \n6. Exit")
        user = int(input('What do u want: '))

    elif(user == 4):
        account_no = int(input('Enter acc number: '))
        password = int(input('Enter password: '))

        for i in data:
            if (data[i]['account_no'] == account_no and data[i]['password'] == password):
                balance_check(i)

        print("\n1. create a account \n2. deposit \n3. withdraw \n4. balance check \n5. Users Information \n6. Exit")
        user = int(input('What do u want: '))

    elif(user == 5):
        account_no = input('Enter acc number: ')

        for i in data:
            if (i == account_no):
                user_info(i)

        print("\n1. create a account \n2. deposit \n3. withdraw \n4. balance check \n5. Users Information \n6. Exit")
        user = int(input('What do u want: '))