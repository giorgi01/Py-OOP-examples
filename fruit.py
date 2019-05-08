import random


class Fruit:

    def __init__(self, name):
        self.name = name
        self.flowering_period = random.choice(['გაზაფხული',
                                               'ზაფხული',
                                               'შემოდგომა',
                                               'ზამთარი'])
        self.ripe = 0

    def info(self):
        print(f'მცენარის სახელი : {self.name}, '
              f'ყვავილობის პერიოდი: {self.flowering_period}')

    def ripening(self, days):
        self.ripe += days
        if self.ripe > 80:
            print(f'{self.name} მწიფეა')

    def show_price(self, period):
        if period == 'ზაფხული':
            print('სავარაუდო ფასი:',
                  round(random.uniform(1, 3), 2), '₾')
        elif period == 'შემოდგომა':
            print('სავარაუდო ფასი:',
                  round(random.uniform(1, 4), 2), '₾')
        elif period == 'ზამთარი':
            print('სავარაუდო ფასი:',
                  round(random.uniform(1, 5), 2), '₾')
        else:
            print('სავარაუდო ფასი:',
                  round(random.uniform(1, 3), 2), '₾')


apple = Fruit('ვაშლი')
apple.info()
apple.ripening(81)
apple.show_price('ზაფხული')