# Processos de um software
- O compilador é responsavel por transformar o código fonte em código objeto.
- Maquina virtual ou gerador de código é o que permite o código objeto ser executado.

**Código fonte:** é aquele escrito pelo programador em linguagem de programação.

![Exemplo de código-fonte](./codigo-fonte.png)

## Compilação

![Fluxo de compilação: código-fonte, código objeto e código executável](./fluxo-compilacao.svg)

## Interpretação
Temos códigos também que utilizam uma abordagem chamada interpretação. O interpretador lê o código fonte e realiza a análise lexica, sintática e geração de codigo sob demanda, de forma gradual.

![Fluxo de interpretação: código-fonte interpretado e executado sob demanda](./fluxo-interpretacao.svg)

### Exemplos:
- PHP
- JavaScript
- Python
- Ruby

## Abordagem híbrida

Há também a abordagem híbrida, que é quando temos o codigo fonte, o código fonte é precompilado e gera um código objeto chamado de bytecode. Ao invés de passar por um gerador de código e ser gerado um código executavel, ele será executado por uma máquina virtual, que interpretará o bytecode e gera o código sob demanda e executa

![Fluxo da abordagem híbrida: código-fonte, bytecode e execução](./fluxo-hibrido.svg)

### Exemplos:
- Java (JVM)
- C# (Microsoft .NET Framework)


## Vantagens
**Compilação:**
- Velocidade do programa *
- Auxílio do computador antes da execução **

**Interpretação:**
- Flexibilidade de manutenção do aplicativo em produção *
- Expressividade da linguagem
- Código fonte não precisa ser recompilado para rodar em plataformas diferentes **

## Como cada uma das três abordagens funciona:

![Comparação entre as abordagens compilada, interpretada e híbrida](./comparacao-abordagens.svg)
