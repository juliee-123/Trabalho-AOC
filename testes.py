from ula import ula

def testes_ula():
    print("==TESTES ULA==")
    #ADD
    res_add=ula("ADD", 5, 8)
    assert res_add==13,f"Erro na adição, resultado esperado: 13, resultado obtido {res_add}"
    print("ADD [ok]: 5+8=13")
    #SUB
    res_sub=ula("SUB", 9, 2)
    assert res_sub==7, f"Erro na subtração,resultado esperado: 7, resultado obtido {res_sub}"
    print("SUB [ok]: 9-2=7")
    #Operações lógicas
     #AND
    res_and=ula("AND", 12, 10)
    #1100 (12) AND 1010 (10) -> 1000 (8)
    assert res_and==8, f"Erro na AND,resultado esperado: 8, resultado obtido {res_and}"
    print("AND [ok]: 12 && 10 = 8 ")
    #OR
    res_or=ula("OR", 12, 10)
    #1100 (12) OR 1010 (10) -> 1110 (14)
    assert res_or==14, f"Erro na OR,resultado esperado: 14, resultado obtido {res_or}"
    print("OR [ok]: 12 | 10 = 14")
    #XOR
    res_xor=ula("XOR", 12,10)
    #1100 (12) XOR 1010 (10) -> 0110(6)
    assert res_xor==6,f"Erro na XOR,resultado esperado: 6, resultado obtido {res_xor}"
    print("XOR [ok]: 12 ^ 10 = 6")

    #Overflow
    res_overflow=ula("ADD", 200,100)
    assert res_overflow==44,f"Erro no limite de bits,resultado esperado: 44, resultado obtido {res_overflow}"
    print("[OK] Limite 8 bits (Overflow): 200 + 100 = 44")

    print("\n=== TODOS OS TESTES PASSARAM COM SUCESSO! ===")
    
if __name__=="__main__":
     testes_ula()

