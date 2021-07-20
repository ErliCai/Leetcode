def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """

    if n == 0 or n == 1 or n == 2:
        return 0


    prime = [True for i in range(n)]
    prime[0] = prime[1] = False

    
    i = 2
    while i * i < n:
        if prime[i]:
            for j in range(2 * i, n, i):
                prime[j] = False
        i += 1

    return sum(prime)

print(countPrimes(10))