a = input()
a = int(a)
b = input()
b = int(b)

print("Вкажіть дію(+, -, *, /):")
d = input()
#d = float(d)

if d =="+":
    r= a + b
    print(r)
elif d =="-":
    r= a - b
    print(r)
elif d == "*":
        r = a * b
        print(r)
elif d == "/":
        if b == 0:
            print("На нуль не ділим")
        else:
            r = a / b
            print(r)

