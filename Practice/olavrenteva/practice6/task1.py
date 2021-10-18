# "while True:" has been removed - it gave endless cycle

def chargen():
    for c in '0123456789':
        yield c


words = [c + c for c in chargen()][:10]

print(words)
