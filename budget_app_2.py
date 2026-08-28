class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        lines = []
        cate_len = len(self.name)
        half_len = (30-cate_len)//2
        header = f"{'*'* half_len}{self.name}{'*'* half_len}"
        lines.append(header)

        for dics in self.ledger:
            amt = dics['amount']
            desc = dics['description'][:23]
            line = f"{desc:<23}{('%.2f'%(amt)):>7}"
            lines.append(line)
        total = f"Total: {round(self.get_balance(), 2)}"
        lines.append(total)
        return "\n".join(lines)

    def deposit(self, amount, description = ""):
        self.amount = amount
        self.description = description
        self.ledger.append({'amount': self.amount, 'description': self.description})

    def withdraw(self, amount, description= ""):
        self.amount = -amount
        self.description = description
        if self.check_funds(amount):
            self.ledger.append({'amount': self.amount, 'description': self.description})
            return True
        else:
            return False

    def get_balance(self):
        self.balance = 0
        for amount in self.ledger:
            self.balance += amount['amount']
        return self.balance

    def transfer(self, amount, category):
        # self.amount = amount
        if self.check_funds(amount):
            self.withdraw(amount, (f"Transfer to {category.name}"))
            category.deposit(amount, (f"Transfer from {self.name}"))
            return True
        else:
            return False
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    def total_deposit(self):
        total = 0
        for i in self.ledger:
             if i['description'] == 'deposit' or i['amount'] > 0:
                 total += i['amount']
        return total
def create_spend_chet(categories: list):
    print("Percentage spent by category")
    for _ in range(100, -1, -10):
        for l in range(len(categories)):
            a =  categories[l].total_deposit() - categories[l].get_balance()
            b = categories[l].total_deposit()
            
            if ( a // b ) * 100 <= _:
                print(f"{_:>3}|  o")
    

food = Category("food")
food.deposit(900, 'deposit')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
cloth = Category("Clothing")
food.transfer(50, cloth)
print(food.get_balance())
create_spend_chet([food, cloth])
