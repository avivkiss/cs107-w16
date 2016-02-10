from crypto.tools import *
from crypto.ideal.block_cipher import BlockCipher

import collections, itertools, random

from IPython import embed as debug

"""
Let E: {0, 1}^k x {0, 1)^n -> {0, 1)^n be a block cipher with
k, n = 32, 2 (in bytes).
Let D = { M (= {0, 1}* : 0 < |M| < n * 2^n and |M| mod n = 0}.
Let tag: {0, 1}^k x D -> {0, 1}^n be defined as follows:
"""

# Use n in bytes in code, in description 128.
n = 16/8
key_len = 32
E = BlockCipher(key_len/2, n).encrypt

def T(k, m):
    k_in, k_out = split(k)
    c = ["\x00" * n]

    m = split(m, n)

    for i in range(len(m)):
        c += [E(k_in, xor_strings(c[i], m[i]))]

    return E(k_out, c[-1])

def V(k, m, t):
    if T(k, m) == t:
        return 1
    else:
        return 0

"""
1. [40 points] Show that T is an insecure MAC by presenting a practical
adversary (A) making q <= 2^(n/2) (n = 16) queries to the tag oracle
(hint: try making 3 block queries) such that Adv(A) >= 0.3 * ((q)*(q-1)/2^n)
(approximately 0.3).
"""

def A(tag):
    """
    You must fill in this method. This is the adversary that the problem is
    asking for. Returns a (message, tag) pair.

    :param tag: This is an oracle supplied by GameUFCMA, you can call this
    oracle to get a "tag" for the data you pass into it.
    """

    return None, None

from crypto.games.game_ufcma import GameUFCMA
from crypto.simulator.ufcma_sim import UFCMASim

if __name__ == '__main__':
    g = GameUFCMA(T, V, key_len)
    s = UFCMASim(g, A)

    # If your code is taking too long try chaning 100 to something smaller,
    # make sure that your code finishes in about 11 seconds.
    print "The advantage of your adversary is ~" + str(s.compute_advantage(100))
