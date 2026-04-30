from _01_HashSet import Solution

def run_tests():
    # Instancia a classe
    solucao = Solution()
    
    print("Iniciando os testes para Contains Duplicate...\n")

    # Teste 1: Contém duplicata (número 1 repete)
    resultado1 = solucao.hasDuplicate([1, 2, 3, 1])
    assert resultado1 == True, f"Erro no Teste 1. Esperado True, mas retornou {resultado1}"
    print("✅ Teste 1 passou! ([1, 2, 3, 1] possui duplicatas)")

    # Teste 2: Não contém duplicata
    resultado2 = solucao.hasDuplicate([1, 2, 3, 4])
    assert resultado2 == False, f"Erro no Teste 2. Esperado False, mas retornou {resultado2}"
    print("✅ Teste 2 passou! ([1, 2, 3, 4] não possui duplicatas)")

    # Teste 3: Múltiplas duplicatas diferentes
    resultado3 = solucao.hasDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    assert resultado3 == True, f"Erro no Teste 3. Esperado True, mas retornou {resultado3}"
    print("✅ Teste 3 passou! (Array grande com várias duplicatas)")

    # Teste 4: Caso limite (Lista com um único elemento não pode ter duplicata)
    resultado4 = solucao.hasDuplicate([5])
    assert resultado4 == False, f"Erro no Teste 4. Esperado False, mas retornou {resultado4}"
    print("✅ Teste 4 passou! (Lista com 1 elemento)")

    # Teste 5: Caso limite (Lista vazia)
    resultado5 = solucao.hasDuplicate([])
    assert resultado5 == False, f"Erro no Teste 5. Esperado False, mas retornou {resultado5}"
    print("✅ Teste 5 passou! (Lista vazia)")

    print("\n🎉 Todos os testes foram concluídos com sucesso!")

# Executa os testes
if __name__ == "__main__":
    run_tests()