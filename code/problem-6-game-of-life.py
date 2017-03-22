import numpy as np

class State:
    def __init__(self, width=10, height=10, file_name=None):
        if file_name != None:
            # read state from file
            with open(file_name, 'r') as file:
                lines = file.readlines()
                self.width, self.height = map(int, lines[0].strip().split())
                self.grid = [[0]*width for _ in range(height)]
                for line in lines[1:]:
                    x, y = map(int, line.strip().split())
                    self.birth(x, y)
        else:
            # create state with all 0's'
            self.width = width
            self.height = height
            self.grid = [[0]*width for _ in range(height)]
     
    def kill(self, n, m):
        self.grid[m][n] = 0
    
    def birth(self, n, m):
        self.grid[m][n] = 1

    def get_neighbors(self, n, m):
        return [[x, y] for x in range(n-1, n+2)
                       for y in range(m-1, m+2)
                       if [x, y] != [n, m]]
        
    def life_around(self, n, m):
        return sum([self.grid[y][x] for x, y in get_neighbors(n, m)])

    def print_state(self):
        for m in range(self.height):
            current_line = ''
            for n in range(self.width):
                current_line += str(self.grid[m][n]) + ' '
            current_line = current_line.strip()
            print(current_line)
        print()

        
class BoundedModel:
    def __init__(self, state):
        self.current_state = state
        self.next_state = None
        self.width = state.width
        self.height = state.height

    def inbounds(self, n, m):
        return n < self.width and n >= 0 and m < self.height and m >= 0

    def life_around(self, n, m):
        return sum([self.current_state.grid[y][x] for x, y in self.current_state.get_neighbors(n, m)
                                                  if self.inbounds(x, y)])
        
    def survives(self, n, m):
        return self.life_around(n, m) == 3

    def get_next_state(self):
        self.next_state = State(width=self.width, height=self.height)
        for n in range(self.width):
            for m in range(self.height):
                if self.survives(n, m):
                    self.next_state.birth(n, m)
                else:
                    self.next_state.kill(n, m)
        self.current_state = self.next_state        
            
    def develop(self, steps, verbose=True):
        if verbose:
            print("State at time t=0:")
            self.current_state.print_state()
        for step in range(steps):
            self.get_next_state()
            if verbose:
                print("State at time t={}:".format(step+1))
                self.current_state.print_state()


class UnboundedModel:
    # For the unbounded model we use the bounded model with resizing controls
    def __init__(self, state):
        self.current_state = state
        # keep track of the location of the state grid for expanding/reducing
        self.origin = [0, 0]
        self.next_state = None
        self.width = state.width
        self.height = state.height
        
    def expand_state():
        new_width = self.width * 2
        new_height = self.height * 2
        new_state = State(width=new_width, height=new_height)
        ox, oy = self.width//2, self.height//2
        for n in range(self.width):
            for m in range(self.height):
                new_state.grid[oy + m][ox + n] = self.current_state.grid[m][n]
        self.current_state = new_state
        self.origin = [ox, oy]
        
    def reduce_state():
        pass

    def survives(self, n, m):
        return self.current_state.life_around(n, m) == 3

    def get_next_state(self):
        self.next_state = State(width=self.width, height=self.height)
        for n in range(-1, self.width + 1):
            for m in range(-1, self.height + 1):
                if self.survives(n, m):
                    self.next_state.birth(n, m)
                else:
                    self.next_state.kill(n, m)
        self.current_state = self.next_state        
            
    def develop(self, steps, verbose=True):
        if verbose:
            print("State at time t=0:")
            self.current_state.print_state()
        for step in range(steps):
            self.get_next_state()
            if verbose:
                print("State at time t={}:".format(step+1))
                self.current_state.print_state()




    
def generate_random_state(max_width=10, max_height=10):
    from numpy.random import randint
    width = randint(1, max_width)
    height = randint(1, max_height)
    state = State(width=width, height=height)
    for n in range(height):
        for m in range(width):
            state.grid[n][m] = randint(0, 2)
    return state
    
if __name__ == "__main__":
    import sys
    # Process command line arguments
    l = len(sys.argv)
    if l > 3:
        print("Invalid arguments!")
    else:
        if l == 1:
            # default situation
            #initial_state = State(file_name="initial-state.txt")
            initial_state = generate_random_state()
            n = 5
        elif l == 2:
            if sys.argv[1].isalnum():
                n = int(sys.argv[1])
                initial_state = generate_random_state()
            else:
                initial_state = State(file_name=sys.argv[1])
                n = 5
        else:
            initial_state = State(file_name=sys.argv[1])
            n = int(sys.argv[2])

    system = BoundedModel(initial_state)
    system.develop(n)
