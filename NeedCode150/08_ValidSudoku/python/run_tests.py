# Substitua pela sua solução
from _01_ import Solution

def run_tests():
    solucao = Solution()
    
    print("Iniciando os testes para Valid Sudoku...\n")

    # Teste 1: Tabuleiro válido padrão
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    resultado1 = solucao.isValidSudoku(board1)
    assert resultado1 == True, "Erro no Teste 1. O tabuleiro é válido, deveria retornar True."
    print("✅ Teste 1 passou! (Tabuleiro válido)")

    # Teste 2: Tabuleiro inválido (O número '8' repete na primeira coluna e no primeiro quadrante)
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    resultado2 = solucao.isValidSudoku(board2)
    assert resultado2 == False, "Erro no Teste 2. O tabuleiro é inválido, deveria retornar False."
    print("✅ Teste 2 passou! (Tabuleiro com repetição na coluna/quadrante)")

    # Teste 3: Tabuleiro completamente vazio (É tecnicamente válido)
    board3 = [
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]
    ]
    resultado3 = solucao.isValidSudoku(board3)
    assert resultado3 == True, "Erro no Teste 3. Tabuleiro vazio deveria retornar True."
    print("✅ Teste 3 passou! (Tabuleiro totalmente vazio)")

    print("\n🎉 Todos os testes foram concluídos com sucesso!")

# Executa os testes
if __name__ == "__main__":
    run_tests()