from random import randint

class Account:
    def __init__(self, card, pin, balance=0):


class Card:
    def __init__(self, can, checksum="8"):
        self.iin = "400000"
        self.can = can
        self.checksum = checksum


def print_menu():
    print("""1. Create an account
    2. Log into account
    0. Exit""")


def print_card(card):
    card_num = card.iin + card.can + card.checksum
    print(card_num)


def gen_card():
    can = str(randint(100000000, 999999999))
    card = Card(can)
    # print_card(card)
    return card


def gen_pin():
    pin = str(randint(1000, 9999))
    return pin


def gen_account():
    card = gen_card()
    pin = gen_pin()
#
# choice = int(input("Please choose option: "))
#
# if choice is 1

print(gen_card())