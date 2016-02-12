from crypto.primitives import random_string
from crypto.tools import *
from Crypto.Hash import HMAC, SHA

import random

"""
1. [45 points] Specify a (purely) SHA1-based (“Purely SHA1 based” means SHA1
is the only cryptographic primitive you may use, you may use HMAC-SHA1).
IND-CPA+INT-CTXT-secure symmetric encryption scheme SE = (K, E, D) by giving
Python code for the E and D (K is defined for you). You may use algorithms
presented in slides as inspiration. Your scheme should be able to encrypt any
message M where |M| mod 160 = 0 and 160 <= |M| < 2^64 (in bits). The ciphertext
should have length 320 + |M| bits, the key should have length at most 320 bits
and both encyrption and decryption should be efficient. Your scheme should have
an 80-bit level of security.
"""

def HMAC_SHA1(k, m):
    return HMAC.new(k, m, SHA).digest()

# Block and key size in bytes.
block_len = 20
key_len = None # Define me

def E(k, m):
    return None, None

def D(k, (c, t)):
    return None

def K():
    return random_string(key_len)

"""
2. [15 points] Provide a convincing and **succinct** justification for the
security of your scheme.
--&--
[Answer here.]
"""

def A_1(lr):
    """
    Provided for experimentation (won't be graded).

    :param lr: This is the oracle supplied by GameLR, you can call this
    oracle to get an encryption of the data you pass into it.
    :return: return 1 to indicate your adversary believes it is the right world
    and return 0 to indicate that your adversary believes it is in the left
    world.
    """
    return None


def A_2(enc, dec):
    """
    Provided for experimentation (won't be graded).

    :param enc: This is an oracle supplied by GameINTCTXT, you can call this
    oracle to get an encryption of the data you pass into it.
    :param dec: This is an oracle supplied by GameINTCTXT, you can call this
    oracle to get a decryption of the data you pass into it.
    """
    pass

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

    key = K()

    for j in range(100):
        blocks = random.randrange(100)
        m = random_string(blocks*block_len)
        c, t = E(key, m)
        bad = False
        if m != D(key, (c, t)):
            print [len(m), len( E(key, m)[0]),  len(D(key, (c, t)))]
            bad = True
    if bad:
        print "Your Decryption function is incorrect"
    else:
        print "Your Decryption function is correct"
