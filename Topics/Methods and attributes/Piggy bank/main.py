class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        total_cents = self.cents + deposit_cents
        if total_cents >= 100:
            dollars = total_cents // 100
            cents = total_cents % 100
            self.dollars += (dollars + deposit_dollars)
            self.cents += cents - 1
        else:
            self.dollars += deposit_dollars
            self.cents += deposit_cents