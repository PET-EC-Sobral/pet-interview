from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lista = []
        quadro = [[] for _ in range(9)]

        for j in range(0, 9):
            for i in range(0, 9):
                lista.append(board[i][j])
                quadro[(i//3)*3+(j//3)].append(board[i][j])
            if self.hasDuplicate(lista):
                return False
            lista = []

        for i in range(0, 9):
            if self.hasDuplicate(board[i]) or self.hasDuplicate(quadro[i]):
                return False

        return True
    
    def hasDuplicate(self, lista: List[str]) -> bool:
        seen = set()
        for num in lista:
            if num != ".":
                if num in seen:
                    return True
                seen.add(num)
        return False