# Expressão condicional ternária

<sub>📚 [Documentação](../README.md) › [Seção 4 · Estrutura condicional](./README.md) › Material 6 de 8</sub>

O operador condicional ternário escolhe **um entre dois valores** a partir de uma condição. Ele é chamado ternário porque possui três partes.

```java
condicao ? valorSeVerdadeiro : valorSeFalso
```

Exemplo:

```java
double nota = 7.5;
String resultado = nota >= 6.0 ? "Aprovado" : "Reprovado";

System.out.println(resultado);
```

Leia da esquerda para a direita:

1. `nota >= 6.0` é a condição;
2. se for `true`, a expressão produz `"Aprovado"`;
3. se for `false`, produz `"Reprovado"`;
4. o valor escolhido é atribuído a `resultado`.

## Equivalência com `if-else`

Este código:

```java
double preco = 100.0;
boolean temDesconto = true;
double valorFinal;

if (temDesconto) {
    valorFinal = preco * 0.90;
} else {
    valorFinal = preco;
}
```

pode ser escrito assim:

```java
double preco = 100.0;
boolean temDesconto = true;
double valorFinal = temDesconto ? preco * 0.90 : preco;
```

As duas versões produzem o mesmo valor. A forma ternária é conveniente porque toda a decisão é uma expressão que pode participar de uma atribuição.

## O resultado tem um tipo

Como qualquer expressão, o ternário produz um valor e esse valor possui um tipo:

```java
int idade = 20;
String categoria = idade >= 18 ? "adulto" : "menor";
```

Os dois resultados precisam ser compatíveis com o local onde o valor será usado:

```java
double valor = true ? 10 : 2.5; // 10 é promovido; o resultado é double
// int erro = true ? 10 : 2.5;  // erro: o resultado pode ser double
```

Nesta etapa, escolha resultados do mesmo tipo sempre que possível. Isso evita que as regras de conversão escondam a intenção.

## Apenas um lado é avaliado

Depois da condição, Java avalia somente o resultado escolhido:

```java
int divisor = 0;
int resultado = divisor != 0 ? 10 / divisor : 0;

System.out.println(resultado); // 0
```

Como a condição é `false`, a divisão não é executada.

## Uso direto na saída

```java
int numero = 7;
System.out.println(numero % 2 == 0 ? "Par" : "Impar");
```

Isso é adequado quando os dois valores são curtos e a condição é fácil de ler.

## Quando usar

Use o ternário quando:

- existe uma única condição;
- o objetivo é escolher entre dois valores;
- a expressão continua curta e clara.

Prefira `if-else` quando:

- cada caminho executa várias instruções;
- existem três ou mais alternativas;
- a condição ou os resultados já são longos;
- é necessário explicar cada caminho com clareza.

O ternário não substitui toda estrutura condicional. Ele substitui bem um `if-else` simples que apenas escolhe um valor.

## Evite ternários aninhados no início

Este código compila:

```java
double nota = 8.0;
String conceito = nota >= 9.0 ? "A" : nota >= 7.0 ? "B" : "C";
```

Mas exige esforço para descobrir qual `:` pertence a qual condição. A versão gradual é mais clara:

```java
String conceito;

if (nota >= 9.0) {
    conceito = "A";
} else if (nota >= 7.0) {
    conceito = "B";
} else {
    conceito = "C";
}
```

Uma escrita menor não é automaticamente uma escrita melhor.

## Teste de mesa

```java
int quantidade = 8;
double precoUnitario = quantidade >= 10 ? 4.50 : 5.00;
double total = quantidade * precoUnitario;
```

| Etapa | Resultado |
| --- | --- |
| `quantidade >= 10` | `false` |
| valor escolhido | `5.00` |
| `precoUnitario` | `5.00` |
| `total` | `40.00` |

Se `quantidade` fosse `10`, a condição seria `true`, o preço unitário seria `4.50` e o total seria `45.00`.

## Referências

- [OCPJ21 Study Guide - Chapter 4: Working with Data](../ocpj21-book/ch04.md), seção *Operators*.
- [Java Language Specification 25 - Conditional Operator](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.25).

---

<div align="center">

⬅️ [A5 · Estrutura switch-case](./A5%20-%20Estrutura%20switch-case.md) &nbsp;·&nbsp; 📂 [Seção 4](./README.md) &nbsp;·&nbsp; [A7 · Escopo e inicialização](./A7%20-%20Escopo%20e%20inicializacao.md) ➡️

</div>
