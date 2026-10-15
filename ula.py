class ULA:
    def limitar_8bits(self, valor):
        return valor & 0xFF
#garantia do limite de 8 bits
    def ula(self, operacao, a, b):
        if operacao == "ADD":
            resultado = a + b
        elif operacao == "SUB":
          resultado = a - b
        elif operacao == "AND":
          resultado = a & b
        elif operacao == "OR":
         resultado = a | b
        elif operacao == "XOR":
            resultado = a ^ b
        else:
            raise ValueError("Operação da ULA inválida")
        return self.limitar_8bits(resultado)