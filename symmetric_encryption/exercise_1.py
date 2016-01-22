import random

from crypto.primitives import AES, AES_I, random_string
from crypto.tools import xor_strings, add_int_to_string
from mock_se import SymmetricEncryption

"""
Let se represent any symmetric encryption scheme for which encryption is
deterministic. Show that se is not IND-CPA secure by giving an efficient
adversary A that achieves an adv(IND-CPA, se, A) = 1. Assume that the message
space is {0, 1}* (represented by a Python string of arbitrary characters).
"""

key_len = 16

se = SymmetricEncryption(key_len)
encrypt, decrypt = se.encrypt, se.decrypt

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

from crypto.games.game_lr import GameLR
from crypto.simulator.lr_sim import LRSim

if __name__ == '__main__':
    g = GameLR(encrypt, 16)
    s = LRSim(g, A)

    print "The advantage of your adversary is ~" + str(s.compute_advantage())
