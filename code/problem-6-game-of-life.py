import numpy as np

class State:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.array([[0]*width for _ in range(height)])
     
    def kill(self, n, m):
        self.grid[n][m] = 0
    
    def birth(self, n, m):
        self.grid[n][m] = 1

    def get_neighbors(self, n, m):
        return [[x, y] for x in range(n-1, n+2)
                       for y in range(m-1, m+2)
                       if [x, y] != [n, m]]
        
    def life_around(self, n, m):
        return sum([self.grid[x][y] for x, y in get_neighbors(n, m)])

        
class BoundedModel:
    def __init__(self, state):
        self.current_state = state
        self.next_state = None
        self.width = state.width
        self.height = state.height

    def inbbounds(self, n, m):
        return n < self.width and n >=0  and m < self.height and m>= 0

    def life_around(self, n, m):
        return sum([self.grid[x][y] for x, y in self.current_state.get_neighbors(n, m)
                                    if self.inbounds(x, y)])
        
    def survives(self, n, m):
        return sum(self.life_around(n, m)) == 3

    def get_next_state(self):
        width = self.current_state.width
        height = self.current_state.height

        self.next_state = self.current_state
        for n in range(width):
            for m in range(height):
                if self.survives(n, m):
                    self.next_state.birth(n, m)
                else:
                    self.next_state.kill(n, m)
        self.current_state = self.next_state        

    def develop(self, steps):
        for _ in range(steps):
            get_next_state()

class UnboundedModel:
    pass

if __name__ == "__main__":
    import sys
    
    l = len(sys.argv)
    if l > 2:
        print("Invalid arguments!")
    else:
        if l == 1:
            # default situation
            n = 30
        else:
            n = int(sys.argv[1])

    width = 10
    height = 10
