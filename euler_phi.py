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

Implementation of Euler's Phi function.
Returns the result of calculating Phi(n).
Optional argument verbose, if true, prints the result.
"""

from math import gcd

def phi(n, verbose = False):

    answer = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            answer += 1

    if verbose:
        print("Phi({}) = {}".format(n ,answer))

    return answer

if __name__ == '__main__':
    import sys

    phi(int(sys.argv[1]), True)
