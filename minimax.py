adj = {
    'A' : ['B', 'C', 'D'],
    'B' : ['E', 'F', 'G'],
    'C' : ['H', 'I', 'J'],
    'D' : ['K', 'L', 'M'], 
}

values = {
    'E' : 3, 'F' : 12, 'G' : 8, 'H' : 2, 'I' : 4, 'J' : 6, 'K' : 14, 'L' : 5, 'M' : 2
}

def minimax(node, isMaxMove):
    if node not in adj:
        return values[node]

    if isMaxMove:
        values[node] = max(minimax(n, False) for n in adj[node])
        return values[node]
    else:
        values[node] = min(minimax(n, True) for n in adj[node])
        return values[node]

print(minimax('A', True))
print(values)
