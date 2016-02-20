import time, sys

"""
Based on slide 49 from Computational Number Theory lecture.

Consider the following computational problem:

Input: N, a, b, x, y where N >= 1 is an integer a, b (= Z*N and x, y are
			 integers with 0 < x, y < N
Output: a^x * b^y mod N

Let k = |N|

1. [10 points] Consider the algorithm that first computes X = a^x mod N, 
then computes Y = b^y mod N, and returns XY mod N. Explain why this has
worst case cost of 4k + 1 multiplications modulo N. 
--&--
[Answer here.]
"""

"""
2. [30 points] Design an alternative, faster algorithm for this problem that
uses at most 2k+1 multiplications modulo N in the "mexp" function. You may
not use the Python "**" operator in your solution (if it appears at all in 
your code you will get 0 points).

Your solution must be faster than the naive solution, here is a sample run
from my solution:

$ python computational_number_theory/exercise_2.py
naive 6.75s
mexp 3.38s
Results matched? True

"""

def exp(a, n, N):
	r = 1

	for i in range(n.bit_length() - 1, -1, -1):
		r = ((r*r) * (a if (n >> i) & 0x1 else 1)) % N

	return r

def mexp(a, b, x, y, N):
	raise Exception("Define me!")

def naive(a, b, x, y, N):
	return (exp(a, x, N) * exp(b, y, N)) % N

def timeit(m, *args):
	start = time.time()
	r = m(*args)
	end = time.time()

	print m.__name__, "%2.2fs" % (end-start)

	return r

def test_both(a, b, x, y, N):
	n = timeit(naive, a, b, x, y, N)
	m = timeit(mexp, a, b, x, y, N)

	print "Results matched?", n == m


if __name__ == '__main__':
	# Just one example, our grader will test more than this.
	test_both(512, 256, 22222222, 22222222, 2**(2**21))
