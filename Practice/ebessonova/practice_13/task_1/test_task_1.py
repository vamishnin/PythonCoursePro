import unittest
import task_1


class TestToRoman(unittest.TestCase):

    def test_input(self):
        assert (task_1.to_roman(-4) == 'Input error')
        assert (task_1.to_roman(50001) == 'Input error')

    def test_convertion(self):
        assert (task_1.to_roman(5) == 'V')
        assert (task_1.to_roman(69) == 'LXIX')
        assert (task_1.to_roman(678) == 'DCLXXVIII')
        assert (task_1.to_roman(1001) == 'MI')
        assert (task_1.to_roman(4999) == 'MMMMCMXCIX')


if __name__ == '__main__':
    unittest.main()
