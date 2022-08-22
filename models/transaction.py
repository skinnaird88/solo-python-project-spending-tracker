class Transaction:

    def __init__(self, name, type, amount, merchant, id = None):
        self.name = name
        self.type = type
        self.amount = amount
        self.merchant = merchant
        self.id = id