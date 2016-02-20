
from crypto.simulator.lr_sim import LRSim


class ALRSim(LRSim):
    """
    This simulator was written to be used with GameLR. It simulates the game
    with an Adversary and allows you to compute an approximate advantage.
    """

    def run(self, b):
        """
        Runs the game in a specific world.

        :param world: 1 or 0, for different worlds.
        :return: True for success and False for failure.
        """
        self.game.initialize(b)
        return self.game.finalize(self.adversary(self.game.lr, self.game.pk))
