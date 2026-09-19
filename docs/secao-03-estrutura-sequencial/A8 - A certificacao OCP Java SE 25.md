# A certificação OCP Java SE 25 e esta seção

<sub>📚 [Documentação](../README.md) › [Seção 3 · Estrutura sequencial](./README.md) › Material 8 de 8</sub>

Este material relaciona a Seção 3 com a certificação **Oracle Certified Professional Java SE 25 Developer**, exame **1Z0-831**.

> [!NOTE]
> O objetivo é revisar apenas o que já foi ensinado. Operadores condicionais, repetições, arrays, objetos e tratamento de exceções serão relacionados à prova somente nas seções correspondentes.

## Grupos de objetivos relacionados

| Grupo de objetivos | Conteúdo já estudado |
| --- | --- |
| Handling Date, Time, Text, Numeric and Boolean Values | tipos primitivos, literais, operadores aritméticos, casting, `String`, formatação e `Math` |
| Performing Input Output Operations | entrada e saídas padrão com `Scanner`, `System.in` e `System.out` |
| Developing Applications with Localization Support | efeito de `Locale` na leitura e na formatação de números |

## Tipos primitivos e literais

Do conteúdo desta seção, é importante saber:

- os oito tipos primitivos e suas faixas gerais;
- que variáveis locais precisam ser inicializadas antes da leitura;
- que literais inteiros são `int` por padrão;
- que literais com ponto decimal são `double` por padrão;
- os sufixos `L`, `F` e `D`;
- as notações hexadecimal, binária e octal;
- as regras do `_` em literais numéricos;
- a diferença entre `char` e `String`.

Tipos por referência serão aprofundados junto com orientação a objetos. Nesta seção, `String` e `Scanner` são usados somente pelo comportamento necessário aos programas básicos.

## Operadores aritméticos e casting

A prova exige atenção a:

- precedência de `*`, `/`, `%`, `+` e `-`;
- divisão inteira quando os dois operandos são inteiros;
- uso de casting antes da divisão para produzir um resultado decimal;
- resto da divisão com `%`;
- promoção de `byte`, `short` e `char` para `int` nas expressões;
- conversões implícitas para tipos mais amplos;
- perda de dados em conversões explícitas;
- truncamento da parte decimal pelo casting.

Os operadores de comparação e as formas abreviadas de atribuição ficam para a Seção 4.

## Saída e formatação

Do material de saída, revise:

- diferença entre `print`, `println` e `printf`;
- especificadores `%d`, `%f`, `%s`, `%c`, `%b`, `%n` e `%%`;
- quantidade de casas decimais em `%.2f`;
- largura e alinhamento de campos;
- sequências de escape como `\n`, `\t`, `\"` e `\\`;
- efeito do `Locale` sobre o separador decimal.

## Funções matemáticas

É necessário prever o tipo e o valor produzido por chamadas como:

- `Math.sqrt` e `Math.pow`, que devolvem `double`;
- `Math.abs`;
- `Math.max` e `Math.min`;
- `Math.round`, `Math.floor` e `Math.ceil`;
- `Math.random`, cujo resultado começa em `0.0` e não chega a `1.0`.

## Entrada padrão

Nesta etapa, basta reconhecer:

- `System.in` como entrada padrão;
- `System.out` como saída padrão;
- o uso de `Scanner` para ler tokens e linhas;
- a diferença entre `next` e `nextLine`;
- a quebra de linha pendente depois de leituras numéricas;
- o efeito de `Locale` sobre `nextDouble`;
- que fechar o `Scanner` ligado a `System.in` fecha também a entrada padrão.

## Questões de revisão

**1. Qual é a saída?**

```java
int a = 7;
int b = 2;
System.out.println(a / b);
System.out.println(a % b);
System.out.println((double) a / b);
```

<details>
<summary><b>💡 Resposta</b></summary>

`3`, `1` e `3.5`. As duas primeiras operações usam inteiros. Na terceira, o casting ocorre antes da divisão.
</details>

**2. O trecho compila?**

```java
byte a = 10;
byte b = 20;
byte soma = a + b;
```

<details>
<summary><b>💡 Resposta</b></summary>

Não. `a + b` produz `int`, mesmo que os dois operandos sejam `byte`. Seria necessário um casting explícito.
</details>

**3. Qual é a saída?**

```java
System.out.println(1 + 2 + "3" + 4);
```

<details>
<summary><b>💡 Resposta</b></summary>

`334`. Primeiro ocorre `1 + 2`, que resulta em `3`. Depois da entrada da `String`, as operações seguintes são concatenações.
</details>

**4. Qual valor é armazenado?**

```java
double valor = 3.99;
int inteiro = (int) valor;
```

<details>
<summary><b>💡 Resposta</b></summary>

`3`. O casting descarta a parte decimal; ele não arredonda.
</details>

**5. Quais são os tipos dos resultados?**

```java
double raiz = Math.sqrt(16);
long arredondado = Math.round(3.6);
```

<details>
<summary><b>💡 Resposta</b></summary>

`Math.sqrt` devolve `double`, portanto `raiz` recebe `4.0`. `Math.round(double)` devolve `long`, portanto `arredondado` recebe `4`.
</details>

**6. O que acontece?**

```java
int total;
System.out.println(total);
```

<details>
<summary><b>💡 Resposta</b></summary>

Erro de compilação. A variável local foi declarada, mas não recebeu valor antes da leitura.
</details>

**7. Qual formato imprime duas casas decimais e termina a linha?**

<details>
<summary><b>💡 Resposta</b></summary>

`System.out.printf("%.2f%n", valor);`.
</details>

**8. Por que este padrão pode pular a leitura do nome?**

```java
int idade = sc.nextInt();
String nome = sc.nextLine();
```

<details>
<summary><b>💡 Resposta</b></summary>

`nextInt` deixa a quebra de linha pendente. O `nextLine` seguinte consome essa quebra e devolve uma linha vazia. Um `sc.nextLine()` extra entre as duas leituras descarta o restante da linha.
</details>

## Referências

- [OCPJ21 Study Guide - Chapter 4: Working with Data](../ocpj21-book/ch04.md)
- [OCPJ21 Study Guide - Chapter 12: File I O](../ocpj21-book/ch12.md)
- [Certificação Oracle Certified Professional Java SE 25 Developer](https://education.oracle.com/java-se-25-developer-professional/pexam_1Z0-831)

---

<div align="center">

⬅️ [A7 · Funções matemáticas em Java](./A7%20-%20Funcoes%20matematicas%20em%20Java.md) &nbsp;·&nbsp; 📂 [Seção 3](./README.md) &nbsp;·&nbsp; [Seção 4 · Estrutura condicional](../secao-04-estrutura-condicional/README.md) ➡️

</div>
