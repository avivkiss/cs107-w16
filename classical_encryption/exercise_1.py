import random, itertools
from collections import defaultdict
"""
Let Z_8 = {0, 1, ...7}. Consider the symmetric encryption scheme in which
a message m = m[0]m[1]m[2]m[3] is a four-digit string containing only numbers 
0-7, a permutation of Z_8 is randomly selected as a key pi, and the ciphertext
c = c[0]c[1]c[2]c[3] = E(pi, m), also a four digit string from digits 0-7 is
computed as follows:
"""

MOD = 8

def E(pi, m):
    """
    :param pi: A random permutation of range(8).
    :param m: A string of integers of length 4.
    :return: ciphertext as string.
    """
    temp = []
    c = ""
    for i in range(4):
        temp.append((int(m[i]) + i + 1) % MOD)
        c += str(pi[temp[i]])

    return c

"""
[10 points] Specify a decryption algorithm D such that SE = (K, E, D) is a
symmetric encryption scheme (slide 2) meeting the correct decryption requirement
(slide 3).
"""
 
def D(pi, c):
    """
    You must fill in this function.

    :param pi: A random permuation of range(8)
    :param c: ciphertext as string
    :return: the correct decryption of c (i.e. m)
    """

    return None

"""
[20 points] Is this scheme a substitution cipher as per the definition of
slides 13, 14? Why or why not? (Please answer within this comment and below
the line.)
--&--
[Answer here].
"""


"""
[10 points] Write a function that tests whether or not a scheme is perfectly
secure as per the definition of slide 46. Assume that the scheme uses a
permutation of the alphabet as the key. 

[20 points] Is the above scheme perfectly secure? Why or why not?
--&--
[Answer here].
"""

def is_perfectly_secure(E, alphabet, text_len):
    """
    You must fill in this function.

    :param E: The encyption function that will be tested
    :param alphabet: The alphabet used in the plain text.
    :param text_len: Length of the plain text.
    :return: True if perfectly secure, false otherwise.
    """

    return None

if __name__ == '__main__':
    pi = [str(i) for i in range(MOD)]
    random.shuffle(pi)

    test_text = "1234"

    if D(pi, E(pi, test_text)) == test_text:
        print "Passed simple decryption test."
    else:
        print "Failed simple decryption test."

    if is_perfectly_secure(E, range(MOD), 4):
        print "According to 'is_perfectly_secure()' E is secure."
    else:
        print "According to 'is_perfectly_secure()' E is insecure."
