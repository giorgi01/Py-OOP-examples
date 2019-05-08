# -*- coding: utf-8 -*-
from random import uniform


class Cashier:

    product_names = []
    product_prices = []
    product_quantity = []

    discounts = {
        'Milk': 'SANTE01',
        'Bread': 'PURI1',
        'Water': 'SNO007'
    }

    def __init__(self, cashier_name):
        self.name = cashier_name

    def product_info(self):
        for product in open('products.txt', 'r').read().split('\n'):
            if product.isalpha():  # ესეიგი პროდუქტის სახელია
                Cashier.product_names.append(product)
            else:
                Cashier.product_prices.append(float(product))  # ფასი
        self.dict1 = dict(zip(Cashier.product_names, Cashier.product_prices))
        print(self.dict1)

    def discount(self, product, code):
        if code == Cashier.discounts[product]:
            print(f'პროდუქტის ამჟამინდელი ფასი:',
                  round(self.dict1[product] - self.dict1[product] * uniform(0, 0.3), 2))
            print(f'გამოყენებული პრომო კოდი: {Cashier.discounts[product]}')

    def sell(self, product, amount):
        self.product = product
        self.amount = amount
        for item in open('quantity.txt', 'r').read().split('\n'):
            if item.isdigit():
                Cashier.product_quantity.append(int(item))  # ==რაოდენობაა
        warehouse = dict(zip(Cashier.product_names, Cashier.product_quantity))
        warehouse[product] -= amount
        print(f'გაიყიდა {amount}ცალი {product}')
        print(f'საწყობის მდგომარეობა {warehouse}')

    def check(self):
        print('------------ჩეკი------------')
        print(self.amount, 'ცალი', self.product)
        print(f'გადასახდელია {self.amount * self.dict1[self.product]}₾')
        print('---------------------------')


cashier1 = Cashier('Anna')
cashier1.product_info()
cashier1.discount('Milk', 'SANTE01')
cashier1.sell('Milk', 2)
cashier1.check()
