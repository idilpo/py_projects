check_prime = [26, 39, 51, 53, 57, 79, 85]
for num in check_prime:
    for i in range(2, num):
        if (num % i == 0):
            print("%d is NOT a prime number" % (num))
            break
        if (i == num - 1):
            print("%d IS a prime number" % (num))
            break
        continue