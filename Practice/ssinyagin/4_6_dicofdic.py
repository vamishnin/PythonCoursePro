class ClearDic:

    def __init__(self, mist, key):
        self.mist = mist
        self.key = key
        #self.key_list = []

    def clear_dic(self):
        print('Матрица для анализа: ', self.mist)
        print('Значение для удаления: ', self.key)
        k = 0
        n = len(self.mist)
        for i in self.mist:
            m = 0
            n = len(i)
            for j in range(n):
                if j == self.key:
                    for item in self.mist:
                        del item[m]
                m += 1

        print('Матрица без значения: ', self.mist)


matrix = [[2, 1, 1, 1], [2, 2, 2, 2], [2, 2, 2, 2]]
hit = ClearDic(matrix, 1)
b = hit.clear_dic()

