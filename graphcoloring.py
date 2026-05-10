G = [
[0,1,1,0,1,0],
[1,0,1,1,0,1],
[1,1,0,1,1,0],
[0,1,1,0,0,1],
[1,0,1,0,0,1],
[0,1,0,1,1,0]
]

node = "abcdef"

colors = ["Blue", "Red", "Yellow", "Green"]

solution = {}

for i in range(len(G)):

    used = []

    for j in range(len(G)):
        if G[i][j] == 1 and node[j] in solution:
            used.append(solution[node[j]])

    for color in colors:
        if color not in used:
            solution[node[i]] = color
            break

for n in solution:
    print("Node", n, "=", solution[n])