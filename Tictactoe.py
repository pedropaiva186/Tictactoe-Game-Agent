class Tictactoe:

    def __init__(self, symbol1 : str, symbol2 : str):
        self.table = [[' ' for _ in range(3)] for _ in range(3)]
        self.symbols = [symbol1, symbol2]

    def interface(self):
        symbol = self.symbols[1]

        while self.verify_victory() == 2:
            self.show_table()

            symbol = (self.symbols[1] if symbol == self.symbols[0] else self.symbols[0])

            while True:
                pos = int(input("Digite a posição de jogada: "))

                if self.insert_element(symbol, pos):
                    break
                
                print("Falha ao inserir o elemento, tente novamente!")
        
        self.show_table()

        if self.verify_victory() == 1:
            print(f"O jogador com símbolo {self.symbols[0]} ganhou!")
        elif self.verify_victory() == -1:
            print(f"O jogador com símbolo {self.symbols[1]} ganhou!")
        else:
            print(f"O jogo empatou!")

    def show_table(self):
        for row in self.table:
            print("|", end=' ')
            for item in row:
                print(f'{item} |', end=' ')
            print('\n')

    def insert_element(self, symbol : str, pos : int) -> bool:
        if symbol not in self.symbols:
            print("O símbolo não faz parte do conjunto previsto")
            return False

        if 0 > pos or pos > 8 or self.table[int(pos / 3)][pos % 3] != ' ':
            print("Não é possível inserir o elemento na posição!\n")
            return False

        self.table[int(pos / 3)][pos % 3] = symbol
        return True
    
    def verify_is_completed(self) -> bool:
        isCompleted = True
        for row in self.table:
            if ' ' in set(row):
                isCompleted = False
                break

        return isCompleted
    
    def verify_victory(self) -> int:
        if self.verify_is_completed():
            return 0
        
        for row in self.table:
            if len(set(row)) == 1 and ' ' not in row:
                if row[0] == self.symbols[0]:
                    return 1
                else:
                    return -1
            
        transpose_table = [list(row) for row in zip(*self.table)]

        for row in transpose_table:
            if len(set(row)) == 1 and ' ' not in row:
                if row[0] == self.symbols[0]:
                    return 1
                else:
                    return -1
        
        aux = set()
        for i in range(3):
            aux.add(self.table[i][i])

        if len(aux) == 1 and ' ' not in aux:
            if aux.pop() == self.symbols[0]:
                return 1
            else:
                return -1
        
        aux.clear()
        for i in range(3):
            aux.add(self.table[i][2-i])

        if len(aux) == 1 and ' ' not in aux:
            if aux.pop() == self.symbols[0]:
                return 1
            else:
                return -1
        
        return 2