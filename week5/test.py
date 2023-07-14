def print_primes(n, m):
    primes = []  # to store the prime numbers
    
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num/2)+1): # check if the number is divisible by any number between 2 and num/2
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    for i, prime in enumerate(primes):
        print(prime, end=" ")
        if (i+1) % m == 0:  # print newline after m primes
            print()
    
    print()  # print a newline at the end

# Example usage
print_primes(50, 4)
