
class myWord:
    
    def __init__(self, word):
        self.word = [c for c in word]
        self.length = len(self.word)

    def insert(self, idx, c):
        self.word.insert(idx, c)

    def remove(self, idx):
        self.word.pop(idx)

    def replace(self, idx, c):
        self.word = c

        
if __name__ == "__main__":
    pass
