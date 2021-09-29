def poly(a):
    mid = int(len(a) / 2)

    if len(a) % 2 == 0:
        mid_val = mid - 1
    else:
        mid_val = mid

    if a[0:mid] == a[len(a):mid_val:-1]:
        print('Polyndrom')
    else:
        print('Not a polyndrom')


a = input('Write a word ')
poly(a)

