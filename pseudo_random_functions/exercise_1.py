from crypto.primitives import AES, AES_I
from crypto.tools import *

"""
Note: Based on exercise in slide 30, PRF lecture.

The family of functions F: {0, 1}^128 x {0, 1}^128 --> {0, 1}^128 is defined by:
"""

# Block & key size in bytes.
block_len = 16
key_len = 16

F = lambda k, m: AES(m, k)

"""
Show that F is not a secure PRF by presenting a practical adversary A such
that Adv(prf, F, A) is close to one and makes at most 2 queries to its Fn
oracle. Fill in the code for adversary A, verify it's advantage by running your code and describe the running time.
"""

def A(fn):
    """
    You must fill in this method.

    :param fn: This is the oracle supplied by GamePRF, you can call this
    oracle to get an "encryption" of the data you pass into it.
    :return: return 1 to indicate your adversary believes it is the real world
    and return 0 to indicate that your adversary believes it is in the random
    world.
    """

    pass

"""
Formally prove that: 1. Your adversary has an advantage of 1 - 2^-128.
---&---
[Answer here].
"""

from crypto.games.game_prf import GamePRF
from crypto.simulator.world_sim import WorldSim

if __name__ == '__main__':
    g = GamePRF(F, key_len, block_len)
    s = WorldSim(g, A)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())
