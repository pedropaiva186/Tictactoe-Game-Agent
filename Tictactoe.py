import time

class Tictactoe:

    def __init__(self, symbol1 : str, symbol2 : str):
        self.table = [[' ' for _ in range(3)] for _ in range(3)]
        self.symbols = [symbol1, symbol2]
        self.moves = 0

    def interface(self):
        from Machine import Machine
        
        option = 0
        
        while 1 > option or option > 3:
            print("Opções:\n[1] 2 Jogadores\n[2] Jogar contra a máquina\n[3] As máquinas jogam")
            option = int(input("Digite a opção desejada: "))
            
        count = 0
        pos = 0
        
        machine = Machine()
        
        while self.verify_victory() == 2:
            self.show_table()
            symbol = self.symbols[count % 2]
            
            if (option == 2 and count % 2 == 1) or option == 3:
                    pos = machine.jogar(self, symbol)
                    self.insert_element(pos)
            else:
                while True:
                        pos = int(input("Digite a posição de jogada: "))

                        if self.insert_element(pos):
                            break
                        
                        print("Falha ao inserir o elemento, tente novamente!")
                        
            if option == 3:
                time.sleep(1)
            
            count += 1
        
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

    def insert_element(self, pos : int) -> bool:
        if 0 > pos or pos > 8 or self.table[int(pos / 3)][pos % 3] != ' ':
            return False

        self.table[int(pos / 3)][pos % 3] = self.symbols[self.moves % 2]
        self.moves += 1

        return True
    
    def get_quantity_blank_spaces(self) -> int:
        return 9 - self.moves
    
    def get_blank_spaces(self) -> list:
        spaces = list()
        
        for i, row in enumerate(self.table):
            for j, space in enumerate(row):
                if space == ' ':
                    spaces.append(i * 3 + j)
                    
        return spaces
    
    def verify_victory(self) -> int:
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
            
        if self.moves == 9:
            return 0
        
        return 2