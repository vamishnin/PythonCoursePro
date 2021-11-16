import pytest
import task_1


@pytest.fixture(scope="function", params=[
    (-4, 'Input error'),
    (5001, 'Input error'),
    (5, 'V'),
    (69, 'LXIX'),
    (678, 'DCLXXVIII'),
    (1001, 'MI'),
    (4999, 'MMMMCMXCIX')
])
def param_test(request):
    return request.param


def test_to_roman(param_test):
    (input_num, expected_output) = param_test
    result = task_1.to_roman(input_num)
    print(f'arabic: {input_num}, roman: {result}, expected roman: {expected_output}')
    assert result == expected_output


if __name__ == '__main__':
    pytest.main()
