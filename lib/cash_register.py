#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, title, price, quantity=1):
        transaction_total = price * quantity
        self.total += transaction_total
        self.items.extend([title] * quantity)
        self.last_transaction = transaction_total

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print("After the discount, the total comes to $800.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if hasattr(self, "last_transaction"):
            self.total -= self.last_transaction
            self.last_transaction = 0

