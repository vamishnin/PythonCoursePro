s = "abcbedefg"

memory = set()
for i in s:
    if i in memory:
        print(i)
        break
    memory.add(i)
else:
    print("No duplicates")



