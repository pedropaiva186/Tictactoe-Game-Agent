class Tictactoe:

    def __init__(self):
        self.table = [[' ' for _ in range(3)] for _ in range(9)]

    def show_table(self):
        for row in self.table:
            for item in row:
                print(f'{item} ')
            print('\n')

    def insert_element(self, symbol : str, pos : int):
        if 0 > pos > 9:
            print("Não é possível inserir o elemento na posição!\n")
            return

        self.table[int(pos / 3)][pos % 3] = symbol