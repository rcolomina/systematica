# coin toss simulator
from numpy.random import rand

def toss(p=0.5):
    # Toss a coin with P(H) = p. head = 1, tails = 0
    assert(0 <= p <= 1)
    if rand() <= p:
        return 1
    else:
        return 0

def testToss(p, N):
    cum_sum = 0
    for _ in range(N):
        cum_sum += toss(p)
    return cum_sum

def tossInRow(p, s):
    tosses = 2
    assert(len(s) == 2)
    coin = {'H': 1, 'T': 0}
    last_2 = toss(p)
    last = toss(p)
    while not (last_2 == coin[s[0]] and last == coin[s[1]]):
        last_2 = last
        last = toss(p)
        tosses += 1
    return tosses

def testTossInRow(s, p='random', m=10, N=10**5):
    random = False
    if p == 'random':
        random = True
    else:
        assert(0<=p<=1)
    for _ in range(m):
        if random:
            p = rand()
        count = 0
        totalSum = 0
        for __ in range(N):
            count += 1
            totalSum += tossInRow(p, s)
        simulated = totalSum/count
        theoretical = {"HH": (1 + p)/(p**2), "HT": 1/(p*(1-p))}
        print("p = {:6f}\tSimulated = {:6f}\tTheoretical = {:6f}".format(p,simulated, theoretical[s]))

        
if __name__ == "__main__":
    print("Testing expected number of tosses to see 'HH'...")
    testTossInRow('HH')
    print()
    print("Testing expected number of tosses to see 'HT'...")
    testTossInRow('HT')
