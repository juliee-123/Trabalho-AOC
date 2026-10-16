from ula import ULA
class CPU:
    def __init__(self):
# Registradores gerais
        self.registradores = {
        "R0": 0,

        "R1": 0,
        "R2": 0,
        "R3": 0
        }
# Memória com 16 posições
        self.memoria = [0] * 16
# Program Counter
        self.pc = 0
# Estado da CPU
        self.halted = False
        self.ula=ULA()
# --------------------------------------------------
# Garante valores de 8 bits
# --------------------------------------------------
    def limitar_8bits(self, valor):
        return valor & 0xFF
# --------------------------------------------------
# EXECUÇÃO DE UMA INSTRUÇÃO
# --------------------------------------------------
    def executar_instrucao(self, instrucao):
# Permite instruções como:
# LOAD R0, 5
        partes = instrucao.replace(",", "").split()
        operacao = partes[0]
# ------------------------------------------------
# LOAD
# ------------------------------------------------
# LOAD R0, 5
# (Coloca o valor 5 no registrador R0.)
# ------------------------------------------------
        if operacao == "LOAD":
            registrador = partes[1]
            valor = int(partes[2])
            self.registradores[registrador] = self.limitar_8bits(valor)
            self.pc += 1
# ------------------------------------------------
# STORE
# ------------------------------------------------
# STORE R0, 15
#(Pega o valor contido no registrador e guarda no endereço especificado)
# ------------------------------------------------
        elif operacao == "STORE":
            registrador=partes[1]
            endereco=int(partes[2])
            self.memoria[endereco] = self.registradores[registrador]
            self.pc += 1
# ------------------------------------------------
# ADD
# ------------------------------------------------
# ADD R0, R1
# R0 = R0 + R1
# ------------------------------------------------
        elif operacao == "ADD":
            reg1=partes[1]
            reg2=partes[2]

            val_a=self.registradores[reg1]
            val_b=self.registradores[reg2]
            resultado = self.ula.ula("ADD", val_a, val_b)
            self.registradores[reg1]=resultado
            self.pc+=1
# ------------------------------------------------
# SUB
# ------------------------------------------------
        elif operacao == "SUB":
            reg1=partes[1]
            reg2=partes[2]

            val_a=self.registradores[reg1]
            val_b=self.registradores[reg2]
            resultado=self.ula.ula("SUB", val_a,val_b)
            self.registradores[reg1]=resultado
            self.pc+=1
# ------------------------------------------------
# AND
# ------------------------------------------------
        elif operacao == "AND":
            reg1=partes[1]
            reg2=partes[2]
            
            val_a=self.registradores[reg1]
            val_b=self.registradores[reg2]
            resultado=self.ula.ula("AND", val_a,val_b)
            self.registradores[reg1]=resultado
            self.pc+=1
# ------------------------------------------------
# OR
# ------------------------------------------------
        elif operacao == "OR":
            reg1=partes[1]
            reg2=partes[2]
            
            val_a=self.registradores[reg1]
            val_b=self.registradores[reg2]
            resultado=self.ula.ula("OR", val_a,val_b)
            self.registradores[reg1]=resultado
            self.pc+=1
# ------------------------------------------------
# XOR
# ------------------------------------------------
        elif operacao == "XOR":
            reg1=partes[1]
            reg2=partes[2]
            
            val_a=self.registradores[reg1]
            val_b=self.registradores[reg2]
            resultado=self.ula.ula("XOR", val_a,val_b)
            self.registradores[reg1]=resultado
            self.pc+=1

# ------------------------------------------------
# JMP
# ------------------------------------------------
# JMP 8
#
# O PC passa a apontar para a posição 8.
# ------------------------------------------------
        elif operacao == "JMP":
            endereco = int(partes[1])
            self.pc = endereco
# ------------------------------------------------
# HALT
# ------------------------------------------------
        elif operacao == "HALT":
            self.halted=True
        else:
         raise ValueError(
         f"Instrução desconhecida: {operacao}"
         )
# --------------------------------------------------
# CICLO DA CPU

# --------------------------------------------------
    def ciclo(self):
# FETCH
        instrucao = self.memoria[self.pc]
        #TRAVA DE SEGURANÇA
        if not instrucao:
            self.halted:True
            return
        print()
        print("-----------------------------")
        print("PC:", self.pc)
        print("Instrução:", instrucao)
        print("Executando...")
# DECODE + EXECUTE
        self.executar_instrucao(instrucao)
# Mostrar registradores
        self.mostrar_estado()
# --------------------------------------------------
# EXECUÇÃO COMPLETA
# --------------------------------------------------
    def executar(self):
        while not self.halted:
            self.ciclo()
            print("A CPU PAROU COM AS INSTRUÇÔES")
# --------------------------------------------------
# MOSTRAR ESTADO
# --------------------------------------------------
    def mostrar_estado(self):
        print("Registradores:")
        for nome, valor in self.registradores.items():
            print(
            f"{nome} = {valor:02X} "
            f"({valor})"
            )