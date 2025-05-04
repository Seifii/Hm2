import random
print("Guess!!")
n = random.randint(1,10)
#n = int(n)
#p = input()
#p = int(p)
s = 0
s = int(s)
while s<3:
    p = input()
    p = int(p)
    if p < n:
        print("More")
    elif p > n:
        print("Less")
    else:
        print("Correct")
        break
    s += 1
if s==3:
    print("Too much! The number is", n)


