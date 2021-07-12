
#!/usr/bin/python3

"""
 Copyright (c) 2021 Savinelli Roberto Nicolás <rsavinelli@frba.utn.edu.ar>

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

def bits_calculator(size_in_bytes):
    bits = 0

    while (pow(2, bits) < size_in_bytes):
        bits = bits + 1

    if (pow(2, bits) != size_in_bytes):
        bits = -1

    return bits

def logical_address_solver(n_pages, page_size, verbose = False):
    # Bits to represent n_pages
    page_bits = bits_calculator(n_pages)

    if verbose:
        print("\tBits needed to represent {} pages = {} bits".format(n_pages, page_bits))

    # Bits to represent the offset
    offset_bits = bits_calculator(page_size)

    if verbose:
        print("\tBits needed to represent the offset = {} bits".format(offset_bits))

    return page_bits, offset_bits


def physical_address_solver(n_frames, frame_size, verbose = False):
    # Bits to represent n_pages
    page_bits = bits_calculator(n_frames)

    if verbose:
        print("\tBits needed to represent {} frames = {} bits".format(n_frames, page_bits))

    # Bits to represent the offset
    offset_bits = bits_calculator(frame_size)

    if verbose:
        print("\tBits needed to represent the offset = {} bits".format(offset_bits))

    return page_bits, offset_bits


def solve(n_pages, page_size, n_frames, frame_size, verbose = False):
    print("# Data:\n\nPages = {}\nPage Size = {}\nFrames = {}\nFrame Size = {}\n".format(n_pages, page_size, n_frames, frame_size))

    print("# A logic address is represented by its page number and its offset, therefore:\n")
    la_page_bits, la_offset_bits = logical_address_solver(n_pages, page_size, verbose)

    if verbose and la_page_bits >= 0 and la_offset_bits >= 0:
        print("\n\tBits needed to represent a logic address = {} bits\n".format(la_page_bits + la_offset_bits))

    print("# A physical address is represented by its frame number and its offset, therefore:\n")
    pa_page_bits, pa_offset_bits = physical_address_solver(n_frames, page_size, verbose)

    if verbose and pa_page_bits >= 0 and pa_offset_bits >= 0:
        print("\n\tBits needed to represent a physical address = {} bits".format(pa_page_bits + pa_offset_bits))

    return la_page_bits, la_offset_bits, pa_page_bits, pa_offset_bits


if __name__ == '__main__':
    import sys

    if int(len(sys.argv)) < 5:
        print("Arguments description: ")
        print("python {} n_pages page_size n_frames frame_size".format(sys.argv[0]))

        print("\nUsage example: ")
        print("python {} 8 1024 32 1024".format(sys.argv[0]))

    else:
        pages = int(sys.argv[1])
        page_size = int(sys.argv[2])
        frames = int(sys.argv[3])
        frame_size = int(sys.argv[4])

        solve(pages, page_size, frames, frame_size, True)
