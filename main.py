from cpu import CPU
import programas
#EXECUÇÃO DAS INSTRUÇÕES DO MAIN
def exe_instrucoes(instrucoes, nome_programa):
    #CRIAMOS A CPU E CARREGAMOS O PROGRAMA
    print(f"\n{'='*50}")
    print(f"{nome_programa}")
    print(f"\n{'='*50}")
    cpu=CPU()

    for i, inst in enumerate(instrucoes):
        cpu.memoria[i]=inst
    cpu.executar()
    print(f"\n{'='*50}")
    print(" FIM DA EXECUÇÃO")
    print(f"{'='*50}\n")
#TRADUZIR A INSTRUÇÃO EM ASSEMBLY
def selec_op(opcao):
    key=str(opcao).upper().strip()
    operacoes={
        "1":"ADD", "ADD":"ADD",
        "2":"SUB","SUB":"SUB",
        "3":"AND", "AND":"AND",
        "4": "XOR", "XOR":"XOR",
        "5":"OR", "OR":"OR" }
    return operacoes.get(key, "1")

def main():
    while True:
        print("====================================")
        print("       SIMULADOR CPU 8 BITS")
        print("====================================")
        print("               MENU:")
        print("1. Programa Padrão (8 instruções, demonstração básica)")
        print("2. Criar operação personalisada na ULA")
        print("3. Testar saltos (JUMP) da cpu")
        print("0. Sair")
        print("===================================")
        escolha = input("Ecolha uma opção: ")
        if escolha =="1":
            exe_instrucoes(
                programas.PROGRAMA_TRABALHO,
                "Programa Padrão (8 instruções)"
            )
        elif escolha=="2":
            try:
                a=int(input("Digite o primeiro número: "))
                b=int(input("Digite o segundo número: "))
                print("Digite a operação que deseja testar:  [1]ADD, [2]SUB, [3]AND, [4]XOR, [5]OR")
                op=input("Sua escolha: ")
                instrucoes=programas.gerar_prog_ula(a, b, op)
                exe_instrucoes(instrucoes, f"Operação personalizada: {a} {op} {b}")
            except ValueError:
                print("\n ERRO! Por favor digite valores válidos")
        elif escolha=="3":
            try:
                jmp=input("Por favor, digite a posição para onde o jump deve pular: ")
                instrucoes=programas.gerar_prog_jmp(jmp)
                exe_instrucoes(instrucoes,f'Teste salto na memória {jmp}')
            except:
                print("\nErro! Por favor digite um número inteiro")
        elif escolha=="0":
            print("\nEncerrando simulador...")
            break
        else:
            print("\nOperação inválida! Digite 0, 1 , 2 ou 3")
if __name__=="__main__":
    main()