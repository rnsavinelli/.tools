#!/usr/bin/python3

"""
 Copyright (c) 2020 Savinelli Roberto Nicolás <rsavinelli@est.frba.utn.edu.ar>

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

"""

from math import gcd
from euler_phi import phi

ERROR = -1

def isPrime(n) :
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True

def via_Fermat_little(a, n, p, verbose = False):
    if (isPrime(p)):
        if verbose:
            print("{} is prime\n".format(p))

        #if gcd(pow(a, n), p) == 1: # traditional implementation
        if gcd(a, p) == 1: # improved implementation
        #if (a % p != 0) or (p % a != 0): # cuestionable implementation
            if verbose:
                print("Finding remainder using Fermat's Little Theorem:\n")

            x = int(n/(p-1))
            y = n - (x * (p-1))
            answer = pow(a, y) % p

            if verbose:
                print("{} = {}*{} + {}\n".format(n, (p-1), x, y))

                print("pow({}, {})".format(a, n))
                print("pow({}, {}*{}+{})".format(a, (p-1), x, y))
                print("pow({}, {}*{})*pow({}, {})".format(a, (p-1), x, a, y))
                print("pow({}, ({}-1)*{})*pow({}, {})".format(a, p, x, a, y))
                print("pow(pow({}, ({}-1)), {}))*pow({}, {})\n".format(a, p, x, a, y))

                print("Provided pow(a, p-1) is congruent to 1 (p)\n")

                print("pow(pow({}, ({}-1)), {})) is congruent to 1 ({})\n".format(a, p, x, p))

                print("Therefore pow({}, {}) is congruent to pow({}, {}) ({})\n".format(a, n, a, y, p))

                print("Remainder of (pow({}, {}) / {}) = Remainder of (pow({}, {}) / {}) = {}\n".format(a, n, p, a, y, p, answer))

            return answer

        else:
            return ERROR

    else:
        if verbose:
            print("{} is not prime\n".format(p))
        return ERROR

def via_Euler_Fermat(a, n, p, verbose = False):
    #if gcd(pow(a, n), p) == 1: # traditional implementation
    if gcd(a, p) == 1: # improved implementation
    #if (a % p != 0) or (p % a != 0): # cuestionable implementation
        if verbose:
            print("Finding remainder using Euler-Fermat's Theorem:\n")

        b = phi(p , verbose)
        x = int(n/b)
        y = n - (x * b)

        answer = pow(a, y) % p

        if verbose:
            print("\npow({}, phi({})) is congruet to 1 ({})".format(a, p, p))
            print("pow({}, {}) is congruet to 1 ({})\n".format(a, b, p))

            print("{} = {}*{}+{}\n".format(n, b, x, y))

            print("pow({}, {}) = pow({}, {}*{}+{})".format(a, n, a, b, x, y))
            print("pow({}, {}) = pow(pow({}, {}), {})*pow({}, {})\n".format(a, n, a, b, x, a, y))

            print("Given pow({}, {}) is congruet to 1 ({}), then".format(a, b, p))
            print("pow({}, {}) ≡  1*pow({}, {}) => pow({}, {}) is congruent to {} ({})\n".format(a, n, a, y, a, y, answer, p))

            print("pow({}, {}) ≡  {} ({})\n".format(a, n, answer, p))

        return answer

    return ERROR

def solve(a, n, p, verbose = False):
    if a < 1 or n < 1 or p < 1:
        return ERROR

    print("Calculating de remainder of pow({}, {}) / {}\n".format(a, n, p))
    answer = via_Fermat_little(a, n, p, verbose)

    if answer == ERROR:
        answer = via_Euler_Fermat(a, n, p, verbose)

    return answer

if __name__ == '__main__':
    import sys

    print("Answer = {}".format(solve(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), True)))
