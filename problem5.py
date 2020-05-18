#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from functools import reduce
def small_evenly_div_n(n):
    list1 = []
    for number in range(1,n):
        nb = number
        for element in list1:
            if nb%element == 0:
                nb//=element
        list1.append(nb)
    return reduce((lambda x,y: x*y),list1)

print(small_evenly_div_n(20))