from random import randint

ACCOUNTS = {}

class Account:
    def __init__(self, card, pin, balance=0):
        self.card = card
        self.pin = pin
        self.balance = balance
        self.card_num = card_num(card)


class Card:
    def __init__(self, can, checksum="8"):
        self.iin = "400000"
        self.can = can
        self.checksum = checksum


def print_menu():
    print("""1. Create an account
2. Log into account
0. Exit\n""")


def print_account_menu():
    print("""1. Balance
2. Log out
0. Exit""")


def card_num(card):
    card_num = card.iin + card.can + card.checksum
    return card_num


def gen_card():
    can = str(randint(100000000, 999999999))
    card = Card(can)
    return card


def gen_pin():
    pin = str(randint(1000, 9999))
    return pin


def gen_account():
    card = gen_card()
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
    if card_number in ACCOUNTS and ACCOUNTS[card_number].pin == pin:
        print("You have successfully logged in!")
        choice = account_menu(ACCOUNTS[card_number])
    else:
        print("Wrong card number or PIN!\n")
    return choice

def bank_main(choice):
    while choice != 0:
        print_menu()
        choice = int(input())
        if choice == 1:
            account = gen_account()
            ACCOUNTS[str(account.card_num)] = account
        elif choice == 2:
            choice = login()
        return choice


def account_menu(account):
    print_account_menu()
    choice = int(input())
    while choice == 1:
        print(f'Balance: {account.balance}')
        print_account_menu()
        choice = int(input())
    if choice == 2:
        print("You have successfully logged out!")

        return None
    if choice == 0:
        return 0


choice = None
while choice != 0:
    choice = bank_main(choice)
print("Bye!")







