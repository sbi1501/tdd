# $5 + 10 CHF = $10
# округление денежных величин
# hash_code()
# равенство значению null
# равенство объектов


class Money:

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, money):
        return (self._amount == money._amount
                and self._currency == money._currency)

    @classmethod
    def dollar(cls, amount):
        return Money(amount, 'USD')

    @classmethod
    def franc(cls, amount):
        return Money(amount, 'CHF')

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)


def test_multiplication():
    five = Money.dollar(5)
    assert five.times(2) == Money.dollar(10)
    assert five.times(3) == Money.dollar(15)


def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert not Money.dollar(5) == Money.dollar(6)
    assert Money.franc(5) != Money.dollar(5)


def test_currency():
    assert Money.dollar(1).currency() == 'USD'
    assert Money.franc(1).currency() == 'CHF'
