"""
Нужно реализовать ORM (объектно-реляционная модель, набор классов, которым
можно описать нужную систему) для интернет-магазина. Функционал магазина:
1. Каталог товаров (товар: название, описание, цена, оценки покупателей, отзывы
покупателей);
2. Зарегистрированные покупатели (пользователь: имя, фамилия, телефон, оценки
товаров, отзывы о товарах, заказы);
3. Заказы (заказ: клиент, товары, дата оформления, статус)

План:
1. Сделать конструкторы для всех основных классов
1.1. Создать тестовые экземпляры основных классов (листы объектов)
2. Сделать конструкторы для всех дополнительных классов
3. Реализовать метод формирования заказа у пользователя
4. Реализовать метод оценки товара
5. Реализовать метод составления отзыва
"""

from datetime import date


class User:
    def __init__(self, name, lastname, phone):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.marks = list()
        self.reviews = list()
        self.orders = list()
        self.messages = list()

    def __repr__(self):
        return f'{self.name} {self.lastname}'

    def make_order(self, good):
        order = Order(self, good)
        self.orders.append(order)


class Good:
    def __init__(self, name, desc, price):
        self.name = name
        self.desc = desc
        self.price = price
        self.marks = list()
        self.reviews = list()

    def __repr__(self):
        return self.name

    def send_promotion(self, text):
        for review in self.reviews:
            review.user.messages.append(str(text))
        print(
            f'Promotions have been sent to people who left review on {self.name}')


class Order:
    def __init__(self, user, good):
        self.user = user
        self.good = good
        self.date = date.today()
        self.status = 'new'

    def __repr__(self):
        return f"{self.user.name}'s order for {self.good.name}"

    def make_review(self, text):
        review = Review(self.good, self.user, text)
        self.user.reviews.append(review)
        self.good.reviews.append(review)

    def give_mark(self, mark):
        given_mark = Mark(self.good, self.user, mark)
        self.user.marks.append(given_mark)
        self.good.mark.append(given_mark)


class Mark:
    def __init__(self, good, user, mark):
        self.good = good
        self.user = user
        self.mark = mark


class Review:
    def __init__(self, good, user, review):
        self.good = good
        self.user = user
        self.review = review

    def __repr__(self):
        return f"{self.user.name}'s review about {self.good.name}:\n{self.review}"


u = [
    User('Serhii', 'Hlavatskyi', 101),
    User('Petr', 'Inkognito', 102)
]

g = [
    Good('PS4', 'best console ever', 400),
    Good('XboxOne', 'worst console ever', 500)
]

first_user = u[0]
second_user = u[1]
ps4 = g[0]
xbox = g[1]
first_user.make_order(ps4)
first_user.make_order(xbox)
second_user.make_order(ps4)
first_user.orders[0].status = 'shipped'
first_user.orders[0].make_review('Really the best place for games')
second_user.orders[0].make_review('Amazing, never buy Xbox!!! NEVER!! Only ps')

ps4.send_promotion('You received 10% discount for buying PS4')
print(second_user.messages)
