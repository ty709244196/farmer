### File farmer.py
### Implements the farmer problem for state space search

from search import *


class FarmerState(ProblemState):
    """
    f -> farmer
    w -> wolf
    s -> sheep
    g -> grain
    """

    def __init__(self, f, w, s, g):
        self.f = f
        self.w = w
        self.s = s
        self.g = g

    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        return "(" + str(self.f) + "," + str(self.w) + "," + str(self.s) + "," + str(self.g) + ")"

    def illegal(self):
        """
        wolf and sheep can't be in the same side if farmer is not with them.
        sheep and grain can't be in the same side if farmer is not with them.
        """
        if self.w == self.s:
            if self.f != self.w:
                return 1

        if self.s == self.g:
            if self.f != self.s:
                return 1
        return 0

    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.f == state.f and self.w == state.w and self.s == state.s and self.g == state.g

    def f2b(self):
        return FarmerState(1, self.w, self.s, self.g)

    def fw2b(self):
        """
        if farmer and wolf both in A, go to B
        else remain unchange.
        """
        if self.f == self.w:
            return FarmerState(1, 1, self.s, self.g)
        else:
            return FarmerState(0,1,self.s,self.g)

    def fs2b(self):
        if self.f == self.s:
            return FarmerState(1, self.w, 1, self.g)
        else:
            return FarmerState(0,self.w, 1, self.g)

    def fg2b(self):
        if self.f == self.g:
            return FarmerState(1, self.w, self.s, 1)
        else:
            return FarmerState(0,self.w,self.s,1)

    def f2a(self):
            return FarmerState(0, self.w, self.s, self.g)

    def fw2a(self):
        if self.f == self.w:
            return FarmerState(0, 0, self.s, self.g)
        else:
            return FarmerState(1,0,self.s,self.g)

    def fs2a(self):
        if self.f == self.s:
            return FarmerState(0, self.w, 0, self.g)
        else:
            return FarmerState(1, self.w, 0, self.g)

    def fg2a(self):
        if self.f == self.g:
            return FarmerState(0, self.w, self.s, 0)
        else:
            return FarmerState(1, self.w, self.s, 0)

    def operatorNames(self):
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """
        return ["farmer to B", "farmer, wolf to B", "farmer, sheep to B", "farmer, grain to B", "Farmer to A",
                "farmer, wolf to A", "farmer, sheep to A", "farmer, grain to A"]

    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.
        """
        return [self.f2b(), self.fw2b(), self.fs2b(),
                self.fg2b(), self.f2a(),
                self.fw2a(), self.fs2a(), self.fg2a()]


Search(FarmerState(0, 0, 0, 0), FarmerState(1, 1, 1, 1))
