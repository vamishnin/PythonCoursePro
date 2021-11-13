from multiprocessing import Process
from multiprocessing import Pool


def custom_sum(*args):
    if len(args) == 0:
        return

    if not all(isinstance(x, type(args[0])) for x in args[1:]):
        raise ValueError("Bad Input!")

    res = args[0]
    for x in args[1:]:
        res += x
    return res


if __name__ == '__main__':
    par1 = (1, 2, 3, 4, 5)
    par2 = ('1', '2', '3', '4', '5')
    par3 = ([1, 2], ['3', '4'], [5])
    params = par1, par2, par3

    with Pool(processes=3) as p:
        results = p.starmap(custom_sum, params)

    for res in results:
        print(res)
