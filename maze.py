def dfs_to_maze(maze : list) -> tuple:
    # Primeiramente, o DFS
    stack = list()
    elements_visited = set()

    inicial_point = find_inicial_point(maze)
    final_point = tuple()

    stack.append((inicial_point, 0)) # Adicionando a posição inicial
    elements_visited.add(inicial_point) # Adicionando a posição inicial como visitada

    pos_x = [-1, 0, 0, 1]
    pos_y = [0, -1, 1, 0]

    while stack: # Enquanto a pilha de elementos não estiver vazia
        point_expected = stack.pop() # Removendo e recolhendo o último elemento, que é possível de ser nosso elemento

        if(maze[point_expected[0][0]][point_expected[0][1]] == 'B'): # Caso tenha encontrado a posição final
            final_point = point_expected
            break

        # Agora vamos verificar os possíveis elementos envolta da posição que estamos
        for i in range(4):
            new_point = ((point_expected[0][0] + pos_x[i], point_expected[0][1] + pos_y[i]), point_expected[1] + 1)
            if isValid(new_point[0][0], new_point[0][1], maze) and maze[new_point[0][0]][new_point[0][1]] != '#' and new_point[0] not in elements_visited:
                stack.append(new_point)
                elements_visited.add(new_point[0])

    return (final_point)

def bfs_to_maze(maze : list) -> tuple:
    # Agora o BFS
    queue = list()
    elements_visited = set()

    inicial_point = find_inicial_point(maze)
    final_point = tuple()

    queue.append((inicial_point, 0)) # Adicionando a posição inicial
    elements_visited.add(inicial_point) # Adicionando a posição inicial como visitada

    pos_x = [-1, 0, 0, 1]
    pos_y = [0, -1, 1, 0]

    while queue: # Enquanto a pilha de elementos não estiver vazia
        point_expected = queue.pop() # Removendo e recolhendo o primeiro elemento, que é possível de ser nosso elemento

        if(maze[point_expected[0][0]][point_expected[0][1]] == 'B'): # Caso tenha encontrado a posição final
            final_point = point_expected
            break

        # Agora vamos verificar os possíveis elementos envolta da posição que estamos
        for i in range(4):
            new_point = ((point_expected[0][0] + pos_x[i], point_expected[0][1] + pos_y[i]), point_expected[1] + 1)
            if isValid(new_point[0][0], new_point[0][1], maze) and maze[new_point[0][0]][new_point[0][1]] != '#' and new_point[0] not in elements_visited:
                queue.insert(0, new_point)
                elements_visited.add(new_point[0])

    return (final_point)

def find_inicial_point(maze : list) -> tuple:
    inicial_x = -1
    inicial_y = -1

    for x, row in enumerate(maze):
        for y, item in enumerate(row):
            if item == 'A':
                inicial_x = x
                inicial_y = y
                break

    return (inicial_x, inicial_y)

def isValid(a : int, b : int, maze : list) -> bool:
    return 0 <= a < len(maze) and 0 <= b < len(maze[0])

# Este será o labirinto no qual vamos aplicar o DFS e BFS

# Cada vírgula representa o "pulo" de uma coluna
maze = [
    "#######",
    "#A   B#",
    "# ### #",
    "#     #",
    "#######"
]

maze1 = [
    "#####",
    "#A  #",
    "# #B#",
    "#   #",
    "#####"
]

maze2 = [
    "##########",
    "#A     #B#",
    "# ### ####",
    "#   #    #",
    "##########"
]

maze3 = [
    "############",
    "#A     #   #",
    "# ### ### ##",
    "#   #     B#",
    "############"
]

maze4 = [
    "###############",
    "#A #   #  #   #",
    "# ## ## # # # #",
    "# #  ##  ## ###",
    "#   #        ##",
    "### # # # # ###",
    "# #    # #   ##",
    "#  ## ## ###  #",
    "#            B#",
    "###############"
]


# A => Ponto inicial
# B => Ponto final

# Objetivo: Encontrar o número de casas necessárias para encontrar o objetivo

answer = dfs_to_maze(maze1)

if(answer == ()):
    print("Não foi possível encontrar o ponto final")
else:
    print(f"Número de movimentos: {answer[1]}\nPosição final: ({answer[0][0]}, {answer[0][1]})")

answer = bfs_to_maze(maze1)

if(answer == ()):
    print("Não foi possível encontrar o ponto final")
else:
    print(f"Número de movimentos: {answer[1]}\nPosição final: ({answer[0][0]}, {answer[0][1]})")