goal = "ABCD"
# goal = "DCBA"

state = ["DCAB"]
# state = ["BCDA"]
# state = ["ABDC"]

def hill_climb(state):
    print(state)

    while (not goal.startswith(state[0])) and len(state) != len(goal):
        state.append(state[0][len(state[0]) - 1])
        state[0] = state[0][0 : len(state[0]) - 1]
        print(state)

    for i in range(len(state)):
        if state[i].startswith(goal[0]):
            state[0], state[i] = state[i], state[0]
            break
    
    for i in range(1, len(goal)):
        for j in range(1, len(state)):
            if state[j][0] == goal[i]:
                state[0] += state[j]
                state.pop(j)
                print(state)
                break
            
hill_climb(state)
