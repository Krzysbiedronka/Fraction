class Fraction:

    """
    Class Fraction: Allows to calculate normalized fractions
    You can add, substract, multiply and divide using fractions
    It will show the fraction easy to read for the user
    (ZeroDivisionError will be raised if necessary)
    """

    def __init__(self, numerator, denominator):
        self.normalize_fraction(numerator, denominator)

    def get_numerator(self):
        return self._numerator

    def get_denominator(self):
        return self._denominator

    def get_fraction_as_float(self):
        return round(self._numerator / self._denominator, 2)

    def normalize_fraction(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("You cannot have 0 as denominator.")
        while True:
            gcd = self.GCD(numerator, denominator)
            if gcd == 1 or numerator == 0:
                self._numerator = int(numerator)
                self._denominator = int(denominator)
                break
            numerator = numerator // gcd
            denominator = denominator // gcd

    def GCD(self, x, y):
        while (y):
            x, y = y, x % y
        return abs(x)

    def __str__(self) -> str:
        if self._numerator == 0:
            return '0'
        if self._denominator == 1:
            return f'{self._numerator}'
        if self._numerator * self._denominator < 0:
            return f'-{abs(self._numerator)}/{abs(self._denominator)}'
        return f'{abs(self._numerator)}/{abs(self._denominator)}'

    def __add__(self, other: "Fraction"):
        a = self._numerator
        b = self._denominator
        c = other._numerator
        d = other._denominator
        return Fraction(a*d+b*c, b*d)

    def __sub__(self, other: "Fraction"):
        a = self._numerator
        b = self._denominator
        c = other._numerator
        d = other._denominator
        return Fraction(a*d-b*c, b*d)

    def __mul__(self, other: "Fraction"):
        a = self._numerator
        b = self._denominator
        c = other._numerator
        d = other._denominator
        return Fraction(a*c, b*d)

    def __truediv__(self, other: "Fraction"):
        a = self._numerator
        b = self._denominator
        c = other._numerator
        d = other._denominator
        return Fraction(a*d, b*c)

    def add_int(self, number):
        fraction = Fraction(number, 1)
        return fraction + self
