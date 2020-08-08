#!/usr/bin/python3

"""
Implementation of extended Euclidean algorithm.
Returns triple (a, b, g) where am + bn = g and g = gcd(m, n).
Optional argument trace, if true, shows progress.
"""

def euclid(m, n, trace = False, depth = 0):

    def output(s):
        if trace:
            print("{}{}".format(' ' * depth, s))

    output("Finding gcd({},{})".format(m, n))

    if m == 0:
        output("base case")
        a, b, g = 0, 1, n
    else:
        q = n//m
        r = n % m
        output("q = {} r = {}".format(q, r))
        a1, b1, g = euclid(r, m, trace, depth + 1)
        a = b1 - a1*q
        b = a1
        output("a = b1 - a1*q = {} - {}*{} = {}".format(b1, a1, q, a))

    output("Returning {}*{} + {}*{} = {}".format(a, m, b, n, g))
    return a, b, g

if __name__ == '__main__':
    import sys

    euclid(int(sys.argv[1]), int(sys.argv[2]), True)
