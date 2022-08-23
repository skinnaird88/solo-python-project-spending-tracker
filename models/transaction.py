class Transaction:

    def __init__(self, name, tag, amount, merchant, id = None):
        self.name = name
        self.tag = tag
        self.amount = amount
        self.merchant = merchant
        self.id = id