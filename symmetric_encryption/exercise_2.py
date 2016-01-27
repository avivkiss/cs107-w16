import random

from crypto.primitives import AES, AES_I, random_string
from crypto.tools import xor_strings, add_int_to_string, int_to_string, split

"""
Let key k be a random 128-bit string. Let encrypt be the following encryption
algorithm, based on the block cipher AES. A message must be a string whose length is a positive multiple of 128.
"""
block_len, key_len = 16, 16

def encrypt(k, x):
    """
    :param k: The key used to encrypt/decrypt the message
    :param x: The plaintext to be decrypted
    :return: return the encryption of plaintext x
    """
    r = random_string(block_len)
    c = r
    for i in range(1, len(x) / block_len + 1, 1):
        w_i = add_int_to_string(r, i, block_len * 8)
        x_i = x[((i - 1) * block_len): (i * block_len)]
        c += AES(k, xor_strings(x_i, w_i))
    return c

"""
1. [30 points] Specify a decryption algorithm decrypt such that SE = (K,E,D)
is a symmetric encryption scheme
"""

def decrypt(k, c):
    """
    You must fill in this method. This is the decryption algorithm that the
    problem is asking for.

    :param k: The key used to encrypt/decrypt the message
    :param c: The cipher text to be decrypted
    :return: return the decryption on the cipher text c
    """
    pass

"""
2. [30 points] Show that this scheme is insecure by presenting a practical
adversary such that the Adv(ind-cpa, SE, A) = 1 making only one LR query.
"""

def A(lr):
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
3. [10 points] Provide a succinct analysis justifying the claimed advantage:
--&--
[Answer here.]
"""

from crypto.games.game_lr import GameLR
from crypto.simulator.lr_sim import LRSim

if __name__ == '__main__':
    g = GameLR(encrypt, key_len)
    s = LRSim(g, A)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())

    key = random_string(key_len)

    for j in range(100):
        blocks = random.randrange(100)
        message = random_string(blocks*block_len)
        cypher = encrypt(key, message)
        if message != decrypt(key, cypher):
            print "Your Decryption function is incorrect"
    print "Your Decryption function is correct"
