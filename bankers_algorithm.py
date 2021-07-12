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

"""

# Banker's Algorithm

def execution_verifier():
    problematic_processes = []

    for j in range(n):
        recs = 0

        for i in range(m):
            recs += allocation_matrix[i][j]

        recs += available_matrix[j]

        for i in range(m):
            if(max_matrix[i][j] > recs):
                problematic_processes.append(k)
                break

    return problematic_processes


def get_safe_sequence(m, n, need_matrix, available_matrix, allocation_matrix):
    ans = []

    while(len(ans) < m):
        for i in range(m):
            if i not in ans:
                valid = True

                for j in range(n):
                    if(need_matrix[i][j] > available_matrix[j]):
                        valid = False

                if valid:
                    for j in range(n):
                        available_matrix[j] += allocation_matrix[i][j]

                    ans.append(i)

    return ans


if __name__=="__main__":

    # BO INPUT

    m = 4 # Number of processes
    n = 4 # Number of resources

    allocation_matrix = [
        [0, 1, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [2, 1, 0, 0],
    ]

    max_matrix = [
        [3, 2, 0, 2],
        [3, 4, 1, 1],
        [9, 5, 1, 3],
        [3, 4, 1, 3]
    ]

    available_matrix = [5, 2, 0, 2]

    # EO INPUT

    need_matrix = [[max_matrix[i][j] - allocation_matrix[i][j] for j in range(n)] for i in range(m)]

    problematic_processes = execution_verifier()

    if(len(problematic_processes) > 0):
        print("Safe sequence is not possible\nThese process can't be executed: ")
        for proc in problematic_processes:
            print(proc)

    else:
        safe_seq = get_safe_sequence(m, n, need_matrix, available_matrix, allocation_matrix)

        print("Safe sequence is: ")
        for i in range(m - 1):
            print("P", safe_seq[i], " -> ", sep="", end="")
        print("P", safe_seq[n - 1], sep="")
