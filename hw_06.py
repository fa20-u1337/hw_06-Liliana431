class Fib():
    """Число Фибоначчи.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Проверка, что start не изменился
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** ТВОЙ КОД ЗДЕСЬ ***"

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """Торговый автомат, продающий некоторый товар по некоторой цене.
    
    >>> v = VendingMachine('яблоко', 10)
    >>> v.vend()
    'Товара нет в наличии.'
    >>> v.restock(2)
    'Количество товара «яблоко»: 2'
    >>> v.vend()
    'Нужно дополнительно внести 10 ₽.'
    >>> v.deposit(7)
    'Доступно: 7 ₽'
    >>> v.vend()
    'Нужно дополнительно внести 3 ₽.'
    >>> v.deposit(5)
    'Доступно: 12 ₽'
    >>> v.vend()
    'Получите яблоко и сдачу 2 ₽.'
    >>> v.deposit(10)
    'Доступно: 10 ₽'
    >>> v.vend()
    'Получите яблоко.'
    >>> v.deposit(15)
    'Товара нет в наличии. Вот твои деньги — 15 ₽.'

    >>> w = VendingMachine('лимонад', 2)
    >>> w.restock(3)
    'Количество товара «лимонад»: 3'
    >>> w.restock(3)
    'Количество товара «лимонад»: 6'
    >>> w.deposit(2)
    'Доступно: 2 ₽'
    >>> w.vend()
    'Получите лимонад.'
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.c = 0
        self.d = 0

    def vend(self):
        if self.c == 0:
            return 'Товара нет в наличии.'
        elif self.d < self.cost:
            return 'Нужно дополнительно внести {0} ₽.'.format(self.cost - self.d)
        else:
            self.c -= 1
            self.d -= self.cost
            if self.d == 0:
                return 'Получите {0}.'.format(self.name)
            else:
                p = self.d
                self.d = 0
                return 'Получите {0} и сдачу {1} ₽.'.format(self.name, p)

    def restock(self, c):
        self.c += c
        return 'Количество товара «{0}»: {1}'.format(self.name, self.c)

    def deposit(self, d):
        self.d += d
        if self.c == 0:
            return 'Товара нет в наличии. Вот твои деньги — {0} ₽.'.format(self.d)
        return  'Доступно: {0} ₽'.format(self.d)
