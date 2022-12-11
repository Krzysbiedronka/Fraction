from fraction import Fraction
from pytest import raises


def test_create_fraction_typical():
    fraction = Fraction(1, 2)
    assert fraction.get_numerator() == 1
    assert fraction.get_denominator() == 2


def test_create_fraction_negatives_arguments():
    fraction = Fraction(-1, -2)
    assert fraction.get_numerator() == -1
    assert fraction.get_denominator() == -2
    assert str(fraction) == '1/2'


def test_GCD_typical():
    fraction = Fraction(1, 2)
    assert fraction.GCD(1, 2) == 1


def test_create_fraction_not_normalized():
    fraction = Fraction(2, 4)
    assert fraction.get_numerator() == 1
    assert fraction.get_denominator() == 2


def test_create_fraction_negative():
    fraction = Fraction(3, -9)
    assert fraction.get_numerator() == 1
    assert fraction.get_denominator() == -3


def test_create_fraction_numerator_0():
    fraction = Fraction(0, -900)
    assert fraction.get_numerator() == 0
    assert fraction.get_denominator() == -900


def test_create_fraction_denominator_0():
    with raises(ZeroDivisionError):
        Fraction(1, 0)


def test_create_fraction_equal_int():
    fraction = Fraction(2, 1)
    assert fraction.get_numerator() == 2
    assert fraction.get_denominator() == 1


def test_str_fraction_typical():
    fraction = Fraction(3, 4)
    assert str(fraction) == '3/4'


def test_str_fraction_equal_int():
    fraction = Fraction(3, 1)
    assert str(fraction) == '3'


def test_str_fraction_numerator_neagtive():
    fraction = Fraction(-9, 2)
    assert str(fraction) == '-9/2'


def test_str_fraction_denominator_neagtive():
    fraction = Fraction(9, -2)
    assert str(fraction) == '-9/2'


def test_add_typical():
    fraction1 = Fraction(3, 4)
    fraction2 = Fraction(50, 100)
    assert str(fraction1 + fraction2) == '5/4'


def test_add_0():
    fraction1 = Fraction(3, 8)
    fraction2 = Fraction(0, -5100)
    assert str(fraction1 + fraction2) == '3/8'


def test_add_0_different_combination():
    fraction1 = Fraction(0, 8)
    fraction2 = Fraction(0, -5100)
    assert str(fraction1 + fraction2) == '0'


def test_add_neagtive():
    fraction1 = Fraction(3, 4)
    fraction2 = Fraction(50, -100)
    assert str(fraction1 + fraction2) == '1/4'


def test_sub_typical():
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(75, 100)
    assert str(fraction1 - fraction2) == '-1/4'


def test_sub_0():
    fraction1 = Fraction(3, 8)
    fraction2 = Fraction(0, -5100)
    assert str(fraction1 - fraction2) == '3/8'


def test_sub_from_0():
    fraction1 = Fraction(0, 8)
    fraction2 = Fraction(40, -5100)
    assert str(fraction1 - fraction2) == '2/255'


def test_mul_typical():
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(75, 100)
    assert str(fraction1 * fraction2) == '3/8'


def test_mul_by_1():
    fraction1 = Fraction(1, 1)
    fraction2 = Fraction(75, 100)
    assert str(fraction1 * fraction2) == '3/4'


def test_mul_by_0():
    fraction1 = Fraction(1, 1)
    fraction2 = Fraction(0, 100)
    assert str(fraction1 * fraction2) == '0'


def test_div_typical():
    fraction1 = Fraction(1, 1)
    fraction2 = Fraction(75, 100)
    assert str(fraction1 / fraction2) == '4/3'


def test_div_by_0():
    fraction1 = Fraction(1, 1)
    fraction2 = Fraction(0, 100)
    with raises(ZeroDivisionError):
        fraction1 / fraction2


def test_div_by_1():
    fraction1 = Fraction(2, 1)
    fraction2 = Fraction(1, 1)
    assert str(fraction1 / fraction2) == '2'


def test_add_integer():
    fraction1 = Fraction(2, 4)
    assert str(fraction1.add_int(10)) == '21/2'
