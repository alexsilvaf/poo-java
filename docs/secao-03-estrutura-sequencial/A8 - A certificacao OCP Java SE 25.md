# A certificação OCP Java SE 25 e esta seção

Este material relaciona o conteúdo da Seção 3 com o que a Oracle cobra na certificação **Oracle Certified Professional, Java SE 25 Developer** (exame **1Z0-831**). Os dados da prova — formato, duração e nota de corte — estão no [A8 da Seção 2](../secao-02-introducao-java/A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md).

> A Seção 2 era quase toda contexto e plataforma, e pouco dela caía na prova. A Seção 3 é o oposto: praticamente tudo o que ela ensina é cobrado, porque tipos, operadores e conversões são a base sobre a qual as outras questões são construídas.

## Grupos de objetivos tocados por esta seção

| Grupo de objetivos | O que desta seção entra |
|---|---|
| **Handling Date, Time, Text, Numeric and Boolean Values** | tipos primitivos, literais, operadores, casting, promoção numérica, `String`, formatação, `Math` |
| **Performing Input/Output Operations** | entrada padrão com `Scanner` |
| Developing Applications with Localization Support | `Locale` afetando formatação e leitura de números |
| Applying Object-Oriented Principles | declaração de variáveis, `final`, `var` |

## O que desta seção cai na prova

### Tipos primitivos e literais (material A1)

Do que **esta seção ensina**, a prova exige saber:

- os oito tipos primitivos, seus tamanhos e seus valores padrão;
- que os valores padrão valem para **atributos**, e que **variáveis locais precisam ser inicializadas** antes do uso — o contrário é erro de compilação;
- os sufixos `L`, `F` e `D`, e por que `long g = 8100000000;` e `float f = 1.75;` não compilam;
- as notações `0x`, `0b` e `0` para literais inteiros;
- as regras do `_` em literais numéricos: nem no começo, nem no fim, nem ao lado do ponto decimal, nem antes do sufixo;
- que `var` é inferência em tempo de compilação, exige inicializador e não aceita `null`;
- que uma variável `final` só pode ser atribuída uma vez.

> Corresponde ao **Capítulo 4** do [OCPJ21 Study Guide](../ocpj21-book/ch04.md), seção *Understanding Data Types*.

> **Vai além desta seção:** *wrapper classes* (`Integer`, `Double`), *autoboxing* e *unboxing*, e o cache de `Integer` entre -128 e 127. A prova cobra isso no mesmo grupo de objetivos, mas depende de conceitos de objeto que só chegam na Seção 7.

### Operadores, casting e promoção numérica (materiais A2 e A5)

Este é o assunto mais cobrado da seção:

- divisão inteira contra divisão de ponto flutuante, e o momento certo de aplicar o casting;
- `ArithmeticException` na divisão inteira por zero, contra `Infinity` e `NaN` na divisão de ponto flutuante;
- precedência entre `*`, `/`, `%` e `+`, `-`, e a avaliação da esquerda para a direita;
- a regra de promoção: `byte`, `short` e `char` são **sempre promovidos a `int`** em uma expressão aritmética — por isso `byte soma = b + c;` não compila;
- que o casting trunca em vez de arredondar, e que ele pode estourar em silêncio: `(byte) 300` é `44`;
- pré e pós-incremento na mesma expressão (`i++ + ++i`);
- que os operadores cumulativos (`+=`, `-=`, ...) fazem um casting implícito, e por isso `short s = 5; s += 1;` compila enquanto `s = s + 1;` não;
- concatenação com `+`: assim que uma `String` entra na expressão, tudo à direita vira texto.

> Corresponde ao **Capítulo 4** do [OCPJ21 Study Guide](../ocpj21-book/ch04.md), seções *Operators*, *Unary Operators*, *Binary Operators* e *Assignment Operators*.

> **Vai além desta seção:** operadores bitwise e de deslocamento (`&`, `|`, `^`, `<<`, `>>`, `>>>`), que estão na Seção 6, e os operadores lógicos e relacionais, que estão na Seção 4.

### Saída e formatação (material A4)

- os especificadores `%d`, `%f`, `%s`, `%c`, `%b`, `%n` e `%%`;
- largura, alinhamento com `-`, preenchimento com `0` e casas decimais com `.n`;
- a diferença entre `%n` e `\n`;
- `String.format` produzindo a mesma saída de `printf`, porém como valor;
- `IllegalFormatConversionException` quando o especificador não corresponde ao tipo do argumento;
- as sequências de escape `\n`, `\t`, `\"` e `\\`;
- *text blocks*: as três aspas, a remoção da indentação comum e a exigência de que o conteúdo comece na linha seguinte à abertura.

> Corresponde ao **Capítulo 4** do [OCPJ21 Study Guide](../ocpj21-book/ch04.md), seções *Formatting Strings* e *Text Blocks*.

> **Vai além desta seção:** os métodos de `String` e `StringBuilder`, a imutabilidade de `String` e o *string pool*. A Seção 6 cobre parte disso.

### A API `Math` (material A7)

- que os métodos são estáticos e que `Math` não é instanciável;
- que `sqrt`, `cbrt` e `pow` devolvem sempre `double`;
- que `Math.round(double)` devolve `long` e `Math.round(float)` devolve `int`, enquanto `floor` e `ceil` devolvem `double`;
- que `Math.round(-2.5)` é `-2`, porque a definição é `floor(x + 0.5)`;
- que `Math.abs(Integer.MIN_VALUE)` continua negativo;
- a faixa de `Math.random()`: de `0.0` inclusive a `1.0` exclusive.

> Corresponde ao **Capítulo 4** do [OCPJ21 Study Guide](../ocpj21-book/ch04.md), seção *The Math API*.

### Entrada padrão (material A6)

- que `System.in`, `System.out` e `System.err` são os fluxos padrão;
- que fechar um `Scanner` ligado a `System.in` fecha a entrada padrão do programa;
- `InputMismatchException` e `NoSuchElementException`, e o que provoca cada uma.

> Corresponde ao **Capítulo 12** do [OCPJ21 Study Guide](../ocpj21-book/ch12.md), seção *Standard Streams*.

> **Vai além desta seção:** todo o resto do Capítulo 12 — `Path`, `Files`, fluxos de arquivo, serialização. `Scanner` aparece na prova como coadjuvante; o peso está na API de arquivos.

## O que desta seção **não** cai na prova

- o conceito de estrutura sequencial e o teste de mesa — são ferramentas de aprendizagem, não conteúdo de linguagem;
- a distinção didática entre entrada, processamento e saída;
- convenções de nomes como `camelCase` e `PascalCase` — a prova cobra o que **compila**, não o que é elegante;
- a explicação de *stack* e *heap* como modelo mental de memória.

## Exemplos no estilo da prova

**1.** O que este código imprime?

```java
int a = 7, b = 2;
System.out.println(a / b);
System.out.println(a % b);
System.out.println((double) a / b);
```

<details>
<summary>Resposta</summary>

`3`, `1` e `3.5`. Os dois primeiros são divisão e resto inteiros. No terceiro, o casting transforma `a` em `double` **antes** da divisão, e a promoção leva `b` junto.
</details>

**2.** O que acontece ao compilar?

```java
byte a = 10;
byte b = 20;
byte soma = a + b;
```

<details>
<summary>Resposta</summary>

**Erro de compilação:** `incompatible types: possible lossy conversion from int to byte`. Em uma expressão aritmética, `byte`, `short` e `char` são promovidos a `int`, então `a + b` é um `int`. Seria preciso escrever `byte soma = (byte) (a + b);`.
</details>

**3.** E este, compila?

```java
short s = 5;
s += 1;
```

<details>
<summary>Resposta</summary>

**Sim**, e `s` fica valendo `6`. Os operadores de atribuição cumulativa aplicam um casting implícito para o tipo da variável. Já `s = s + 1;` **não** compilaria, pela regra da promoção a `int`.
</details>

**4.** Qual é a saída?

```java
System.out.println(1 + 2 + "3" + 4 + 5);
```

<details>
<summary>Resposta</summary>

`3345`. A avaliação é da esquerda para a direita: `1 + 2` ainda é soma e dá `3`; a partir da `String` `"3"`, tudo vira concatenação.
</details>

**5.** O que é impresso?

```java
int x = 5;
x = x++;
System.out.println(x);
```

<details>
<summary>Resposta</summary>

`5`. O pós-incremento devolve o valor antigo (`5`), incrementa `x` para `6`, e a atribuição então sobrescreve `x` com o `5` que havia sido devolvido.
</details>

**6.** Qual é o resultado?

```java
System.out.println(Math.round(-2.5));
System.out.println(Math.round(2.5));
```

<details>
<summary>Resposta</summary>

`-2` e `3`. `Math.round(x)` equivale a `floor(x + 0.5)`: `floor(-2.0)` é `-2` e `floor(3.0)` é `3`.
</details>

**7.** O que este código faz em tempo de execução?

```java
System.out.println(10 / 0);
```

<details>
<summary>Resposta</summary>

Lança **`ArithmeticException: / by zero`**. Se fosse `10.0 / 0`, não haveria exceção: o resultado seria `Infinity`.
</details>

**8.** Qual é a saída?

```java
double d = 3.99;
int i = (int) d;
System.out.println(i);
```

<details>
<summary>Resposta</summary>

`3`. O casting **trunca**, descartando a parte decimal. Para obter `4`, seria preciso `Math.round(d)`.
</details>

**9.** Este código compila?

```java
public class Teste {
    static int contador;

    public static void main(String[] args) {
        int total;
        System.out.println(contador);
        System.out.println(total);
    }
}
```

<details>
<summary>Resposta</summary>

**Não.** `contador` é um atributo e recebe o valor padrão `0`, mas `total` é uma variável local: `variable total might not have been initialized`.
</details>

**10.** O que `Integer.parseInt("3.14")` devolve?

<details>
<summary>Resposta</summary>

Nada: lança **`NumberFormatException`**. `parseInt` só aceita a representação de um inteiro. Para `3.14` seria preciso `Double.parseDouble`, que exige o ponto como separador decimal.
</details>

## Referências

- [OCPJ21 Study Guide — Chapter 4: Working with Data](../ocpj21-book/ch04.md)
- [OCPJ21 Study Guide — Chapter 12: File I/O](../ocpj21-book/ch12.md)
- [Certificação Oracle Certified Professional, Java SE 25 Developer](https://education.oracle.com/java-se-25-developer-professional/pexam_1Z0-831)
