# Substitua pelo nome da solução que quer testar

from _01ForcaBruta import Solution

# 2. A função de testes
def run_tests():
    # Instanciamos a classe para poder usar os métodos dela
    solucao = Solution()
    
    print("Iniciando os testes...\n")

    # Teste 1: Caso padrão
    resultado1 = solucao.twoSum([2, 7, 11, 15], 9)
    assert resultado1 == [0, 1], f"Erro no Teste 1. Esperado [0, 1], mas retornou {resultado1}"
    print("✅ Teste 1 passou! (target 9 em [2, 7, 11, 15])")

    # Teste 2: Elementos fora de ordem
    resultado2 = solucao.twoSum([3, 2, 4], 6)
    assert resultado2 == [1, 2], f"Erro no Teste 2. Esperado [1, 2], mas retornou {resultado2}"
    print("✅ Teste 2 passou! (target 6 em [3, 2, 4])")

    # Teste 3: Elementos iguais
    resultado3 = solucao.twoSum([3, 3], 6)
    assert resultado3 == [0, 1], f"Erro no Teste 3. Esperado [0, 1], mas retornou {resultado3}"
    print("✅ Teste 3 passou! (target 6 em [3, 3])")

    # Teste 4: Sem solução possível
    resultado4 = solucao.twoSum([1, 2], 5)
    assert resultado4 == [], f"Erro no Teste 4. Esperado [], mas retornou {resultado4}"
    print("✅ Teste 4 passou! (Nenhuma soma atinge o target)")

    print("\n🎉 Todos os testes foram concluídos com sucesso!")

# 3. Executando os testes
if __name__ == "__main__":
    run_tests()