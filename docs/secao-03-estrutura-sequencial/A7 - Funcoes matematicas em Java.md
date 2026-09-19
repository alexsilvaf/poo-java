# Funções matemáticas em Java

<sub>📚 [Documentação](../README.md) › [Seção 3 · Estrutura sequencial](./README.md) › Material 7 de 8</sub>

Java não tem operador de potenciação nem de raiz quadrada. Essas operações ficam na classe `java.lang.Math`, que é importada automaticamente e não precisa de `import`.

## Como a classe `Math` é usada

As operações são chamadas pelo nome `Math`, seguido de ponto e do nome desejado:

```java
double raiz = Math.sqrt(81.0);   // 9.0
```

Neste ponto, basta reconhecer o formato `Math.operacao(valor)`. Métodos estáticos, objetos e construtores serão explicados nas seções de orientação a objetos.

## Os métodos mais usados

| Método | O que faz | Exemplo | Resultado |
|---|---|---|---|
| `Math.sqrt(x)` | raiz quadrada | `Math.sqrt(81.0)` | `9.0` |
| `Math.cbrt(x)` | raiz cúbica | `Math.cbrt(27.0)` | `3.0` |
| `Math.pow(x, y)` | `x` elevado a `y` | `Math.pow(2, 10)` | `1024.0` |
| `Math.abs(x)` | valor absoluto | `Math.abs(-7)` | `7` |
| `Math.max(a, b)` | o maior dos dois | `Math.max(3, 9)` | `9` |
| `Math.min(a, b)` | o menor dos dois | `Math.min(3, 9)` | `3` |
| `Math.round(x)` | arredonda para o inteiro mais próximo | `Math.round(3.6)` | `4` |
| `Math.floor(x)` | arredonda para baixo | `Math.floor(3.9)` | `3.0` |
| `Math.ceil(x)` | arredonda para cima | `Math.ceil(3.1)` | `4.0` |
| `Math.random()` | decimal aleatório em `[0.0, 1.0)` | — | varia |

Constantes: `Math.PI` (3.141592653589793) e `Math.E` (2.718281828459045).

## Detalhes que importam

### `pow` e `sqrt` sempre devolvem `double`

```java
double area = Math.pow(5, 2);       // 25.0
int lado = (int) Math.sqrt(16);     // 4 — precisa de casting para virar int
```

Mesmo `Math.pow(2, 3)`, cujo resultado é exato, devolve `8.0` e não `8`.

### `round`, `floor` e `ceil` devolvem tipos diferentes

```java
long arredondado = Math.round(3.6);   // long
double piso = Math.floor(3.9);        // double
double teto = Math.ceil(3.1);         // double
```

`Math.round(double)` devolve `long`; `Math.round(float)` devolve `int`. `floor` e `ceil` devolvem `double` — eles arredondam o valor, mas não mudam o tipo.

### `round` arredonda para cima no meio do caminho

```java
System.out.println(Math.round(2.5));    // 3
System.out.println(Math.round(-2.5));   // -2   — e não -3
```

`Math.round(x)` é definido como `floor(x + 0.5)`. Para valores negativos exatamente no meio, isso puxa o resultado para cima — ou seja, para mais perto do zero. É uma pegadinha recorrente em provas.

### `abs` do menor `int` possível

```java
System.out.println(Math.abs(Integer.MIN_VALUE));   // -2147483648
```

Não existe `int` positivo capaz de representar esse valor, e o resultado permanece negativo. Não há exceção, apenas um valor errado.

## Números aleatórios

```java
double sorteio = Math.random();              // 0.0 <= sorteio < 1.0
int dado = (int) (Math.random() * 6) + 1;    // 1 a 6
```

A fórmula geral para um inteiro entre `min` e `max`, inclusive:

```java
int valor = (int) (Math.random() * (max - min + 1)) + min;
```

Outras formas de gerar números aleatórios serão apresentadas quando o curso aprofundar classes e objetos. Nesta seção, `Math.random()` é suficiente.

## Um programa completo

```java
import java.util.Locale;
import java.util.Scanner;

public class Distancia {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);   // ponto no lugar da vírgula
        Scanner sc = new Scanner(System.in);

        // 1. ENTRADA
        System.out.print("x1, y1: ");
        double x1 = sc.nextDouble();
        double y1 = sc.nextDouble();

        System.out.print("x2, y2: ");
        double x2 = sc.nextDouble();
        double y2 = sc.nextDouble();

        // 2. PROCESSAMENTO
        double distancia = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));

        // 3. SAÍDA
        System.out.printf("Distancia: %.3f%n", distancia);   // três casas decimais

        sc.close();
    }
}
```

```
x1, y1: 0 0
x2, y2: 3 4
Distancia: 5.000
```

## Trigonometria e logaritmos

Existem também `Math.sin`, `Math.cos`, `Math.tan`, `Math.log` (logaritmo natural), `Math.log10` e `Math.exp`. As funções trigonométricas trabalham em **radianos**, não em graus:

```java
double graus = 90;
double radianos = Math.toRadians(graus);
System.out.println(Math.sin(radianos));   // 1.0
```

## Referências

- [OCPJ21 Study Guide — Chapter 4: Working with Data](../ocpj21-book/ch04.md), seção *The Math API*.

---

<div align="center">

⬅️ [A6 · Entrada de dados em Java](./A6%20-%20Entrada%20de%20dados%20em%20Java.md) &nbsp;·&nbsp; 📂 [Seção 3](./README.md) &nbsp;·&nbsp; [A8 · A certificação OCP Java SE 25 e esta seção](./A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md) ➡️

</div>
