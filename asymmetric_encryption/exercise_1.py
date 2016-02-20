from crypto.primitives import *
from crypto.tools import *

import random
import IPython

"""
Based on slide 47.

Let k be an integer and let K_{RSA} be an RSA generator with associated
security parameter 8k. Assume that if (N, p, q, e, d) is an output of K_{RSA}
then (p - 1)/2 and (q-1)/2 are primes larger than 2^2k. Let P denote the set
of all odd primes smaller than 2^k. Consider the encryption and decryption
algorithms below, where the message M is in Z*N:
"""

k = 64

def prime_between_withp(s, e):
    r = prime_between(s, e)

    while not is_prime((r-1)/2):
        print "Miss"
        r = prime_between(s, e)

    print "Found", r
    return r

def K():
    # This took too long so I chose them for you in this case, your solutions
    # must work for any p, q with the given properties.
    # p = prime_between_withp(2**(k*8/2-1), 2**(k*8) - 1)
    # q = prime_between_withp(2**(k*8/2-1), 2**(k*8) - 1)
    p = 3077360440446421525121754622214670349641041744074080342959049511112312228322524553636624308027535291775883958590538761797182074340668403355817146591774223
    q = 5975329872674470534923271120753151867222383992076504176868797961682511858688686162580143452407809780744069451070787203506739027595255600805671318343638143
    N = p * q

    pk = N
    sk = (N, p, q)

    return (pk, sk)

def E(pk, m):
    N = pk
    e = prime_between(3, 2**k) # draw from P
    return (exp(m, e, N), e)

"""
1. [15 points] Prove that P is a subset or euqal to Z*phi(N) for any N output by
K.
--&--
[Answer]
"""

"""
2. [30 points] Provide D and Proof
Specify in Python a O(k^3)-time decryption algorithm D such that AE = (K, E, D)
is an asymmetric encryption scheme satisfying the correct decyption condition,
and prove that this is indeed the case. Your code may invoke basic operators
from Python (like +, *, /, %) and from the "crypto.tools" (like egcd and modinv)
which you can assume to have the running time of those listed in the
Computaitonal Number Theory slides and you should use part 1 above.
--&--
[Proof of correctness.]
"""

def D(sk, (c, e)):
    return None

"""
3. Specify in Python an adversary A making one LR query and acheiving
Adv(ind-cpa, AE, A) = 1. The messages int he LR query must both be in Z*N, and
the running itme of A should be O(k), where k is the security parameter
associated to K_{RSA} and the time taken by game procedures to execute is not
counted in the time of A.
"""

def A(lr, pk):
    return None


from game_alr import GameALR
from alr_sim import ALRSim

if __name__ == '__main__':
    g = GameALR(E, K)
    s = ALRSim(g, A)

    print "The advantage of your adversary is ~" + str(s.compute_advantage(200))

    pk, sk = K()

    C = E(pk, 2484401)

    print "Simple test case works?", D(sk, C) == 2484401
