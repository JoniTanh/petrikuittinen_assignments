path = input("Give me file path?")
sumx = 0
with open(path) as f:
    for line in f:
        n = float(line.rstrip())
        sumx += n
print("sum =", sumx)
