# Processamento de dados e casting

Processar é transformar valores e guardar o resultado. Em Java isso acontece por meio de **atribuições** e **conversões de tipo**.

## Atribuição

O `=` **não** é igualdade matemática: ele copia o valor da direita para a variável da esquerda.

```java
int x = 5;
x = x + 3;    // lê-se: o novo x é o x anterior mais 3
```

Por isso `x = x + 3` faz sentido em programação e não faria em matemática.

### Operadores de atribuição cumulativa

```java
int x = 10;
x += 5;    // equivale a x = x + 5   → 15
x -= 3;    // x = x - 3              → 12
x *= 2;    // x = x * 2              → 24
x /= 4;    // x = x / 4              → 6
x %= 4;    // x = x % 4              → 2
```

### Incremento e decremento

```java
int i = 5;
i++;   // 6   — equivale a i = i + 1
i--;   // 5
```

A posição do operador muda o valor da **expressão**, não o da variável:

```java
int a = 5;
System.out.println(a++);   // imprime 5, depois a vira 6  (pós-incremento)

int b = 5;
System.out.println(++b);   // b vira 6, depois imprime 6  (pré-incremento)
```

Em uma linha isolada, `a++` e `++a` produzem o mesmo efeito. A diferença só importa quando o valor é usado na mesma expressão — e é aí que a certificação costuma armar as pegadinhas.

## Conversão implícita (widening)

![Conversão entre tipos numéricos](./conversao-numerica.svg)

Quando o valor cabe com folga no tipo de destino, Java converte sozinho, sem perda:

```java
int inteiro = 100;
double decimal = inteiro;     // 100.0 — conversão automática
long grande = inteiro;        // 100
```

A ordem é `byte → short → int → long → float → double`, e `char → int`. Ir para a **direita** é automático.

> `long` para `float` é conversão implícita mesmo os dois tendo tamanhos diferentes: `float` cobre uma faixa maior de valores, ainda que com menos precisão. É por isso que a ordem da conversão não é a ordem dos tamanhos em bits.

## Conversão explícita (casting)

Ir para a **esquerda** exige que o programador assuma a responsabilidade, escrevendo o tipo entre parênteses:

```java
double valor = 3.99;
int inteiro = (int) valor;      // 3 — a parte decimal é descartada, não arredondada
System.out.println(inteiro);
```

```java
double d = 3.99;
int errado = d;                 // erro: possible lossy conversion from double to int
```

O casting **trunca**, nunca arredonda. Para arredondar existe `Math.round`, no material [A7](./A7%20-%20Funcoes%20matematicas%20em%20Java.md).

### Casting pode estourar silenciosamente

```java
int grande = 300;
byte pequeno = (byte) grande;
System.out.println(pequeno);    // 44 — os bits que não couberam foram descartados
```

Nenhum erro, nenhum aviso: o valor simplesmente fica errado. Esse é o preço de forçar a conversão.

## Promoção numérica em expressões

Antes de calcular, Java **promove** os operandos a um tipo comum. As regras, na ordem:

1. Se um operando for `double`, o outro é promovido a `double`.
2. Senão, se um for `float`, o outro é promovido a `float`.
3. Senão, se um for `long`, o outro é promovido a `long`.
4. Senão, **ambos são promovidos a `int`** — inclusive `byte`, `short` e `char`.

```java
int a = 10;
double b = 3;
System.out.println(a / b);        // 3.3333333333333335 — a virou double

byte x = 10, y = 20;
byte soma = x + y;                // erro: o resultado de x + y é int
byte certo = (byte) (x + y);      // 30 — precisa do casting
```

A regra 4 surpreende: somar dois `byte` produz um `int`. Vale para `short` e `char` também.

```java
char letra = 'A';
System.out.println(letra + 1);          // 66 — virou int
System.out.println((char) (letra + 1)); // B
```

## Dividindo inteiros e esperando decimal

O erro mais frequente da seção, em três versões:

```java
int a = 10, b = 4;

double errado = a / b;             // 2.0 — a divisão inteira aconteceu antes
double certo1 = (double) a / b;    // 2.5 — converte antes de dividir
double certo2 = a / (double) b;    // 2.5
double certo3 = a / 4.0;           // 2.5 — literal já é double
```

## Convertendo texto em número

Dados que chegam como texto — de um arquivo, de um formulário, de `args` — precisam ser convertidos:

```java
String texto = "42";
int numero = Integer.parseInt(texto);        // 42
double decimal = Double.parseDouble("3.14"); // 3.14
long longo = Long.parseLong("900000");
```

E o caminho inverso:

```java
int numero = 42;
String texto1 = String.valueOf(numero);   // "42"
String texto2 = "" + numero;              // "42" — funciona, mas menos claro
```

Se o texto não representa um número válido, o programa lança `NumberFormatException` em tempo de execução:

```java
int erro = Integer.parseInt("abc");   // NumberFormatException
int erro2 = Integer.parseInt("3.14"); // NumberFormatException — parseInt não aceita decimal
```

> `Double.parseDouble` espera o **ponto** como separador decimal, independentemente do idioma do sistema. `Double.parseDouble("3,14")` falha.

## Precisão de ponto flutuante

`double` e `float` guardam números em base 2, e nem todo decimal tem representação exata:

```java
System.out.println(0.1 + 0.2);          // 0.30000000000000004
System.out.println(0.1 + 0.2 == 0.3);   // false
```

Isso não é bug de Java: é como o padrão IEEE 754 funciona em qualquer linguagem. Para dinheiro e outros valores que exigem exatidão, a solução é `BigDecimal`, que fica para mais adiante no curso.

## Referências

- [OCPJ21 Study Guide — Chapter 4: Working with Data](../ocpj21-book/ch04.md), seções *Unary Operators*, *Binary Operators* e *Assignment Operators*.
