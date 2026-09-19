# Operadores de atribuição cumulativa

<sub>📚 [Documentação](../README.md) › [Seção 4 · Estrutura condicional](./README.md) › Material 4 de 8</sub>

Quando uma variável recebe um novo valor calculado a partir dela mesma, Java oferece uma escrita mais curta.

```java
double saldo = 500.0;
saldo = saldo - 80.0;
```

A mesma atualização pode ser escrita assim:

```java
double saldo = 500.0;
saldo -= 80.0;
```

O operador `-=` lê o valor atual de `saldo`, subtrai `80.0` e guarda o resultado novamente em `saldo`.

## Operadores aritméticos cumulativos

| Forma cumulativa | Ideia equivalente | Exemplo a partir de `x = 10` | Novo valor |
| :---: | --- | --- | ---: |
| `x += 3` | `x = x + 3` | soma 3 | 13 |
| `x -= 3` | `x = x - 3` | subtrai 3 | 7 |
| `x *= 3` | `x = x * 3` | multiplica por 3 | 30 |
| `x /= 3` | `x = x / 3` | faz divisão inteira | 3 |
| `x %= 3` | `x = x % 3` | guarda o resto | 1 |

Exemplo com uma conta:

```java
double saldo = 1000.0;

saldo += 250.0; // depósito: 1250.0
saldo -= 80.0;  // saque: 1170.0
saldo *= 1.01;  // acréscimo de 1%: 1181.7

System.out.printf("Saldo: %.2f%n", saldo);
```

## Atualização dentro de uma condição

A atribuição cumulativa muda a variável. Ela pode aparecer em um bloco condicional quando a atualização só deve acontecer em determinado caminho:

```java
double preco = 200.0;
boolean clienteFrequente = true;

if (clienteFrequente) {
    preco *= 0.90; // aplica 10% de desconto
}

System.out.printf("Preco final: %.2f%n", preco);
```

Não confunda calcular 10% com manter 90%. Multiplicar por `0.90` mantém 90% do preço e, portanto, retira 10%.

## Não é apenas uma abreviação textual

Para tipos menores que `int`, a forma cumulativa inclui uma conversão implícita para o tipo da variável:

```java
short quantidade = 5;
quantidade += 1; // compila
```

Mas a forma expandida não compila:

```java
short quantidade = 5;
// quantidade = quantidade + 1; // erro: quantidade + 1 produz int
```

A equivalência completa de `quantidade += 1` é parecida com:

```java
quantidade = (short) (quantidade + 1);
```

Essa conversão pode perder dados sem avisar:

```java
byte valor = 127;
valor += 1;
System.out.println(valor); // -128
```

O valor ultrapassou a faixa do `byte` e deu a volta. A forma curta não torna a operação mais segura.

## A expressão da direita é calculada primeiro

```java
int total = 10;
total *= 2 + 3;

System.out.println(total); // 50
```

O lado direito `2 + 3` é calculado primeiro. Depois ocorre `total *= 5`.

Isso corresponde a:

```java
total = total * (2 + 3);
```

e não a:

```java
total = total * 2 + 3;
```

## Incremento e decremento

Somar ou subtrair exatamente 1 é tão comum que Java possui `++` e `--`:

```java
int contador = 0;

contador++; // contador += 1
contador++; // agora vale 2
contador--; // agora vale 1
```

Quando usados sozinhos em uma linha, `contador++` e `++contador` produzem o mesmo efeito final. A diferença aparece quando o operador faz parte de uma expressão maior:

```java
int a = 5;
int b = a++; // b recebe 5; depois a vira 6

int c = 5;
int d = ++c; // c vira 6; depois d recebe 6
```

| Operação | Valor atualizado | Valor produzido pela expressão |
| --- | --- | --- |
| `x++` | soma 1 a `x` | valor antigo |
| `++x` | soma 1 a `x` | valor novo |
| `x--` | subtrai 1 de `x` | valor antigo |
| `--x` | subtrai 1 de `x` | valor novo |

Enquanto o conteúdo é novo, evite misturar vários incrementos na mesma expressão. Separar cada atualização em sua própria linha torna o código e o teste de mesa mais claros.

## Um programa completo

```java
import java.util.Scanner;

public class ContaSimples {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double saldo = 500.0;

        System.out.print("Valor do saque: ");
        double saque = sc.nextDouble();

        if (saque > 0.0 && saque <= saldo) {
            saldo -= saque;
            System.out.printf("Saque realizado. Saldo: %.2f%n", saldo);
        } else {
            System.out.println("Saque invalido.");
        }

        sc.close();
    }
}
```

O `saldo -= saque` só é alcançado depois que a condição confirma que o valor é positivo e cabe no saldo.

## Referências

- [OCPJ21 Study Guide - Chapter 4: Working with Data](../ocpj21-book/ch04.md), seção *Assignment Operators*.
- [Java Language Specification 25 - Assignment Operators](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.26).

---

<div align="center">

⬅️ [A3 · Estrutura condicional if-else](./A3%20-%20Estrutura%20condicional%20if-else.md) &nbsp;·&nbsp; 📂 [Seção 4](./README.md) &nbsp;·&nbsp; [A5 · Estrutura switch-case](./A5%20-%20Estrutura%20switch-case.md) ➡️

</div>
