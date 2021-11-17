import pytest
import task_1


class TestToRoman:

    @pytest.fixture(scope="function", params=[
        (-4, 'Input error'),
        (5001, 'Input error'),
    ])
    def param_test_neg(self, request):
        return request.param

    @pytest.fixture(scope="function", params=[
        (5, 'V'),
        (69, 'LXIX'),
        (678, 'DCLXXVIII'),
        (1001, 'MI'),
        (4999, 'MMMMCMXCIX')
    ])
    def param_test_pos(self, request):
        return request.param

    def test_wrong_input(self, param_test_neg):
        (input_num, expected_output) = param_test_neg
        result = task_1.to_roman(input_num)
        print(f'arabic: {input_num}, output: {result}, expected output: {expected_output}')
        assert result == expected_output

    def test_to_roman(self, param_test_pos):
        (input_num, expected_output) = param_test_pos
        result = task_1.to_roman(input_num)
        print(f'arabic: {input_num}, roman: {result}, expected roman: {expected_output}')
        assert result == expected_output


if __name__ == '__main__':
    pytest.main()
