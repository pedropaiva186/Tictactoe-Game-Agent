from Tictactoe import Tictactoe
import copy
import math

class Machine:
    def __init__(self):
        pass
    
    def jogar(self, tabuleiro : Tictactoe, symbol : str) -> int:
        possibles_moves = tabuleiro.get_blank_spaces()
        
        moves = [0] * len(possibles_moves)
        
        for i, move in enumerate(possibles_moves):
            temp_tab = copy.deepcopy(tabuleiro)
            temp_tab.insert_element(move)
            
            moves[i] = self._choose_best_move(temp_tab, symbol)
            
        if symbol == tabuleiro.symbols[0]:
            return possibles_moves[moves.index(max(moves))] 
        else:
            return possibles_moves[moves.index(min(moves))] 
    
    def _choose_best_move(self, tabuleiro : Tictactoe, symbol : str) -> int:
        quant = 0
        i = 1
        possibles_moves = tabuleiro.get_blank_spaces()
        
        for move in possibles_moves:
            temp_tab = copy.deepcopy(tabuleiro)
            temp_tab.insert_element(move)
            
            if temp_tab.verify_victory() != 2:
                if (symbol == tabuleiro.symbols[0] and temp_tab.verify_victory == -1) or (symbol == tabuleiro.symbols[1] and temp_tab.verify_victory == 1):
                    i = 2
                else:
                    i = 1
                
                quant += temp_tab.verify_victory() * math.factorial(len(possibles_moves)) * i
            else:
                quant += self._choose_best_move(temp_tab, symbol)
                
        return quant