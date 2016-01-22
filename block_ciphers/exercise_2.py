from crypto.primitives import *
from crypto.tools import *
from crypto.ideal.block_cipher import *
import sys, itertools

"""
Let E be a blockcipher  E:{0, 1}^8 x {0, 1}^8 --> {0, 1}^8
Define F: {0, 1}^16 x {0, 1}^16 --> {0, 1}^16 by:

Notes:
Derived from lecture 3 slide 40.
Sizes in comments are bits, sizes in code are in bytes (bits * 8).
"""

# Block & key size in bytes.
block_len, key_len = 2, 2

E = BlockCipher(key_len/2, block_len/2)
 
def F(k, x):
    """
    Blockcipher F made by composition with smaller function E.

    :param k: cipher key
    :param x: plaintext messager
    :return: cipher text
    """
    k1, k2 = split(k)
    x1, x2 = split(x)

    y1 = E.decrypt(k1, xor_strings(x1, x2))
    y2 = E.encrypt(k2, bitwise_complement_string(x2))

    return y1 + y2

"""
1. [30 points] Prove that F is a blockcipher by giving an efficiently computable
               inverse F_I:
"""

def F_I(k, c):
    """
    Fill this in, this is the inverse of F.

    :param k: cipher key
    :param c: cipher text
    :return: plain text
    """

    return None

"""
2. [20 points] What is the running time of a 4-query exhaustive key-search
               attack on F?
--&--
[Answer here].
"""

"""
3. [50 points] Give a 4-query key-recovery attack in the form of an adversary A
specified in code, achieving Adv(kr, F, A) = 1 and having running time
O(2^(8) * T_{E}) (T_{E} is the running time of the encryption function E),
where the big-oh hides some small constant.
"""


def A(fn):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for.

    :param fn: This is the oracle supplied by GameKR, you can call this
    oracle to get an "encryption" of the data you pass into it.
    :return: return the a string that represents a key guess.
    """

    pass

from crypto.games.game_kr import GameKR
from crypto.simulator.kr_sim import KRSim

if __name__ == '__main__':
    g = GameKR(F, key_len, block_len)
    s = KRSim(g, A)

    key = random_string(key_len)

    for j in range(100):
        message = random_string(block_len)
        cypher = F(key, message)
        if message != F_I(key, cypher):
            print "Your Decryption function is incorrect."
            sys.exit()

    print "Your Decryption function appears correct."

    print "The advantage of your adversary is ~" + str(s.compute_advantage(20))
