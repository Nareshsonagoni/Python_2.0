
for r in range(6):
    for c in range(7):
        if (r == 0 and c % 3 != 0) or (r == 1 and c % 3 == 0) or (r - c == 2) or (r + c == 8):
            print('*',end = "")
        else:
            print(end = " ")
    print()

# Always imagine the output first before doing the patterns, it will be easy to write code once you have an idea