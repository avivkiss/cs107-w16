import time

"""
Based on slide 49 from Computational Number Theory lecture.

Consider the following computational problem:

Input: a, b, x, y where a, b, x, y are positive integers >= 0.
Outpu: a^x * b^y

Let k = max(bit_length(x), bit_length(y))

1. [10 points] Consider the algorithm that first computes X = a^x, the
computes Y = b^y, and returns XY. Explain why this has worst case cost of
4k + 1.
--&--
[Answer here.]
"""

"""
2. [30 points] Design an alternative, faster algorithm for this problem that
uses at most 2k+1 multiplications in the "mexp" function. You may not use the
Python "**" operator in your solution (if it appears at all in your code you
will get 0 points).

Your solution must be faster than the naive solution, here is a sample run
from my solution:

$ python computational_number_theory/exercise_2.py
naive 2.43s
mexp 2.15s
Results matched? True

"""

def exp(a, n):
	r = 1
	for i in range(n.bit_length() - 1, -1, -1):
		r = (r*r) * (a if (n >> i) & 0x1 else 1)

	return r

def mexp(a, b, x, y):
	raise Exception("Define me!")

def naive(a, b, x, y):
	return exp(a, x) * exp(b, y)

def timeit(m, *args):
	start = time.time()
	r = m(*args)
	end = time.time()

	print m.__name__, "%2.2fs" % (end-start)

	return r

def test_both(a, b, x, y):
	n = timeit(naive, a, b, x, y)
	m = timeit(mexp, a, b, x, y)

	print "Results matched?", n == m

	return None

if __name__ == '__main__':
	# Just one example, our grader will test more than this.
	test_both(512, 256, 22222222, 22222222)
