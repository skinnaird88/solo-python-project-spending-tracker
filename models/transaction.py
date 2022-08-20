class Transaction:

    def __init__(self, description, type, amount, merchant, id = None):
        self.description = description
        self.type = type
        self.amount = amount
        self.merchant = merchant
        self.id = id