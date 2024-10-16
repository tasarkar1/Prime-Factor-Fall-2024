"""
prime.py -- Write the application code here
"""

def generate_prime_factors(n):
    if type(n) is not int:
        raise ValueError
    primelist = []
    for num in range (2, n):
         while (n % num) ==0:
            primelist.append(num)
            n//=num
    if n > 1:
         primelist.append(n)
    return primelist


