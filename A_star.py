adj = {
    'Arad' : [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Bucharest' :[('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni',85)],
    'Craiova' : [('Dobereta', 120), ('Riminicu Vilcea', 146), ('Pitesi', 138)],
    'Dobreta' : [('Mehadia', 75), ('Craiova', 120)],
    'Eforie' : [('Hirsova', 86)],
    'Fagaras' : [('Sibiu', 99), ('Bucharest', 211)],
    'Giurgiu': [('Bucharest', 90)],
    'Hirsova': [('Eforie', 86),('Urziceni',98)],
    'Iasi': [('Vaslui', 92),('Neamt',87)],
    'Mehadia' : [('Lugoj',70), ('Dobreta',75)],
    'Neamt' : [('Iasi',87)],
    'Oradea' : [('Zerind',75), ('Sibiu',151)],
    'Pitesti' : [('Rimnicu Vilcea',97),('Craiova',138),('Bucharest',101)],
    'Rimnicu Vilcea' : [('Sibiu',80),('Craiova',146),('Pitesti',97)],
    'Sibiu' : [('Oradea',151),('Arad',140),('Fagaras',99),('Rimnicu Vilcea',80)],
    'Timisoara' : [('Arad',118),('Lugoj',70)],
    'Urziceni' : [('Bucharest',85),('Vaslui',142),('Hirsova',98)],
    'Vaslui' : [('Iasi', 92), ('Urziceni', 142)],
    'Zerind' : [('Arad', 75), ('Oradea', 71)]
}

h = {
    'Arad' : 366,
    'Bucharest' : 0,
    'Craiova' : 160,
    'Dobreta' : 242,
    'Eforie' : 161,
    'Fagaras' : 178,
    'Giurgiu' : 77,
    'Hirsova' : 151,
    'Iasi' : 226,
    'Lugoj' : 244,
    'Mehadia' : 241,
    'Neamt' : 234,
    'Oradea' : 380,
    'Pitesti' : 98,
    'Rimnicu Vilcea' : 193,
    'Sibiu' : 253,
    'Timisoara' : 329,
    'Urziceni' : 80,
    'Vaslui' : 199,
    'Zerind' : 374,
}

initial = input("Enter the initial state: ")
goal = 'Bucharest'

current = (initial, 0) # (current_city, path_cost_till_here)
print(f"The path is: {initial} -> ", end="")

while current[0] != goal:
    f_values = [] # store tuple (f, path_cost, city)
    for city in adj[current[0]]:
        path_cost = current[1] + city[1]
        f = path_cost + h[city[0]]
        f_values.append((f, path_cost, city[0]))
    
    # visit the node with the least f value
    f_values.sort()
    current = (f_values[0][2], f_values[0][1])
    print(f"{current[0]} -> ", end="")

print("X")
print(f"Path cost is {current[1]}")
