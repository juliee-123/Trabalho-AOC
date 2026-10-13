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
# --------------------------------------------------
# Garante valores de 8 bits
# --------------------------------------------------
def limitar_8bits(self, valor):
return valor & 0xFF