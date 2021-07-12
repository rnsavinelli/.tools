#!/usr/bin/python3

"""
 Copyright (c) 2020 Savinelli Roberto Nicolás <rsavinelli@frba.utn.edu.ar>

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.

Implementation of the extended Euclidean algorithm.
Returns triple (a, b, g) where a_{m} + b_{n} = g and g = gcd(m, n).
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
