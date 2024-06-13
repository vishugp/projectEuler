#!/usr/bin/python

# https://projecteuler.net/problem=\9


def check_pythagorean_primes(n = 1000):
    for a in range(1,n):
        for b in range(a,n):
            for c in range(b,n):
                if a+b+c==n and a**2+b**2-c**2==0:
                    print(a,b,c)
                    print(a*b*c)
                    return
                    
check_pythagorean_primes(1000)
                
