list_numbers = [0,1]
counter = 0
while counter <=  8:
    new_number = list_numbers[-1] + list_numbers[-2]
    list_numbers.append(new_number)
    counter += 1
print(list_numbers)

# other way to do so:
x = 0
y = 1
fibonacci_list =[x, y]
limit = 11
for i in range(0, limit - 2):
    fn = x + y
    fibonacci_list.append(fn)
    x = y
    y = fn
print(fibonacci_list)
for e in fibonacci_list:
    print(e, end=' ')

# 3rd way:
def fibon(n):
    x = 1
    y = 1
    fibonacci_list2 = [x,y]
    for i in range(0, n - 2):
        fb = x + y
        fibonacci_list2.append(fb)
        x = y
        y = fb
    return  fibonacci_list2[-1]
print('5th Fibbonacci term:', fibon(5))
print('10th Fibonacci term: ', fibon(10))
print('15th Fibonacci term: ', fibon(15))

