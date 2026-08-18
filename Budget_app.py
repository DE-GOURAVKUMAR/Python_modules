class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        cate_len = len(self.name)
        half_len = (30-cate_len)//2
        print(f"{'*'* half_len}{self.name}{'*'* half_len}")
    
    def __str__(self):
        return f"Total: {round(self.get_balance(), 2)}"
        
    def deposit(self, amount, description = ""):
        self.amount = amount
        self.description = description
        # des_len = len(self.description)
        # half_des = (23-des_len)
        sliced = description[:23]
        data = {'amount': self.amount, 'description': self.description}
        self.ledger.append(data)
        print(f"{sliced:<23}{('%.2f'%(self.amount)):>7}")
       

    def withdraw(self, amount, description= ""):
        self.amount = -amount
        self.description = description
        sliced = description[:23]
        if self.check_funds(amount):
            data_1 = {"amount": self.amount, "description": self.description}
            self.ledger.append(data_1)
            print(f"{sliced:<23}{('%.2f' % self.amount):>7}")
            return True   
        else:
            return False
    def get_balance(self):
        self.balance = 0
        for i in range(0, len(self.ledger)):
            self.balance += self.ledger[i]['amount']
        return self.balance
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False   

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    
       





def create_spend_chart(categories):
    pass

p1 = Category("food")

# p2 = Category("clothing")
p1.deposit(900, 'deposit')
p1.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
clothing = Category("clothing")
p1.transfer(50, clothing)
print(p1)