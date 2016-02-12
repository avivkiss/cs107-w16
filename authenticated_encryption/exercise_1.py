from crypto.primitives import AES, AES_I, random_string
from crypto.tools import xor_strings, split, join, int_to_string

"""
Let E denote AES. Let K be the key generation algorithm that returns a
random 128-bit AES key K and let SE = (K, E, D) be the
symmetric encryption scheme whose encryption and decryption algorithms are
as follows:
"""

block_len = 16
key_len = 16

def E(k, m):
    if len(m) != block_len * 4: return None

    m = split(m, block_len)

    c = [random_string(block_len)]
    t = ["\x00" * block_len]

    for i in range(4):
        c += [AES(k, xor_strings(m[i], c[i]))]
        t += [AES(k, xor_strings(m[i], t[i]))]

    return join(c), t[-1]

def D(k, (c, t)):
    if len(c) != block_len * 5: return None

    c = split(c, block_len)

    m = []
    tm = ["\x00" * block_len]

    for i in range(4):
        m += [xor_strings(AES_I(k, c[i+1]), c[i])]
        tm += [AES(k, xor_strings(m[i], tm[i]))]

    if tm[-1] != t: return None

    return join(m)


"""
1. [20 points] Give an IND-CPA adversary that shows that this sceme is not
IND-CPA secure:
"""

def A_1(lr):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for.

    :param lr: This is the oracle supplied by GameLR, you can call this
    oracle to get an encryption of the data you pass into it.
    :return: return 1 to indicate your adversary believes it is the right world
    and return 0 to indicate that your adversary believes it is in the left
    world.
    """
    pass


"""
2. [30 points] Give an INT-CTXT adversary that shows that this sceme is not
INT-CTXT secure:
"""

def A_2(enc, dec):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for. You must call dec on a valid candidate to win the game.

    :param enc: This is an oracle supplied by GameINTCTXT, you can call this
    oracle to get an encryption of the data you pass into it.
    :param dec: This is an oracle supplied by GameINTCTXT, you can call this
    oracle to get a decryption of the data you pass into it.
    """
    pass


"""
3. [15 points] Is SE an Encrypt-and-MAC construction? Justify your answer.
--&--
[Answer here].
"""

from crypto.games.game_lr import GameLR
from crypto.simulator.lr_sim import LRSim

from crypto.games.game_int_ctxt import GameINTCTXT
from crypto.simulator.ctxt_sim import CTXTSim

if __name__ == '__main__':
    g1 = GameLR(E, 16)
    s1 = LRSim(g1, A_1)

    g2 = GameINTCTXT(E, D, key_len)
    s2 = CTXTSim(g2, A_2)

    print "The advantage of A_1 adversary is ~" + str(s1.compute_advantage())
    print "The advantage of A_2 adversary is ~" + str(s2.compute_advantage())
