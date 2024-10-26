# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
# is_prime = True
# for i in numbers:
#     k = 0
#     for j in range(min(numbers), max(numbers), 1):
#         if i % j == 0:
#             k += 1
#     if k == 2:
#         primes.append(i)
#     elif k >= 2:
#         not_primes.append(i)
# print(primes)
# print(not_primes)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    k = 0
    is_prime = True
    for j in range(min(numbers), max(numbers)):
        if i % j == 0:
            k += 1
            if k > 2:
                is_prime = False
    if is_prime:
        if i != 1:
            primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)
