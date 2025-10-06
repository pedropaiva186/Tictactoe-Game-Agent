from Tictactoe import Tictactoe
import copy
import math
import random

class Machine:
    def __init__(self):
        pass
    
    def jogar(self, tabuleiro : Tictactoe, symbol : str) -> int:
        possibles_moves = tabuleiro.get_blank_spaces()
        
        best_score = math.inf
        best_moves = []
        
        for move in possibles_moves:
            temp_tab = copy.deepcopy(tabuleiro)
            temp_tab.insert_element(move)
            
            value = self._choose_best_move(temp_tab, symbol)
            
            # Trocando o sinal do elemento caso queira maximizar para sempre minimizar
            if symbol == tabuleiro.symbols[0]:
                value *= -1
            
            if value < best_score:
                best_score = value
                best_moves = [move]
            elif value == best_score:
                best_moves.append(move)
                
        return random.choice(best_moves) if best_moves else None
                
    
    def _choose_best_move(self, tabuleiro : Tictactoe, symbol : str) -> int:
        possibles_moves = tabuleiro.get_blank_spaces()
        minimax_value = 0
        
        # Setando o valor a depender se queremos maximizar ou minimizar a jogada
        if tabuleiro.symbols[0] == symbol:
            minimax_value = -math.inf
        else:
            minimax_value = math.inf

        
        for move in possibles_moves:
            temp_tab = copy.deepcopy(tabuleiro)
            temp_tab.insert_element(move)
            
            if temp_tab.verify_victory() != 2: # Alguém ganhou o jogo
                return temp_tab.verify_victory()
                
            if symbol == tabuleiro.symbols[0]:
                minimax_value = max(minimax_value, self._choose_best_move(temp_tab, tabuleiro.symbols[1] if tabuleiro.symbols[0] == symbol else tabuleiro.symbols[0]))
            else:
                minimax_value = min(minimax_value, self._choose_best_move(temp_tab, tabuleiro.symbols[1] if tabuleiro.symbols[0] == symbol else tabuleiro.symbols[0]))
            
        return minimax_value