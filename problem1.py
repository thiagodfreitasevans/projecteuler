# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def multiples_three_or_five(n):
    for i in range(3,n):
        if (i%3 == 0) or (i%5 == 0):
            print(i)
            yield i
sum_multiples = sum(list(multiples_three_or_five(1000)))
print(sum_multiples)