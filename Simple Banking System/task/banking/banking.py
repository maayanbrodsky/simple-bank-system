from random import randint


MAIN_MENU = ("""1. Create an account
2. Log into account
0. Exit\n""")

ACCOUNT_MENU = ("""1. Balance
2. Log out
0. Exit\n""")

IIN = "400000"


class Account:
    def __init__(self, card, pin, balance=0):
        self.card = card
        self.pin = pin
        self.balance = balance
        self.card_num = card_num(card)


class Card:
    def __init__(self,iin, can, checksum):
        self.iin = iin
        self.can = can
        self.checksum = checksum


def double_odds(num):
    digits = list(num)
    doubled = []
    i = 0
    for digit in digits:
        digit = int(digit)
        if i % 2 == 0:
            digit = digit * 2
        i += 1
        doubled.append(digit)
    return doubled


def substract_9(num):
    digits = num
    new_digits = []
    for digit in digits:
        if digit > 9:
            digit -= 9
        new_digits.append(digit)
    return new_digits


def gen_checksum(num):
    doubled = double_odds(num)
    subtracted = substract_9(doubled)
    digit_sum = sum(subtracted)
    print(digit_sum)
    checksum = 0
    if (digit_sum + checksum) % 10 == 0:
        print(checksum)
        return str(checksum)
    else:
        while (digit_sum + checksum) % 10 != 0:
            checksum +=1
        print(checksum)
    return str(checksum)



def card_num(card):  #This will need to be changed
    card_num = card.iin + card.can + card.checksum
    return card_num


def gen_card(iin):
    can = str(randint(0, 999999999)).zfill(9)
    checksum = gen_checksum(can)
    card = Card(iin, can, checksum)
    return card


def gen_pin():
    pin = str(randint(0, 9999)).zfill(4)
    return pin


def gen_account():
    card = gen_card(IIN)
    pin = gen_pin()
    account = Account(card, pin)
    print(f"""Your card has been created
Your card number:
{account.card_num}
Your card PIN:
{account.pin}\n""")
    return account


def login():
    card_number = input("Enter your card number: ")
    choice = None
    pin = input("Enter you PIN: ")
    if card_number in accounts and accounts[card_number].pin == pin:
        print("You have successfully logged in!")
        choice = account_menu(accounts[card_number])
    else:
        print("Wrong card number or PIN!\n")
    return choice


def bank_main(choice):
    while choice != 0:
        print(MAIN_MENU)
        choice = int(input())
        if choice == 1:
            account = gen_account()
            accounts[str(account.card_num)] = account
        elif choice == 2:
            choice = login()
        return choice


def account_menu(account):
    print(ACCOUNT_MENU)
    choice = int(input())
    while choice == 1:
        print(f'Balance: {account.balance}')
        print(ACCOUNT_MENU)
        choice = int(input())
    if choice == 2:
        print("You have successfully logged out!")

        return None
    if choice == 0:
        return 0


accounts = {}

choice = None
while choice != 0:
    choice = bank_main(choice)
print("Bye!")







