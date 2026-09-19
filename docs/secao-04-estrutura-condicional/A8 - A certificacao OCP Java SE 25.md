# A certificação OCP Java SE 25 e esta seção

<sub>📚 [Documentação](../README.md) › [Seção 4 · Estrutura condicional](./README.md) › Material 8 de 8</sub>

Este material relaciona a Seção 4 com a certificação **Oracle Certified Professional, Java SE 25 Developer** (exame **1Z0-831**). O foco permanece nos assuntos já estudados: operadores, decisões, `switch`, ternário, escopo e inicialização de variáveis locais.

## Grupos de objetivos relacionados

| Grupo de objetivos | Conteúdo desta seção |
| --- | --- |
| Handling Date, Time, Text, Numeric and Boolean Values | comparações, igualdade, operadores lógicos e operador ternário |
| Implementing Program Flow Control | `if`, `else`, `switch`, `break` e seleção entre caminhos |
| Applying Object-Oriented Principles | escopo e inicialização de variáveis locais |

## O que desta seção cai na prova

### Comparações e operadores lógicos

É necessário prever:

- o resultado de `<`, `<=`, `>`, `>=`, `==` e `!=`;
- a diferença entre atribuição `=` e igualdade `==`;
- a precedência entre operações aritméticas, comparações, igualdade, `&&` e `||`;
- o efeito da negação `!`;
- a avaliação de curto-circuito de `&&` e `||`;
- a diferença entre `&&` e `&`, ou entre `||` e `|`, quando os operandos são booleanos.

Esses pontos aparecem no [Capítulo 4 do OCPJ21 Study Guide](../ocpj21-book/ch04.md), nas seções sobre operadores de igualdade, relacionais e lógicos.

### `if`, `else if` e `else`

A prova costuma exigir a leitura exata do fluxo:

- a condição de um `if` precisa ser `boolean`;
- um `else` se associa ao `if` ainda sem `else` mais próximo;
- sem chaves, apenas uma instrução pertence ao `if` ou ao `else`;
- um ponto e vírgula logo após a condição forma uma instrução vazia;
- em uma cadeia, somente o primeiro bloco cuja condição for verdadeira é executado.

O assunto corresponde à seção *The if Statement* do [Capítulo 5](../ocpj21-book/ch05.md).

### Atribuição cumulativa e incremento

- `x += y` realiza a operação e converte implicitamente o resultado para o tipo de `x`;
- `byte`, `short` e `char` são promovidos em operações aritméticas comuns;
- `x++` produz o valor antigo e depois incrementa;
- `++x` incrementa e produz o valor novo;
- operações cumulativas podem causar estouro sem lançar erro.

Esse conteúdo se conecta ao material de casting da Seção 3 e à seção *Assignment Operators* do [Capítulo 4](../ocpj21-book/ch04.md).

### `switch`

Na forma tradicional apresentada nesta seção, é preciso saber:

- como o valor selecionado encontra um `case`;
- que `default` executa quando nenhum caso combina;
- que a ausência de `break` permite continuar nos casos seguintes;
- que vários rótulos podem levar ao mesmo bloco;
- que os rótulos precisam ser valores constantes compatíveis.

O assunto corresponde à seção *The switch Statement* do [Capítulo 5](../ocpj21-book/ch05.md).

### Ternário, escopo e inicialização

- o ternário avalia a condição e somente um dos dois resultados;
- a expressão produz um valor, e esse valor precisa ser compatível com o destino;
- uma variável local só pode ser usada dentro de seu escopo;
- todo caminho que chega ao uso de uma variável local precisa tê-la inicializado;
- uma atribuição que ocorre apenas em um `if` sem `else` pode não ser suficiente.

## O que é ferramenta didática

O teste de mesa, os diagramas de fluxo e a escolha de nomes claros ajudam a aprender e a evitar erros. A prova não pergunta pela técnica em si; ela apresenta código e exige exatamente a mesma simulação que o teste de mesa treina.

## Questões no estilo da prova

**1. Qual é a saída?**

```java
int x = 8;
System.out.println(x > 5 && x < 10);
System.out.println(x < 5 || x == 8);
```

<details>
<summary><b>💡 Resposta</b></summary>

`true` e `true`. Na primeira expressão, as duas comparações são verdadeiras. Na segunda, a primeira é falsa, mas a segunda é verdadeira.
</details>

**2. O que acontece?**

```java
int divisor = 0;
boolean resultado = divisor != 0 && 20 / divisor > 2;
System.out.println(resultado);
```

<details>
<summary><b>💡 Resposta</b></summary>

Imprime `false`. Como a primeira parte do `&&` é falsa, a divisão não é avaliada e não ocorre divisão por zero.
</details>

**3. Qual é a saída?**

```java
int idade = 20;

if (idade >= 18)
    System.out.println("A");
    System.out.println("B");
```

<details>
<summary><b>💡 Resposta</b></summary>

Imprime `A` e `B`. Sem chaves, somente a primeira chamada de `println` pertence ao `if`. A segunda sempre executa.
</details>

**4. Qual é a saída?**

```java
int x = 5;

if (x > 0);
{
    System.out.println("Positivo");
}
```

<details>
<summary><b>💡 Resposta</b></summary>

Imprime `Positivo`. O ponto e vírgula encerra o `if` com uma instrução vazia. O bloco seguinte é independente.
</details>

**5. O que é impresso?**

```java
short s = 5;
s += 3.5;
System.out.println(s);
```

<details>
<summary><b>💡 Resposta</b></summary>

`8`. A soma produz um valor decimal, e a atribuição cumulativa inclui uma conversão implícita para `short`, descartando a parte fracionária.
</details>

**6. Qual é a saída?**

```java
int opcao = 2;

switch (opcao) {
    case 1:
        System.out.print("A");
    case 2:
        System.out.print("B");
    case 3:
        System.out.print("C");
        break;
    default:
        System.out.print("D");
}
```

<details>
<summary><b>💡 Resposta</b></summary>

`BC`. A execução começa no `case 2` e continua no `case 3`, onde encontra o `break`.
</details>

**7. Qual valor é atribuído?**

```java
int a = 10;
int b = 4;
int menor = a < b ? a : b;
```

<details>
<summary><b>💡 Resposta</b></summary>

`4`. A condição `a < b` é falsa, então o ternário produz o valor depois dos dois-pontos.
</details>

**8. O código compila?**

```java
int x = 3;
int resultado;

if (x > 0) {
    resultado = 1;
}

System.out.println(resultado);
```

<details>
<summary><b>💡 Resposta</b></summary>

Não. Existe um caminho estrutural em que a condição é falsa e `resultado` não recebe valor. O compilador informa que a variável pode não ter sido inicializada.
</details>

**9. O código compila?**

```java
int x = 3;
int resultado;

if (x > 0) {
    resultado = 1;
} else {
    resultado = -1;
}

System.out.println(resultado);
```

<details>
<summary><b>💡 Resposta</b></summary>

Sim. Os dois caminhos atribuem um valor antes do uso.
</details>

**10. Qual é a saída?**

```java
int x = 5;
int y = x++;
int z = ++x;
System.out.println(x + " " + y + " " + z);
```

<details>
<summary><b>💡 Resposta</b></summary>

`7 5 7`. `y` recebe o valor antigo de `x`, depois `x` vira `6`; em seguida `++x` leva `x` a `7` antes de atribuir `z`.
</details>

## Referências

- [OCPJ21 Study Guide - Chapter 4: Working with Data](../ocpj21-book/ch04.md)
- [OCPJ21 Study Guide - Chapter 5: Making Decisions](../ocpj21-book/ch05.md)
- [Java Language Specification 25 - Expressions](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html)
- [Java Language Specification 25 - Statements](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html)
- [Certificação Oracle Certified Professional, Java SE 25 Developer](https://education.oracle.com/java-se-25-developer-professional/pexam_1Z0-831)

---

<div align="center">

⬅️ [A7 · Escopo e inicialização](./A7%20-%20Escopo%20e%20inicializacao.md) &nbsp;·&nbsp; 📂 [Seção 4](./README.md) &nbsp;·&nbsp; [Seção 5 · Estruturas repetitivas](../secao-05-estruturas-repetitivas/README.md) ➡️

</div>
