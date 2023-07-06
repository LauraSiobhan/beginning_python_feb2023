""" a class which defines a playing card """

class PlayingCard:
    suit = ""
    _value = ""
    ten_values = ('J', 'Q', 'K')
    suits = ('hearts', 'clubs', 'diamonds', 'spades')
    values = [str(num) for num in range(2, 11)]
    values.extend('JQKA')

    def __init__(self, value, suit):
        self.set_value(value.upper())
        self.suit = suit

    def __repr__(self):
        return f"PlayingCard('{self.value}', '{self.suit}')"

    def __str__(self):
        return f'{self.value} of {self.suit}'

    def points(self):
        if self._value in self.ten_values:
            return 10
        if self._value == 'A':
            return 11
        return int(self._value)

    def set_value(self, data):
        if data not in self.values:
            raise ValueError(f'{data} is not a valid card value')
        self._value = data
