import random

n = 4
population = [random.randint(0, 31) for i in range(n)]
print(population)

def f(x):
    return x ** 2

def genetic_algorithm():
    global n, population

    # selection
    fx = [f(i) for i in population]
    prob = [i / sum(fx) for i in fx]
    expected_count = [n * i for i in prob]
    actual_count = [round(i) for i in expected_count]
    
    selection = []
    for i in range(len(actual_count)):
        cnt = actual_count[i]
        for j in range(cnt):
            selection.append(population[i])
    n = len(selection)
    
    # crossover
    mates = []
    for s in selection:
        mate = s
        while mate == s:
            mate = random.choice(selection)
        mates.append(mate)
    
    crossed = [0] * n
    for i in range(n):
        c = random.randint(0, 3)
        for j in range(0, c + 1):
            crossed[i] = (crossed[i] | ((1 << j) & (selection[i])))
        for j in range(c + 1, 4 + 1):
            crossed[i] = (crossed[i] | ((1 << j) & (mates[i])))

    # mutation
    # 20% mutation chance
    mutated = crossed.copy()
    for i in range(n):
        chance = random.randint(1, 5)
        if chance == 1:
            m = random.randint(0, 4)
            mutated[i] = (mutated[i] ^ (1 << m))

    population = mutated
    print(population)

for itr in range(10):
    genetic_algorithm()
