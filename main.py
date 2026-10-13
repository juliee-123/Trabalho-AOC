from cpu import CPU
cpu = CPU()
# Programa de teste
cpu.memoria[0] = "LOAD R0, 5"
cpu.memoria[1] = "LOAD R1, 8"
cpu.memoria[2] = "ADD R0, R1"

cpu.memoria[3] = "STORE R0, 15"
cpu.memoria[4] = "HALT"

print("================================")
print(" CPU SIMULADA - 8 BITS")
print("================================")

cpu.executar()

print()
print("Memória[15]:", cpu.memoria[15])