#The sum of the squares of the first ten natural numbers is,
#1**2+2**2+...+10**2=385
#The square of the sum of the first ten natural numbers is,
#(1+2+...+10)**2=55**2=3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_squares(n):
    return n*(n+1)*(2*n+1)//6
def square_sum(n):
    return (n*(n+1)//2)**2
def dif_squaresum_sumsquares(n):
    ret = square_sum(n)-sum_squares(n)
    print(f"The difference between the sum of the squares and the square of the sum of the first {n} natural numbers is {ret}")
    return ret

dif_squaresum_sumsquares(100)