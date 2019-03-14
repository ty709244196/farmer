from informedSearch import *
"""
Problem     BFS     A*(tiles)    A*(dist)
A           4       3           3
B           77      8           7
C           179     18          10
D           666     48          20
E           809     44          20
F           1843    110         123
G           5396    375         61
H           48707   3290        186
"""

class EightPuzzle(InformedProblemState):
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def __str__(self):
        return self.puzzle

    def illegal(self):
        if self.puzzle == -1: return 1
        return 0

    def equals(self, state):
        return self.puzzle == state.puzzle

    def left(self):
        """
        if 0 is not on the left edge, move 0 to the left
        """
        i = self.puzzle.index('0')
        if i not in (0, 3, 6):
            index = i - 1
            newpuzzle = self.puzzle[0: index] + '0' + self.puzzle[index] + self.puzzle[i + 1:]
            return EightPuzzle(newpuzzle)
        return EightPuzzle(-1)

    def right(self):
        """
        if 0 is not on the right edge, move 0 to the right
        """
        i = self.puzzle.index('0')
        if i not in (2, 5, 8):
            j = i + 1
            newpuzzle = self.puzzle[0: i] + self.puzzle[j] + '0' + self.puzzle[j + 1:]
            return EightPuzzle(newpuzzle)
        return EightPuzzle(-1)

    def up(self):
        """
        if 0 is not on the top edge, move 0 up
        """
        i = self.puzzle.index('0')
        if i not in (0, 1, 2):
            j = i - 3
            newpuzzle = self.puzzle[0: j] + '0' + self.puzzle[j + 1: i] + self.puzzle[j] + self.puzzle[i + 1:]
            return EightPuzzle(newpuzzle)
        return EightPuzzle(-1)

    def down(self):
        """
        if 0 is not on the bottom edge, move 0 down
        """
        i = self.puzzle.index('0')
        if i not in (6, 7, 8):
            j = i + 3
            newpuzzle = self.puzzle[0: i] + self.puzzle[j] + self.puzzle[i + 1: j] + '0' + self.puzzle[j + 1:]
            return EightPuzzle(newpuzzle)
        return EightPuzzle(-1)

    def operatorNames(self):
        return ["left", "right", "up", "down"]

    def applyOperators(self):
        return [self.left(), self.right(), self.up(), self.down()]

    def heuristic(self, goal):
        """BFS"""
        sum = 0
        """A*(tiles)"""
        #sum = EightPuzzle.tiles(self, goal)
        """A*(dist)"""
        #sum = EightPuzzle.dist(self, goal)
        return sum

    def dist(self, goal):
        dist = 0
        for i in goal.puzzle:
            dist += abs(self.puzzle.index(i) - goal.puzzle.index(i))
        return dist

    def tiles(self, goal):
        count = 0
        for i in range(0, 9):
            if self.puzzle[i] != goal.puzzle[i]:
                count += 1
        return count


goal = '123804765'
a = '130824765'
b = '134862075'
c = '013425876'
d = '712803654'
e = '812704653'
f = '263405187'
g = '734615802'
h = '745603812'
InformedSearch(EightPuzzle(a), EightPuzzle(goal))
InformedSearch(EightPuzzle(b), EightPuzzle(goal))
InformedSearch(EightPuzzle(c), EightPuzzle(goal))
InformedSearch(EightPuzzle(d), EightPuzzle(goal))
InformedSearch(EightPuzzle(e), EightPuzzle(goal))
InformedSearch(EightPuzzle(f), EightPuzzle(goal))
InformedSearch(EightPuzzle(g), EightPuzzle(goal))
InformedSearch(EightPuzzle(h), EightPuzzle(goal))
