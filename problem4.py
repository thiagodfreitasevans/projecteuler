#A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
def palindromics_six_3dig_prod():
    limit = 998001 # 999*999
    for i in range(limit,1,-1):
        palind_numb = str(i)
        group1 = palind_numb[0] == palind_numb[-1] 
        group2 = palind_numb[1] == palind_numb[-2]
        group3 = palind_numb[2] == palind_numb[-3]
        if (group1 and group2) and group3:
            for j in range(999,100,-1):
                if i%j == 0:
                    factor = i/j
                    if (factor > 99) and (factor < 1000):
                        return i
print(palindromics_six_3dig_prod())