import task1
import pytest


class TestToRomanFunc:
    @pytest.fixture(
        params=((1, 'I'), (3, 'III'), (4, 'IV'), (5, 'V'), (8, 'VIII'), (9, 'IX'), (10, 'X'),
                (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'),
                (900, 'CM'), (1000, 'M'), (444,'CDXLIV'), (1677,'MDCLXXVII'), (3999, 'MMMCMXCIX')),
        ids=lambda args: f'Test for {args[0]} and expected result {args[1]}'
    )
    def positive_tests_to_roman(self, request):
        return request.param

    @pytest.fixture(
        params=(0, 5001, -1, 'str'),
        ids=lambda args: f'Test for {args} and expected NonValidInput exception'
    )
    def negative_tests_to_roman(self, request):
        return request.param

    def test_to_roman_positive(self, positive_tests_to_roman):
        initial_val, expected_val = positive_tests_to_roman
        assert(task1.to_roman(initial_val) == expected_val)

    def test_to_roman_negative(self, negative_tests_to_roman):
        with pytest.raises(task1.NonValidInput):
            val = negative_tests_to_roman
            task1.to_roman(val)
