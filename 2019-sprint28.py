combo = []
count = 0

for x in range(-10, 11):
    for y in range(-10, 11):
        if x + abs(y) == abs(x) + y:
            combo.append((x,y))
            count += 1

print(combo)
print(count)