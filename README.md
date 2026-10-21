## Simulador de CPU de 8 Bits

<p align="center">
  <strong>Trabalho de Arquitetura de Computadores</strong><br>
  Universidade Federal do Ceará (UFC) — Campus Sobral
</p>


## Apresentação

O projeto a seguir apresenta o desenvolvimento de um simulador de uma Unidade Central de Processamento (CPU) utilizando a linguagem Python. Temos como objetivo demonstrar, de maneira prática, como funcionam alguns componentes básicos de um processador, como registradores, memória e Unidade Lógica e Aritmética (ULA).

Por meio da execução de instruções, podemos acompanhar o funcionamento da CPU e observar as mudanças que acontecem nos registradores e na memória durante a execução do programa.

## Objetivo geral:

Entender melhor como uma CPU funciona, colocando em prática os conteúdos estudados na disciplina. Para isso, desenvolvemos um simulador que executa instruções, realiza operações matemáticas e lógicas e permite acompanhar os resultados durante a execução.

## Como funciona a CPU

Componentes principais da CPU simulada:

- Registradores: são espaços que guardam valores usados durante as operações. O simulador possui quatro registradores: R0, R1, R2 e R3.
- Memória: possui 16 posições para armazenar instruções e dados.
- PC (Contador de Programa): indica a posição da instrução que será executada.
- ULA: é responsável por realizar as operações matemáticas e lógicas.
- Controle de execução: permite que a CPU execute as instruções e encerre o programa quando necessário.

O simulador trabalha com valores de 8 bits, que podem representar números de 0 a 255 sem sinal.

## Instruções:

| Instrução | O que faz |
|---|---|
| LOAD | Coloca um valor em um registrador. |
| STORE | Guarda na memória o valor de um registrador. |
| ADD | Soma os valores de dois registradores. |
| SUB | Subtrai um valor de outro. |
| AND | Realiza uma operação lógica AND. |
| OR | Realiza uma operação lógica OR. |
| XOR | Realiza uma operação lógica XOR. |
| JMP | Faz a execução continuar em outra posição. |
| HALT | Encerra a execução da CPU. |

## Etapas da execução:

A execução das instruções é dividida em três etapas:

1. Fetch (Busca): a CPU procura a próxima instrução usando o PC.
2. Decode (Decodificação): a CPU identifica qual operação deve ser realizada.
3. Execute (Execução): a instrução é executada, podendo alterar os registradores, a memória ou o PC.

Isso permite que o simulador execute as instruções na ordem correta e mostre as mudanças que acontecem durante o funcionamento da CPU.

## Organização dos arquivos:


- "cpu.py": contém a estrutura da CPU e a execução das instruções.
- "ula.py": contém as operações matemáticas e lógicas.
- "programas.py": contém os programas utilizados na demonstração.
- "testes.py": contém os testes do simulador.
- "main.py": apresenta o menu principal e permite escolher as opções disponíveis.

## Execução do programa:

Para realizar a execução do programa é necessário ter o Python 3 instalado.

Com os arquivos do projeto na mesma pasta, abra o terminal e execute:

python3 main.py

O programa apresenta um menu com opções para executar o programa padrão, testar operações da ULA, testar saltos e sair.

## Programa de exemplo:

O programa padrão possui oito instruções:

LOAD R0, 20
LOAD R1, 10
ADD R0, R1
LOAD R2, 5
SUB R0, R2
STORE R0, 14
STORE R1, 15
HALT

Primeiro, os valores 20 e 10 são colocados nos registradores R0 e R1. Depois, é realizada uma soma, que resulta em 30. Em seguida, o valor 5 é carregado em R2 e subtraído do resultado anterior, deixando 25 em R0.

Por fim, os valores são armazenados nas posições 14 e 15 da memória, e a instrução "HALT" encerra a execução.

## Testes:

O projeto possui um arquivo chamado "testes.py", utilizado para verificar as operações da ULA e algumas funções da CPU.

Para executar os testes, utilize o comando:

python3 testes.py

Após executar o comando, é possível conferir no terminal os resultados apresentados pelos testes.

## Conclusão:

Com esse projeto, podemos entender melhor como uma CPU executa instruções e como seus componentes trabalham juntos. A atividade também permitiu colocar em prática os conteúdos estudados em Arquitetura de Computadores, utilizando Python para simular o funcionamento básico de um processador.

## Repositório:

O código-fonte do projeto está disponível no GitHub:

"Trabalho-AOC" (https://github.com/juliee-123/Trabalho-AOC)

Integrantes

- Nome: Ana Júlia Vasconcelos Cruz
- Nome: Ângela Carla Vanconcelos Silva 
