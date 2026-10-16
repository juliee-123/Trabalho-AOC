# ==========================================
# 1. PROGRAMA PRINCIPAL (TRABALHO ACADÊMICO)
# ==========================================
PROGRAMA_TRABALHO = [
    "LOAD R0, 20",   # 0: Carrega 20 em R0
    "LOAD R1, 10",   # 1: Carrega 10 em R1
    "ADD R0, R1",    # 2: ULA 1 - Soma (R0 = 30)
    "LOAD R2, 5",    # 3: Carrega 5 em R2
    "SUB R0, R2",    # 4: ULA 2 - Subtração (R0 = 25)
    "STORE R0, 14",  # 5: Guarda o resultado 25 na Memória[14]
    "STORE R1, 15",  # 6: Guarda o valor 10 na Memória[15]
    "HALT"           # 7: Encerra a CPU
]
#====================================
# 2.FUNÇÕES DINÂMICAS
#====================================
def gerar_prog_ula(a,b,operacao):
    op_limpa=str(operacao).upper().strip()
    return[
        f'LOAD R0, {a}',
        f'LOAD R1, {b}',
        f'{op_limpa} R0, R1',
        "HALT"
    ]
def gerar_prog_jmp(destino):
    destin=int(destino)
    #GARANTINDO QUE DESTINO CAIBA NA LISTA
    tamanho=max(4, destin+2)
    programa=["HALT"]*tamanho
    programa[0]="LOAD R0,8"
    programa[1]=f'JMP {destin}'
    programa[destin]='LOAD R1, 12'
    return programa
