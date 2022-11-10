import random

mainBalance = 0.0
data = dict()

def create_acc():
    global data
    name = input("Enter name: ")
    age = int(input('Enter age: '))

    if(age <= 18):
        print('You can not created acc')
    else:
        account_no = random.randint(10000, 99999)
        for i in data:
            if (account_no == int(i)):
                print("account number already exits")
                create_acc()
        else:
            print('\nAccount created successfully')
            password = random.randint(100, 999)
            print("Acc number: ", account_no)
            print("Password: ", password)

            data.update({str(account_no):{
                                    'name': name,
                                    'account_no': account_no,
                                    'password': password,
                                    'balance': mainBalance
                                     }
                        })

            print(data)
            print('*****'.center(100, "-"))


def deposit(index):
    deposit1 = int(input('Enter deposit amount: '))
    data[index]['balance'] = data[index]['balance'] + deposit1
    print('account balance: ', data[index]['balance'])
    print(data[index])
    print('*****'.center(100, "-"))

def withdraw(index):
    amount = int(input('\nEnter amount: '))
    data[index]['balance'] = data[index]['balance'] - amount
    print('account balance: ', data[index]['balance'])
    print(data[index])
    print('*****'.center(100, "-"))

def balance_check(index):
    print("\nBalance: ", data[index]['balance'])
    print(data[index])
    print('*****'.center(100, "-"))

def user_info(index):
    print(data[index])
    print('*****'.center(100, "-"))