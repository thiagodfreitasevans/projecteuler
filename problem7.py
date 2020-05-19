import pdb
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
def is_prime(n):
    #We don't need to care with even numbers because all of passed numbers are odd
    aux = n//2
    for i in range(3,aux,2):
        if n%i==0:
            return False
    return True
def get_prime(n):
    count = 2 # 2 and 3
    if n == 1:
        return 2
    if n == 2:
        return 3
    number = 5 #The 3th prime
    current_prime = None
    while count < n:
        if is_prime(number):
            count+=1
            current_prime = number
        number+=2
    return current_prime

print(get_prime(10001))