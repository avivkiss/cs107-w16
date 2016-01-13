from crypto.primitives import *
from crypto.tools import *

"""
Let the family of functions E: {0, 1}^128 x {0, 1}^128 --> {0, 1}^128 be a
blockcipher and A an adversary. The TKR game measures A's ability to find the
target key (as defined in lecture 3 slide 21 and in games.game_tkr).

Let the advantage of the adversary for TKR with cipher E be
Adv(tkr, E, A) = Pr[tkr(A, E) => True].

[30 points] Now, given E with block_len and key_len design a blockcipher

E: {0, 1}^128 x {0, 1}^128 --> {0, 1}^128 such that:
- For any q > 0 there is a q-query adversary A with Adv(kr, E, A) = 1
- Adv(tkr, E, A) <= 2^(-128) for any A.

[10 points] Give an example of such an adversary in A with Adv(kr, E, A) = 1
            and Adv(tkr, E, A) <= 2^(-128).

Note:
Derived from slide 21 lecture 3 (block ciphers).
Sizes in comments are bits, sizes in code are in bytes (bits * 8).
"""

# Block & key size in bytes.
block_len, key_len = 16, 16

def E(k, m):
    """
    You must fill in this function, this is your block cipher that must have
    the above properties.

    :param k: This is the key for the block cipher.
    :param m: Message for the block cipher.
    :return: Ciphertext.
    """

    pass


def A(fn):
    """
    You need to fill in an adversary making some number of queries q > 0
    that has the above properties.

    :param fn: This is the oracle supplied by GameKR, you can call this
    oracle to get an "encryption" of the data you pass into it.
    :return: return the a string that represents a key guess.
    """

    pass

"""
Running this code will give you some intuition about whether or not your code
is working. However you must explain two things:

1. [30 points] Why does your adversary have Adv(kr, E, A) = 1?
2. [30 points] Why is the tkr advantage small for *any* A?
--&--
[Answer here].
"""


from crypto.games.game_kr import GameKR
from crypto.games.game_tkr import GameTKR
from crypto.simulator.kr_sim import KRSim

if __name__ == '__main__':
    g1 = GameKR(E, key_len, block_len)
    s1 = KRSim(g1, A)

    g2 = GameTKR(E, key_len, block_len)
    s2 = KRSim(g2, A)

    print "The advantage of your adversary under KR is ~" + str(s1.compute_advantage())
    print "The advantage of your adversary under TKR is ~" + str(s2.compute_advantage())
