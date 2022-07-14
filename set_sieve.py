
LIMIT = 10001

not_prime = set()

for num in range(2, LIMIT):
    if num in not_prime:
        continue   # num is not prime
    print(num, end=', ')
    for m in range(num * 2, LIMIT, num):
        not_prime.add(m)



