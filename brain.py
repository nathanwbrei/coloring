from copy import deepcopy
from pync import Notifier

def search(num_colors, graph):
    # Do a depth-first search over the configuration space, keeping a
    # stack of assignments and variable domains.

    init_cfg = Assignment(num_colors, graph)
    stack = [(init_cfg, init_cfg.choose())]

    while stack and not stack[-1][0].complete():
        
        cur_var, cur_vals = stack[-1][1]

        if not cur_vals:
            stack.pop()
        else:
            # If we still have options with our current stack frame
            new_val = cur_vals.pop(0)
            new_cfg = stack[-1][0].set(cur_var, new_val)

            if new_cfg.propagate():
                stack.append((new_cfg, new_cfg.choose()))

    if stack and stack[-1][0].complete():
        Notifier.notify("Found a solution!",title="GraphColorizer")
        return [v[0] for v in stack[-1][0].table] 
    else:
        print "Failed @num_colors=%d" % num_colors
        Notifier.notify("Failed @num_colors=%d. :(" % num_colors, title="GraphColorizer")
        return search(num_colors+1, graph)
    

        
class Assignment(object):
    def __init__(self, num_colors, graph):
        # Create a new table. table[var]=[color1, color2,...]

        self.table = [[i for i in xrange(num_colors)] for j in xrange(len(graph))] 
        self.graph = graph

    def choose(self):
        # Find the most constrained node, return (id, domain)
        imin = -1 
        xmin = self.table[0]
        lmin = 100000000 

        for i,x in enumerate(self.table):
            if len(x) < lmin and len(x) > 1:
                imin = i
                xmin = x
                lmin = len(x)
        if imin == -1:
            print "Found a solution!"
        return (imin, xmin)


    def complete(self):
        for i in self.table:
            if len(i) != 1:
                return False
        return True


    def set(self, var, val):
        # Returns a new Assignment object with the var set to val
        result = deepcopy(self)
        result.table[var] = [val]
        return result

    def propagate(self):
        # Propagates the `!=` constraint. Returns true if feasible
        frontier = set(range(len(self.table)))
        while frontier:
            icur = frontier.pop()
            xcur = self.table[icur] 
            neighbors = self.graph[icur]

            if len(xcur) == 1:
                for n in neighbors:
                    if xcur[0] in self.table[n]:
                        self.table[n].remove(xcur[0])
                        if len(self.table[n]) == 0:
                            return False
                        frontier.add(n)
        return True





         


