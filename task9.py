def f(x):
    mas = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            mas.append(i)
            if i != int(x**0.5):
                mas.append(x//i)
    return mas
print(len(f(2097152)))
