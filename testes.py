from ula import ULA
from cpu import CPU

def testes_ula():
    u=ULA()
    print("==INICIANDO TESTES ULA==")
    #ADD
    res_add=u.ula("ADD",5, 8)
    assert res_add==13,f"Erro na adição, resultado esperado: 13, resultado obtido {res_add}"
    print("ADD [ok]: 5+8=13")
    #SUB
    res_sub=u.ula("SUB", 9, 2)
    assert res_sub==7, f"Erro na subtração,resultado esperado: 7, resultado obtido {res_sub}"
    print("SUB [ok]: 9-2=7")
    #Operações lógicas
     #AND
    res_and=u.ula("AND", 12, 10)
    #1100 (12) AND 1010 (10) -> 1000 (8)
    assert res_and==8, f"Erro na AND,resultado esperado: 8, resultado obtido {res_and}"
    print("AND [ok]: 12 && 10 = 8 ")
    #OR
    res_or=u.ula("OR", 12, 10)
    #1100 (12) OR 1010 (10) -> 1110 (14)
    assert res_or==14, f"Erro na OR,resultado esperado: 14, resultado obtido {res_or}"
    print("OR [ok]: 12 | 10 = 14")
    #XOR
    res_xor=u.ula("XOR", 12,10)
    #1100 (12) XOR 1010 (10) -> 0110(6)
    assert res_xor==6,f"Erro na XOR,resultado esperado: 6, resultado obtido {res_xor}"
    print("XOR [ok]: 12 ^ 10 = 6")

    #Overflow
    res_overflow=u.ula("ADD", 200,100)
    assert res_overflow==44,f"Erro no limite de bits,resultado esperado: 44, resultado obtido {res_overflow}"
    print("[OK] Limite 8 bits (Overflow): 200 + 100 = 44")

    print("\n=== TODOS OS TESTES DA ULA PASSARAM COM SUCESSO! ===")
    
def testes_cpu():
     cpu=CPU()
     print("==INICIANDO TESTES CPU==")
     #VERIFICANDO CARREGAMENTO DE REGISTRADORES
     cpu.executar_instrucao("LOAD R0, 12")
     assert cpu.registradores["R0"]==12, f"Erro de execução: resultado esperado: 12, resultado obtido:{cpu.registradores['R0']}"
     print("LOAD [OK]: R0=12")
     #VERIFICANDO GUARDAR NA MEMÓRIA
     cpu.registradores["R1"]=20
     cpu.executar_instrucao("STORE R1, 12")
     assert cpu.memoria[12]==20, f'Erro de execução: resultado esperado: 20, resultado obtido:{cpu.memoria[12]}'
     print("STORE [OK]: 20 GUARDADO EM MEMÓRIA[12]")
     #VERIFICANDO PC
     pc_ini=cpu.pc
     cpu.executar_instrucao("LOAD R0, 12")
     assert cpu.pc==pc_ini+1, f'Erro de execução, o pc não está incrementando corretamente, esperado:{pc_ini+1}, obtido:{cpu.pc}'
     print("INCREMENTO DAS INSTRUÇÕES [OK]")
     #VERIFICANDO SALTOS NAS INSTRUÇÕES
     cpu.executar_instrucao("JMP 12")
     assert cpu.pc==12, f'Erro de execução, o pc não está pulando instruções, esperado:cpu.pc=12, obtido:cpu.pc={cpu.pc}'
     #VERIFICANDO PARAFA
     cpu.executar_instrucao("HALT")
     assert cpu.halted==True, f'Erro, a cpu não está parando corretanente! HALT==False'
     print("HALT [OK], A CPU PARA CORRETAMENTE")
    #EXEMPLO DADO
     cpu_prog=CPU()
     cpu_prog.memoria[0] = "LOAD R0, 5"
     cpu_prog.memoria[1] = "LOAD R1, 8"
     cpu_prog.memoria[2] = "ADD R0, R1"

     cpu_prog.memoria[3] = "STORE R0, 15"
     cpu_prog.memoria[4] = "HALT"
     cpu_prog.executar()
     assert cpu_prog.memoria[15] == 13, f"Erro no programa exemplo, esperado 13, obtido {cpu_prog.memoria[15]}"
     print("Programa Exemplo [OK]: Executado do início ao fim com resultado 13 na Memória[15]")
if __name__=="__main__":
    testes_ula() 
    testes_cpu()
    print("==TODOS OS TESTES PASSARAM, CPU E ULA FUNCIONANDO PERFEITAMENTE==")
