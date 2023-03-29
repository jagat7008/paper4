def divisible(n):
    for i in range(1,n+1):
        if i % 10==0 and i % 2==0:
            yield i
for num in divisible(20):
    print(num)