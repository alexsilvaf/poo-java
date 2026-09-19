# Expressões aritméticas

<sub>📚 [Documentação](../README.md) › [Seção 3 · Estrutura sequencial](./README.md) › Material 2 de 8</sub>

Uma **expressão** é qualquer trecho de código que, ao ser avaliado, produz um valor. `2 + 3` é uma expressão que resulta em `5`; `preco * 0.9` é uma expressão que resulta em um número.

Toda expressão tem um **valor** e um **tipo**. Os tipos vistos no material [A1 - Variáveis e tipos básicos](./A1%20-%20Variaveis%20e%20tipos%20basicos.md) não valem só para as variáveis: eles valem também para o resultado de cada conta. Em Java, `10 / 3` e `10.0 / 3` são expressões diferentes porque têm tipos diferentes.

## Os cinco operadores aritméticos

| Operador | Nome | Exemplo | Resultado |
|:---:|---|---|---|
| `+` | adição | `7 + 3` | `10` |
| `-` | subtração | `7 - 3` | `4` |
| `*` | multiplicação | `7 * 3` | `21` |
| `/` | divisão | `7 / 3` | `2` |
| `%` | resto da divisão | `7 % 3` | `1` |

Não existe operador de potenciação em Java. Para elevar um número a uma potência usa-se `Math.pow`, que está no material [A7 - Funções matemáticas em Java](./A7%20-%20Funcoes%20matematicas%20em%20Java.md).

## A divisão tem dois comportamentos

Este é o ponto que mais gera erro no início do curso:

```java
System.out.println(10 / 3);      // 3     — divisão inteira
System.out.println(10.0 / 3);    // 3.3333333333333335
System.out.println(10 / 3.0);    // 3.3333333333333335
```

A regra é simples: **se os dois operandos são inteiros, a divisão é inteira** e a parte fracionária é descartada, não arredondada. Basta que **um** dos operandos seja de ponto flutuante para que o resultado seja de ponto flutuante.

```java
int a = 10, b = 3;
System.out.println(a / b);          // 3
System.out.println(a / (double) b); // 3.3333333333333335
System.out.println((double) (a / b)); // 3.0  — tarde demais: a divisão já foi inteira
```

> [!WARNING]
> A última linha é o erro clássico. Converter o **resultado** não recupera o que já foi perdido; é preciso converter antes de dividir.

O `(double)` desses exemplos é um **casting**, a conversão explícita de um tipo em outro. Ele aparece aqui só como ferramenta para forçar a divisão real; as regras completas estão no material [A5 - Processamento de dados e casting](./A5%20-%20Processamento%20de%20dados%20e%20casting.md).

## O operador `%`

O `%` devolve o **resto** da divisão inteira. Ele é usado com muito mais frequência do que parece:

```java
System.out.println(17 % 5);   // 2   — 17 = 5*3 + 2
System.out.println(20 % 5);   // 0   — divisão exata
System.out.println(7 % 2);    // 1   — número ímpar
System.out.println(8 % 2);    // 0   — número par
```

Usos comuns: descobrir se um número é par ou ímpar, separar os dígitos de um número, converter segundos em minutos e segundos, distribuir valores em cédulas.

```java
int totalSegundos = 3725;
int horas   = totalSegundos / 3600;         // 1
int minutos = (totalSegundos % 3600) / 60;  // 2
int segundos = totalSegundos % 60;          // 5
```

O `%` também funciona com `double`, e aí devolve o resto real: `7.5 % 2` é `1.5`.

## Divisão por zero

O comportamento **muda conforme o tipo**, e isso é cobrado na certificação:

```java
System.out.println(10 / 0);       // ArithmeticException: / by zero
System.out.println(10 % 0);       // ArithmeticException: / by zero
System.out.println(10.0 / 0);     // Infinity
System.out.println(-10.0 / 0);    // -Infinity
System.out.println(0.0 / 0);      // NaN  (Not a Number)
```

Divisão inteira por zero **quebra o programa** em tempo de execução. Divisão de ponto flutuante por zero não lança exceção: produz `Infinity`, `-Infinity` ou `NaN`.

## Precedência de operadores

Java segue a precedência da matemática:

1. parênteses `( )`
2. `*`, `/`, `%` — da esquerda para a direita
3. `+`, `-` — da esquerda para a direita

```java
System.out.println(7 + 3 * 2);     // 13  — a multiplicação vem primeiro
System.out.println((7 + 3) * 2);   // 20  — o parêntese muda a ordem
System.out.println(10 - 4 - 3);    // 3   — avalia (10-4) e depois -3
System.out.println(20 / 5 * 2);    // 8   — avalia (20/5) e depois *2, não 20/(5*2)
```

`*`, `/` e `%` têm a **mesma** precedência entre si, e são avaliados da esquerda para a direita. O mesmo vale para `+` e `-`.

> [!TIP]
> Na dúvida, use parênteses. Eles não custam nada em desempenho e evitam que o leitor do código precise lembrar a tabela de precedência.

## Escrevendo fórmulas matemáticas em Java

A notação matemática usa duas dimensões; o código usa uma linha só. Traduzir exige parênteses que a fórmula original não mostra:

| Fórmula | Em Java |
|---|---|
| soma de `a` e `b`, dividida por 2 | `(a + b) / 2.0` |
| base vezes altura, dividido por 2 | `base * altura / 2.0` |
| 1 dividido por (1 mais `x`) | `1.0 / (1 + x)` |
| `a` mais o quociente de `b` por `c` | `a + b / c` |

O erro mais comum é esquecer o parêntese do numerador: `a + b / 2` calcula `a` mais a metade de `b`, e não a média entre os dois.

## Sinal de menos unário

O `-` também aparece como operador **unário**, aplicado a um único valor:

```java
int x = 5;
int y = -x;         // -5
int z = -(-x);      // 5
System.out.println(3 - -2);   // 5  — cuidado com o espaço: 3 - (-2)
```

## Concatenação: o `+` que não soma

Quando um dos operandos do `+` é uma `String`, o `+` deixa de ser adição e passa a ser **concatenação**:

```java
System.out.println(1 + 2 + " reais");     // "3 reais"  — soma primeiro, concatena depois
System.out.println("reais " + 1 + 2);     // "reais 12" — concatena, e o 2 vira texto também
```

A avaliação é da esquerda para a direita. Assim que uma `String` entra na conta, tudo dali em diante vira texto. Esse detalhe aparece com frequência em provas de certificação.

## Referências

- [OCPJ21 Study Guide — Chapter 4: Working with Data](../ocpj21-book/ch04.md), seção *Operators*.

---

<div align="center">

⬅️ [A1 · Variáveis e tipos básicos em Java](./A1%20-%20Variaveis%20e%20tipos%20basicos.md) &nbsp;·&nbsp; 📂 [Seção 3](./README.md) &nbsp;·&nbsp; [A3 · As três operações básicas de programação](./A3%20-%20As%20tres%20operacoes%20basicas.md) ➡️

</div>
