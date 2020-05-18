#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
def prime_factors(n):
    number = n
    factor = 2
    while number >= factor:
        if number%factor == 0:
            yield factor
            number//=factor
        else:
            factor+=1
print(list(prime_factors(600851475143))[-1])