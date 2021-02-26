#sesson o1
res = 0
for e in range(1, 21):
    print('Now res is equal to:', res)
    res += 1

print('Total SUM:', res)

# marcar punto rojo -> debug -> step over (cambia uno a uno) -> console

def sum(n):
    res = 0
    for i in range(1, n+1):
        res += 1
    return res

print('The sum of the very first 20 numbers:', sum(20))
print('Sum of 100 numbers:', sum(100))

# fibonacci 2.0

series = [0, 1, 1]
a = 1
b = 1
for i in range(1, 9):
    c = b + a
    series.append(c)
    a = b
    b = c
print(series)