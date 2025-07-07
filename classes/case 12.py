from datetime import datetime


class Transaction:
    def __init__(self, amount, category, description, type, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.type = type
        self.date = date

    def display(self):
        return (
            f"Transaction(amount: {self.amount},"
            f" category: {self.category}, description: {self.description},"
            f" type: {self.type}, date: {self.date})"
        )


class FinanceManager:
    def __init__(self):
        self.transactions = []
        self.FileName = "transaction.json"
        self.date_format = "%Y-%m-%d"

    def add_transaction(self, amount, category, description, type, date):
        transaction = Transaction(
            amount,
            category,
            description,
            type,
            datetime.strptime("2025-01-20", self.date_format),
        )
        self.transactions.append(transaction)

    def view_transactions(self, filter_type=None):
        for transaction in self.transactions:
            if transaction.type is filter_type:
                print(transaction.display())
            else:
                print(transaction.display())

    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            if transaction.type in ("income", "investment"):
                balance += transaction.amount
                # print(f'{balance} toatal amount')
            elif transaction.type == "expense":
                balance -= transaction.amount
                # print(f'{balance} ramaining amount')
        return balance
        


manager = FinanceManager()
manager.add_transaction(1500.00, "Salary", "Monthly paycheque", "income", "2025-01-19")
manager.add_transaction(45.50, "Food", "Groceries", "expense", "2025-01-15")
manager.add_transaction(250.00, "Utilities", "Electricity", "expense", "2025-01-11")
manager.add_transaction(0, "Travel", "Bus fare", "expense", "2025-01-20")
manager.add_transaction(100, "Books", "New novel", "investment", "2025-01-15")
manager.view_transactions()
print(manager.get_balance())
