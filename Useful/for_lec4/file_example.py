# Descriptors
# from tempfile import mkstemp
# import os
#
#
# d, p = mkstemp(dir='.')
# print(d)
# print(p)
# os.write(d, 'abcdef'.encode())
# os.close(d)


with open("myfile.txt", "r") as f:
    for i in f:
        print(i)


# Safe work with file
# s = f.read(1)
# while s:
#     print(s)
#     s = f.read(1)
# print(f.closed)
# f.close()
# print(f.closed)



