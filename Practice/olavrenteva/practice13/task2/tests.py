from task2 import Money
import pytest


class TestMoneyBase:
    @pytest.fixture(
        params=(
                ((0, 0), '0,00'),
                ((1, 5), '1,05'),
                ((10, 99), '10,99')
        ),
        ids=lambda args: f'Test for {args[0]}'
    )
    def param_positive_creation(self, request):
        return request.param

    def test_creation_positive(self, param_positive_creation):
        rub, pen = param_positive_creation[0]
        m = Money(rub, pen)
        assert(m.ruble == rub and m.penny == pen)

    def test_money_to_str(self, param_positive_creation, capsys):
        rub, pen = param_positive_creation[0]
        exp_print_res = param_positive_creation[1]
        m = Money(rub, pen)
        print(m)
        captured = capsys.readouterr()
        assert(captured.out.strip() == exp_print_res)

    @pytest.fixture(
        params=(
                ((0.2, 0), 'ruble should be integer'),
                (('one', 0), 'ruble should be integer'),
                ((1, 100), 'penny should be natural number and should not exceed 99'),
                ((1, -1), 'penny should be natural number and should not exceed 99'),
                ((1, 5.5), 'penny should be natural number and should not exceed 99'),
                ((10, 'two'), 'penny should be natural number and should not exceed 99')
        ),
        ids=lambda args: f'Test for {args[0]}'
    )
    def param_negative_creation(self, request):
        return request.param

    def test_creation_negative(self, param_negative_creation):
        rub, pen = param_negative_creation[0]
        with pytest.raises(ValueError) as exception:
            m = Money(rub, pen)
        assert str(exception.value) == param_negative_creation[1]


class TestMoneyCompare:
    @pytest.fixture(
        params=(
                (((5, 10), (5, 10)), True),
                (((1, 5), (5, 10)), False)
        ),
        ids=lambda args: f'Test for {args[0][0]} == {args[0][1]} and result {args[1]}'
    )
    def param_tests_eq(self, request):
        return request.param

    def test_eq(self, param_tests_eq):
        (m1_rub, m1_pen), (m2_rub, m2_pen) = param_tests_eq[0]
        m1 = Money(m1_rub, m1_pen)
        m2 = Money(m2_rub, m2_pen)
        exp_res = param_tests_eq[1]
        assert(m1 == m2 if exp_res is True else not m1 == m2)

    @pytest.fixture(
        params=(
                (((5, 10), (5, 10)), True),
                (((1, 5), (5, 10)), True),
                (((5, 5), (5, 1)), False)
        ),
        ids=lambda args: f'Test for {args[0][0]} <= {args[0][1]} and result {args[1]}'
    )
    def param_tests_le(self, request):
        return request.param

    def test_le(self, param_tests_le):
        (m1_rub, m1_pen), (m2_rub, m2_pen) = param_tests_le[0]
        m1 = Money(m1_rub, m1_pen)
        m2 = Money(m2_rub, m2_pen)
        exp_res = param_tests_le[1]
        assert(m1 <= m2 if exp_res is True else not m1 <= m2)

    @pytest.fixture(
        params=(
                (((5, 10), (5, 10)), False),
                (((1, 5), (5, 10)), True),
                (((5, 5), (5, 1)), False)
        ),
        ids=lambda args: f'Test for {args[0][0]} < {args[0][1]} and result {args[1]}'
    )
    def param_tests_lt(self, request):
        return request.param

    def test_lt(self, param_tests_lt):
        (m1_rub, m1_pen), (m2_rub, m2_pen) = param_tests_lt[0]
        m1 = Money(m1_rub, m1_pen)
        m2 = Money(m2_rub, m2_pen)
        exp_res = param_tests_lt[1]
        assert (m1 < m2 if exp_res is True else not m1 < m2)

    @pytest.fixture(
        params=(
                (((5, 10), (5, 10)), True),
                (((1, 5), (5, 10)), False),
                (((5, 5), (5, 1)), True)
        ),
        ids=lambda args: f'Test for {args[0][0]} >= {args[0][1]} and result {args[1]}'
    )
    def param_tests_ge(self, request):
        return request.param

    def test_ge(self, param_tests_ge):
        (m1_rub, m1_pen), (m2_rub, m2_pen) = param_tests_ge[0]
        m1 = Money(m1_rub, m1_pen)
        m2 = Money(m2_rub, m2_pen)
        exp_res = param_tests_ge[1]
        assert (m1 >= m2 if exp_res is True else not m1 >= m2)

    @pytest.fixture(
        params=(
                (((5, 10), (5, 10)), False),
                (((1, 5), (5, 10)), False),
                (((5, 5), (5, 1)), True)
        ),
        ids=lambda args: f'Test for {args[0][0]} > {args[0][1]} and result {args[1]}'
    )
    def param_tests_gt(self, request):
        return request.param

    def test_gt(self, param_tests_gt):
        (m1_rub, m1_pen), (m2_rub, m2_pen) = param_tests_gt[0]
        m1 = Money(m1_rub, m1_pen)
        m2 = Money(m2_rub, m2_pen)
        exp_res = param_tests_gt[1]
        assert (m1 > m2 if exp_res is True else not m1 > m2)


class TestMoneyArithmetic:
    @pytest.fixture(
        params=(
                (((1, 2), (3, 10)), (4, 12)),
                (((1, 99), (3, 10)), (5, 9))
        ),
        ids=lambda args: f'Test for {args[0][0]} + {args[0][1]} and result {args[1]}'
    )
    def param_tests_sum(self, request):
        return request.param

    def test_sum(self, param_tests_sum):
        (m1_rub, m1_pen), (m2_rub, m2_pen) = param_tests_sum[0]
        m1 = Money(m1_rub, m1_pen)
        m2 = Money(m2_rub, m2_pen)
        (exp_sum_rub, exp_sum_pen) = param_tests_sum[1]
        exp_sum = Money(exp_sum_rub, exp_sum_pen)
        assert(m1 + m2 == exp_sum)

    @pytest.fixture(
        params=(
                (((5, 10), (3, 1)), (2, 9)),
                (((10, 5), (3, 80)), (6, 25)),
                (((1, 1), (3, 80)), (-2, 79))
        ),
        ids=lambda args: f'Test for {args[0][0]} - {args[0][1]} and result {args[1]}'
    )
    def param_tests_sub(self, request):
        return request.param

    def test_sub(self, param_tests_sub):
        (m1_rub, m1_pen), (m2_rub, m2_pen) = param_tests_sub[0]
        m1 = Money(m1_rub, m1_pen)
        m2 = Money(m2_rub, m2_pen)
        (exp_sub_rub, exp_sub_pen) = param_tests_sub[1]
        exp_sub = Money(exp_sub_rub, exp_sub_pen)
        assert(m1 - m2 == exp_sub)

    @pytest.fixture(
        params=(
                (((5, 10), (2, 55)), 2),
                (((1, 5), (4, 22)), 0.25)
        ),
        ids=lambda args: f'Test for {args[0][0]} / {args[0][1]} and result {args[1]}'
    )
    def param_tests_div_money(self, request):
        return request.param

    def test_div_money(self, param_tests_div_money):
        (m1_rub, m1_pen), (m2_rub, m2_pen) = param_tests_div_money[0]
        m1 = Money(m1_rub, m1_pen)
        m2 = Money(m2_rub, m2_pen)
        exp_res = param_tests_div_money[1]
        assert(m1 / m2 == exp_res)

    @pytest.fixture(
        params=(
                (((5, 10), 2), 2.55),
                (((1, 5), 4.5), 0.23)
        ),
        ids=lambda args: f'Test for {args[0][0]} / {args[0][1]} and result {args[1]}'
    )
    def param_tests_div_num(self, request):
        return request.param

    def test_div_num(self, param_tests_div_num):
        (m_rub, m_pen), num = param_tests_div_num[0]
        m = Money(m_rub, m_pen)
        exp_res = param_tests_div_num[1]
        assert(m / num == exp_res)


class TestMoneyDollar:
    def setup(self):
        Money.clear_rate_to_dollar()

    def test_set_correct_rate(self):
        Money.set_rate_to_dollar(0.014)
        assert(Money.get_rate_to_dollar(), 0.014)

    def test_correct_convert_to_dollar(self):
        Money.set_rate_to_dollar(0.014)
        m = Money(1000, 10)
        dol = m.convert_to_dollars()
        assert(dol, 14.0014)

    def test_clear_rate(self):
        Money.set_rate_to_dollar(0.014)
        Money.clear_rate_to_dollar()
        assert(not Money.get_rate_to_dollar())

    @pytest.fixture(
        params=(0, 'str'),
        ids=lambda args: f'Test for {args}'
    )
    def param_tests_incorrect_dollar_rate(self, request):
        return request.param

    def test_set_incorrect_rate(self, param_tests_incorrect_dollar_rate):
        with pytest.raises(ValueError) as exception:
            Money.set_rate_to_dollar(param_tests_incorrect_dollar_rate)
        assert(exception.value, 'rate_to_dollar should be natural number')

    def test_incorrect_convert_to_dollar(self):
        m = Money(1000, 10)
        with pytest.raises(Exception) as exception:
            m.convert_to_dollars()
        assert(exception.value, 'rate_to_dollar is not defined')
