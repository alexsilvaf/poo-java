# Operadores bitwise

<sub>📚 [Documentação](../README.md) › [Seção 6 · Outros tópicos básicos sobre Java](./README.md) › Material 2 de 8</sub>

Os operadores **bitwise** trabalham com a representação binária dos tipos inteiros. Nesta aula, os exemplos usam valores pequenos para que cada bit possa ser acompanhado no papel.

## Relembrando o binário

Um literal iniciado por `0b` está escrito em base 2:

```java
int a = 0b1100; // 12
int b = 0b1010; // 10

System.out.println(a); // 12
System.out.println(b); // 10
```

## `&`, `|` e `^`

Os operadores comparam os bits da mesma posição:

| `a` | `b` | `a & b` | `a | b` | `a ^ b` |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

- `&` mantém 1 somente quando os dois bits são 1;
- `|` produz 1 quando ao menos um bit é 1;
- `^` produz 1 quando os bits são diferentes.

```text
  1100  (12)
& 1010  (10)
  ----
  1000  (8)

  1100
| 1010
  ----
  1110  (14)

  1100
^ 1010
  ----
  0110  (6)
```

```java
int a = 0b1100;
int b = 0b1010;

System.out.println(a & b); // 8
System.out.println(a | b); // 14
System.out.println(a ^ b); // 6
```

## Complemento `~`

`~` inverte todos os bits. Os tipos inteiros usam complemento de dois, então:

```java
int x = 5;
System.out.println(~x); // -6
```

Uma relação útil é `~x == -x - 1`.

Não observe apenas os quatro últimos bits: um `int` possui 32 bits, inclusive os bits usados na representação do sinal.

## Deslocamentos

| Operador | Efeito |
| :---: | --- |
| `<<` | desloca para a esquerda e preenche com zeros à direita |
| `>>` | desloca para a direita e preserva o bit de sinal |
| `>>>` | desloca para a direita e preenche com zeros à esquerda |

```java
int valor = 12; // 1100

System.out.println(valor << 1); // 24
System.out.println(valor >> 1); // 6
```

Enquanto não ocorre perda de bits, deslocar uma posição à esquerda equivale a multiplicar por 2. Deslocar à direita um valor positivo equivale a dividir por 2, descartando o resto.

Para valores negativos, `>>` e `>>>` diferem:

```java
int negativo = -8;

System.out.println(negativo >> 1);  // -4
System.out.println(negativo >>> 1); // 2147483644
```

O segundo resultado é positivo porque `>>>` insere zero na posição mais à esquerda.

## Formas cumulativas

```java
int permissoes = 0b0101;

permissoes |= 0b0010;
permissoes &= 0b0111;
permissoes ^= 0b0001;
permissoes <<= 1;
```

Como nos operadores cumulativos da Seção 4, a operação calcula e guarda o resultado na mesma variável.

## Uso com `boolean`

`&`, `|` e `^` também aceitam valores `boolean`:

```java
boolean a = true;
boolean b = false;

System.out.println(a & b); // false
System.out.println(a | b); // true
System.out.println(a ^ b); // true
```

Com `boolean`, `&` e `|` avaliam os dois lados. Já `&&` e `||`, estudados na Seção 4, podem interromper a avaliação pelo curto-circuito. `^` é verdadeiro quando os lados são diferentes.

## Precedência essencial

Operadores de deslocamento são avaliados antes de `&`, que vem antes de `^`, que vem antes de `|`. Use parênteses quando uma expressão mistura grupos:

```java
int a = 0b1100;
int b = 0b1010;
int resultado = (a & b) | 0b0001;
```

## Questões rápidas

1. `0b0101 & 0b0011` resulta em `0b0001`, ou 1.
2. `0b0101 | 0b0011` resulta em `0b0111`, ou 7.
3. `0b0101 ^ 0b0011` resulta em `0b0110`, ou 6.
4. `8 << 2` resulta em 32.
5. `16 >> 2` resulta em 4.

## Referências

- [OCPJ21 Study Guide - Chapter 4: Working with Data](../ocpj21-book/ch04.md), seção *Operators*.
- [Java Language Specification 25 - Shift Operators](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.19).
- [Java Language Specification 25 - Integer Bitwise Operators](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.22.1).

---

<div align="center">

⬅️ [A1 · Restrições e convenções para nomes](./A1%20-%20Restricoes%20e%20convencoes%20para%20nomes.md) &nbsp;·&nbsp; 📂 [Seção 6](./README.md) &nbsp;·&nbsp; [A3 · Funções interessantes para String](./A3%20-%20Funcoes%20interessantes%20para%20String.md) ➡️

</div>
