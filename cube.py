class Cube:
    cubestate = dict()
    statenames = "flt frt flb frb plt prt plb prb ft fr fl fb pt pr pl pb lt lr lb lr".split()
    state = dict()
    def __init__(self):
        print self.statenames
        for i in range(len(self.statenames)):
            self.state[self.statenames[i]] = self.state[i] = 0
        print self.state
        self.state[4] = 'blue'
        print self.state

