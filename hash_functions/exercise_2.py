from crypto.games.game_cr import GameCR
from crypto.simulator.cr_sim import CRSim
from crypto.ideal.block_cipher import BlockCipher
from crypto.primitives import *
from crypto.tools import *

"""
Let D be the set of all strings whose length is a positive multiple of 128.
Define the has function H: {0,1}^k x D -> {0,1}^128 be defined as
follows:
"""

# Block & key size in bytes.
block_len = 16
key_len = 16

def H(k, m):
    """
    Hash function.

    :param k: Key used by the hash function, must be of size key_len
    :param m: Message hashed by the function, must be of length n * block_len
    """
    if len(m) % block_len != 0:
        raise ValueError("Input length is outside of parameters.")

    w = []
    c = ["\x00" * 16]
    m = split(m, block_len)

    for b in m:
        w += [AES(k, xor_strings(c[-1], b))]
        c += [AES(k, xor_strings(w[-1], b))]

    return c[-1]

"""
[30 points] Show that H is not collision resistant by presenting a practical
adversary (A) such that adv(cr, H, A) = 1. Note that the running time of
the birthday attack is too large for it to be considered practical.
"""

def A(k):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for.

    :param k: This is key used as the seed to the provided hash function
    :return: return 2 messages, m1 and m2, that your adversary believes collide.
    """

    return None, None


if __name__ == '__main__':
    g = GameCR(H, key_len)
    s = CRSim(g, A)

    print "\nThe advantage of your adversary is ~" + str(s.compute_advantage())
