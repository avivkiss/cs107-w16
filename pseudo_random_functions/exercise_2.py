from crypto.primitives import AES, AES_I, random_string
from crypto.tools import split, xor_strings
from crypto.ideal.hash_function import HashFunction

"""
Note: Based on exercise in slide 31, PRF lecture.

Let g: {0, 1}^k x {0, 1}^l --> {0, 1}^l be a family of functions (it is
arbitrary, but given, meaning known to the adversary) and let r>= 1 be an
integer. The r-round Feistel cipher associated to G is the family of functions
G(r): {0, 1}^k x {0, 1}^2l --> {0, 1}^2l, defined as follows for any key
K <- {0, 1}^k and input x <- {0, 1}^2l:
"""

# Block & key size in bytes.
block_len = 16
key_len = 16

g = HashFunction(block_len, key_len).hash

def G(r):
    def _G(k, x):
        l_0, r_0 = split(x)

        L, R = [l_0], [r_0]

        for i in range(1, r + 1):
            L.append(R[i-1])
            R.append(xor_strings(g(k, R[i-1]), L[i-1]))

        return L[r] + R[r]
    return _G

"""
1. Show that G(1) is not a secure PRF by presenting a practical adversary A_1
such that Adv(prf, F, A_1) = 1 - 2^-l. Fill in the code for adversary A, make
only one Fn query. Justify why your advantage is 1 - 2^-l.
--&--
[Answer here].
"""

def A_1(fn):
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
2. Show that G(2) is not a secure PRF by presenting a practical adversary A_2
such that Adv(prf, F, A_2) = 1 - 2^-l. Fill in the code for adversary A, make
only two Fn queries. Justify why your advantage is 1 - 2^-l.
--&--
[Answer here].
"""

def A_2(fn):
    """
    You must fill in this method.

    :param fn: This is the oracle supplied by GamePRF, you can call this
    oracle to get an "encryption" of the data you pass into it.
    :return: return 1 to indicate your adversary believes it is the real world
    and return 0 to indicate that your adversary believes it is in the random
    world.
    """

    pass


from crypto.games.game_prf import GamePRF
from crypto.simulator.world_sim import WorldSim

if __name__ == '__main__':
    g_1 = GamePRF(G(1), key_len, 2*block_len)
    s_1 = WorldSim(g_1, A_1)

    g_2 = GamePRF(G(2), key_len, 2*block_len)
    s_2 = WorldSim(g_2, A_2)

    print "The advantage of your adversary A_1 is ~" + \
                                        str(s_1.compute_advantage())

    print "The advantage of your adversary A_2 is ~" + \
                                        str(s_2.compute_advantage())
