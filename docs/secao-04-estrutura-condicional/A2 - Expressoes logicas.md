# Expressões lógicas

<sub>📚 [Documentação](../README.md) › [Seção 4 · Estrutura condicional](./README.md) › Material 2 de 8</sub>

Uma expressão lógica combina ou inverte valores `boolean`. Ela permite transformar perguntas simples, como `idade >= 18`, em perguntas mais completas, como "a idade está entre 18 e 65?".

Os três operadores usados primeiro são:

| Operador | Nome | Ideia |
| :---: | --- | --- |
| `&&` | E lógico | as duas condições precisam ser verdadeiras |
| `||` | OU lógico | pelo menos uma condição precisa ser verdadeira |
| `!` | NÃO lógico | inverte `true` e `false` |

## Operador E `&&`

O resultado de `a && b` só é `true` quando **as duas** partes são `true`.

| `a` | `b` | `a && b` |
| :---: | :---: | :---: |
| `false` | `false` | `false` |
| `false` | `true` | `false` |
| `true` | `false` | `false` |
| `true` | `true` | `true` |

Exemplo: uma nota é válida quando está entre 0 e 10, incluindo os limites.

```java
double nota = 7.5;
boolean notaValida = nota >= 0.0 && nota <= 10.0;

System.out.println(notaValida); // true
```

As duas comparações são avaliadas separadamente:

```text
nota >= 0.0   -> true
nota <= 10.0  -> true
true && true  -> true
```

Java não aceita a notação matemática `0 <= nota <= 10`. É preciso repetir a variável: `nota >= 0 && nota <= 10`.

## Operador OU `||`

O resultado de `a || b` é `true` quando **pelo menos uma** das partes é `true`.

| `a` | `b` | `a || b` |
| :---: | :---: | :---: |
| `false` | `false` | `false` |
| `false` | `true` | `true` |
| `true` | `false` | `true` |
| `true` | `true` | `true` |

Exemplo: um valor está fora do intervalo de 0 a 10 quando é menor que 0 **ou** maior que 10.

```java
double nota = 12.0;
boolean foraDoIntervalo = nota < 0.0 || nota > 10.0;

System.out.println(foraDoIntervalo); // true
```

## Operador NÃO `!`

O `!` inverte um valor booleano:

| `a` | `!a` |
| :---: | :---: |
| `false` | `true` |
| `true` | `false` |

```java
boolean sistemaAberto = false;
boolean sistemaFechado = !sistemaAberto;

System.out.println(sistemaFechado); // true
```

Ele também pode negar uma expressão inteira:

```java
int idade = 16;
boolean maiorDeIdade = idade >= 18;

System.out.println(!maiorDeIdade); // true
System.out.println(!(idade >= 18)); // true
```

No segundo caso, os parênteses deixam claro o que está sendo negado.

## Traduzindo frases para condições

| Requisito | Expressão Java |
| --- | --- |
| idade entre 18 e 65, inclusive | `idade >= 18 && idade <= 65` |
| temperatura abaixo de 10 ou acima de 35 | `temperatura < 10 || temperatura > 35` |
| número não é zero | `numero != 0` |
| número é par e positivo | `numero % 2 == 0 && numero > 0` |
| não está aprovado | `!aprovado` |

Comece escrevendo cada pergunta simples. Depois escolha `&&` quando todas precisam valer ou `||` quando uma delas basta.

## Avaliação de curto-circuito

Os operadores `&&` e `||` podem deixar de avaliar a segunda parte quando o resultado já está decidido.

No `&&`, se a primeira parte é `false`, o resultado completo só pode ser `false`:

```java
int divisor = 0;
boolean podeDividir = divisor != 0 && 10 / divisor > 2;

System.out.println(podeDividir); // false, sem divisão por zero
```

Como `divisor != 0` é `false`, Java não executa `10 / divisor > 2`. Isso evita a `ArithmeticException` que a divisão inteira por zero provocaria.

No `||`, se a primeira parte é `true`, o resultado completo já é `true`:

```java
int idade = 70;
boolean prioridade = idade >= 60 || idade <= 12;
```

Como `idade >= 60` é `true`, a segunda comparação não precisa ser avaliada.

> [!TIP]
> Coloque primeiro a condição que protege a segunda. A ordem `10 / divisor > 2 && divisor != 0` ainda tenta dividir por zero.

## `&` e `|` com valores booleanos

Java também permite `&` e `|` entre valores `boolean`. O resultado lógico é semelhante ao de `&&` e `||`, mas **as duas partes sempre são avaliadas**.

```java
boolean a = false;
boolean b = true;

System.out.println(a & b);  // false
System.out.println(a | b);  // true
```

Nesta etapa do curso, prefira `&&` e `||`. Eles expressam a intenção com clareza e evitam avaliações desnecessárias. O uso de `&` e `|` com números pertence ao tópico de operadores bitwise, estudado na Seção 6.

## Precedência dos operadores

Entre os operadores vistos até aqui, a ordem principal, da maior para a menor precedência, é:

1. negação lógica e sinais unários: `!`, `+`, `-`;
2. multiplicação, divisão e resto: `*`, `/`, `%`;
3. adição e subtração: `+`, `-`;
4. comparações: `<`, `<=`, `>`, `>=`;
5. igualdade: `==`, `!=`;
6. E lógico: `&&`;
7. OU lógico: `||`.

```java
int idade = 20;
double renda = 1800.0;
boolean estudante = true;

boolean desconto = idade < 18 || renda < 2000.0 && estudante;
```

O `&&` vem antes do `||`, então a expressão equivale a:

```java
boolean desconto = idade < 18 || (renda < 2000.0 && estudante);
```

Mesmo quando os parênteses não são obrigatórios, use-os para mostrar como a regra foi pensada.

## Leis úteis de negação

Negar um intervalo pode ser mais fácil se a comparação e o conector forem invertidos:

```java
boolean dentro = idade >= 18 && idade <= 65;
boolean fora = idade < 18 || idade > 65;
```

As duas condições são opostas. Em termos gerais:

- `!(a && b)` equivale a `!a || !b`;
- `!(a || b)` equivale a `!a && !b`.

Para iniciantes, a melhor estratégia não é decorar a fórmula, mas testar valores nos limites e conferir se a condição responde à pergunta correta.

## Teste de mesa da condição

Para `idade >= 18 && idade <= 65`, experimente valores antes, nos limites e depois do intervalo:

| `idade` | `idade >= 18` | `idade <= 65` | Resultado |
| ---: | :---: | :---: | :---: |
| 17 | `false` | `true` | `false` |
| 18 | `true` | `true` | `true` |
| 65 | `true` | `true` | `true` |
| 66 | `true` | `false` | `false` |

Testar os limites encontra erros de `>` e `>=` mais rapidamente do que testar apenas um valor no meio do intervalo.

## Referências

- [OCPJ21 Study Guide - Chapter 4: Working with Data](../ocpj21-book/ch04.md), seção *Logical Operators*.
- [Java Language Specification 25 - Conditional-And Operator](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.23).
- [Java Language Specification 25 - Conditional-Or Operator](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.24).

---

<div align="center">

⬅️ [A1 · Expressões comparativas](./A1%20-%20Expressoes%20comparativas.md) &nbsp;·&nbsp; 📂 [Seção 4](./README.md) &nbsp;·&nbsp; [A3 · Estrutura condicional if-else](./A3%20-%20Estrutura%20condicional%20if-else.md) ➡️

</div>
