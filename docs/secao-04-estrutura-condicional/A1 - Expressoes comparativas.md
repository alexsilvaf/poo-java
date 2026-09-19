# Expressões comparativas

<sub>📚 [Documentação](../README.md) › [Seção 4 · Estrutura condicional](./README.md) › Material 1 de 8</sub>

Uma expressão comparativa coloca dois valores lado a lado e responde a uma pergunta com apenas dois resultados possíveis: `true` ou `false`. Esse resultado tem o tipo primitivo `boolean`, apresentado na Seção 3.

```java
int idade = 20;
boolean maiorDeIdade = idade >= 18;

System.out.println(maiorDeIdade); // true
```

Até aqui, as expressões aritméticas produziam números. A partir de agora, expressões também serão usadas para decidir qual trecho do programa deve ser executado.

## Os seis operadores de comparação

| Operador | Leitura | Exemplo | Resultado |
| :---: | --- | --- | :---: |
| `>` | maior que | `8 > 5` | `true` |
| `<` | menor que | `8 < 5` | `false` |
| `>=` | maior ou igual a | `8 >= 8` | `true` |
| `<=` | menor ou igual a | `7 <= 6` | `false` |
| `==` | igual a | `4 == 4` | `true` |
| `!=` | diferente de | `4 != 4` | `false` |

O operador de igualdade é `==`, com dois sinais. Um único `=` continua sendo atribuição.

```java
int quantidade = 10;                 // atribui 10
boolean temDez = quantidade == 10;   // compara com 10
```

Trocar `==` por `=` não é uma abreviação: muda completamente a operação.

## Comparações produzem `boolean`

O resultado pode ser impresso, guardado em uma variável ou usado diretamente por uma estrutura condicional:

```java
double nota = 7.5;

boolean aprovado = nota >= 6.0;
System.out.println(aprovado);       // true
System.out.println(nota < 6.0);     // false
```

Neste primeiro material, o importante é separar a **pergunta** de seu **resultado**:

| Expressão | Pergunta feita | Resposta |
| --- | --- | :---: |
| `nota >= 6.0` | a nota é pelo menos 6? | `true` ou `false` |
| `idade < 18` | a idade é menor que 18? | `true` ou `false` |
| `numero % 2 == 0` | o resto da divisão por 2 é zero? | `true` ou `false` |

## Comparando números

Os operadores relacionais funcionam com os tipos numéricos e com `char`:

```java
int a = 10;
double b = 10.0;

System.out.println(a == b);  // true: os valores numéricos são iguais
System.out.println(a < 12);  // true
System.out.println(b != 10); // false
```

Java promove o tipo menor antes da comparação. Por isso, comparar `int` com `double` é permitido.

Também é possível comparar caracteres, porque um `char` guarda um código numérico:

```java
System.out.println('A' < 'B'); // true
System.out.println('a' > 'Z'); // true
```

Esse tipo de comparação depende dos códigos Unicode. Para quem está começando, é mais claro comparar números e usar `char` apenas quando o problema realmente pedir.

## Limites de intervalos

Grande parte dos erros em condições acontece nos limites. Considere uma nota válida de 0 a 10:

```java
double nota = 10.0;

System.out.println(nota > 0);   // true, mas exclui o zero
System.out.println(nota >= 0);  // true e inclui o zero
System.out.println(nota < 10);  // false, porque exclui o dez
System.out.println(nota <= 10); // true e inclui o dez
```

Antes de escrever o operador, leia o requisito com atenção:

- **maior que 18** corresponde a `idade > 18`;
- **a partir de 18** corresponde a `idade >= 18`;
- **no máximo 100** corresponde a `valor <= 100`;
- **menos de 5** corresponde a `quantidade < 5`.

## Comparando valores de ponto flutuante

Números `double` podem guardar pequenas aproximações. Por isso, uma conta que parece resultar exatamente em `0.3` pode não ser igual a `0.3` por dentro:

```java
double resultado = 0.1 + 0.2;

System.out.println(resultado);        // 0.30000000000000004
System.out.println(resultado == 0.3); // false
```

Quando uma tolerância for aceitável, compare a distância entre os valores:

```java
double diferenca = Math.abs(resultado - 0.3);
boolean aproximadamenteIgual = diferenca < 0.000001;

System.out.println(aproximadamenteIgual); // true
```

`Math.abs` já foi apresentado na Seção 3; nenhum conceito novo é necessário aqui.

## `==` em textos

`String` é um tipo por referência. Para tipos por referência, `==` verifica se as variáveis apontam para o mesmo objeto, e não se os textos possuem as mesmas letras. Portanto, não use `==` para comparar o conteúdo digitado pelo usuário.

```java
String resposta = "sim";

System.out.println(resposta == "sim"); // não é a comparação de conteúdo adequada
```

A comparação de conteúdo de objetos será estudada com mais contexto quando o curso aprofundar classes e métodos. Nesta seção, as decisões principais usam números, caracteres e valores `boolean`.

## Precedência

As operações aritméticas acontecem antes das comparações:

```java
int x = 3;
int y = 4;

boolean resultado = x + y > 5; // equivale a (x + y) > 5
System.out.println(resultado);  // true
```

Os parênteses podem tornar a intenção mais clara, mas uma comparação inteira não pode participar de uma soma:

```java
boolean certo = (x + y) > 5;
// int errado = x + (y > 5); // erro: não se soma int com boolean
```

## Teste rápido

Considere:

```java
int x = 8;
int y = 3;
```

| Expressão | Resultado |
| --- | :---: |
| `x > y` | `true` |
| `x <= 8` | `true` |
| `x == y` | `false` |
| `x != y` | `true` |
| `x % 2 == 0` | `true` |
| `y % 2 != 0` | `true` |

Faça esse tipo de avaliação no papel antes de usar a condição em um `if`. O teste de mesa começa pela capacidade de prever cada expressão isoladamente.

## Referências

- [OCPJ21 Study Guide - Chapter 4: Working with Data](../ocpj21-book/ch04.md), seções *Equality Operators* e *Relational Operators*.
- [Java Language Specification 25 - Equality Operators](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.21).
- [Java Language Specification 25 - Relational Operators](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.20).

---

<div align="center">

📂 [Seção 4](./README.md) &nbsp;·&nbsp; [A2 · Expressões lógicas](./A2%20-%20Expressoes%20logicas.md) ➡️

</div>
