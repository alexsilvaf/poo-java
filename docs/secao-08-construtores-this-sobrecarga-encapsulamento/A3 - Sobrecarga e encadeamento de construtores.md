# Sobrecarga e encadeamento de construtores

<sub>📚 [Documentação](../README.md) › [Seção 8 · Construtores, palavra this, sobrecarga e encapsulamento](./README.md) › Material 3 de 8</sub>

**Sobrecarga** é a declaração de métodos ou construtores com o mesmo nome e listas de parâmetros diferentes.

## Sobrecarga de métodos

```java
public class Calculator {
    public static int max(int a, int b) {
        return a > b ? a : b;
    }

    public static double max(double a, double b) {
        return a > b ? a : b;
    }
}
```

Chamadas:

```java
System.out.println(Calculator.max(4, 7));       // versão int
System.out.println(Calculator.max(4.5, 3.2));   // versão double
```

O compilador escolhe a versão aplicável a partir dos argumentos.

## O que precisa mudar

A lista de parâmetros pode mudar em:

- quantidade;
- tipos;
- ordem dos tipos.

```java
void show(int value) { }
void show(double value) { }
void show(String text, int count) { }
void show(int count, String text) { }
```

Trocar apenas o nome do parâmetro não cria outra assinatura:

```java
void show(int value) { }
// void show(int number) { } // mesma assinatura; não compila
```

Trocar apenas o retorno também não é permitido:

```java
int convert(int value) { return value; }
// double convert(int value) { return value; } // não compila
```

## Conversões simples na escolha

Quando não existe correspondência exata, uma conversão de alargamento pode tornar uma versão aplicável:

```java
static void print(long value) {
    System.out.println("long");
}

print(5); // int pode ser alargado para long
```

Se houver uma correspondência exata e outra por alargamento, a exata é mais específica:

```java
static void print(int value)  { System.out.println("int"); }
static void print(long value) { System.out.println("long"); }

print(5); // int
```

Autoboxing, varargs e combinações com genéricos serão retomados quando esses pré-requisitos forem ensinados.

## Sobrecarga de construtores

```java
public class Product {
    public String name;
    public double price;
    public int quantity;

    public Product() {
    }

    public Product(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public Product(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
}
```

Cada expressão seleciona um construtor:

```java
Product first = new Product();
Product second = new Product("TV", 900.00);
Product third = new Product("TV", 900.00, 10);
```

## Evitando repetição com `this(...)`

Um construtor pode invocar outro construtor da mesma classe:

```java
public Product() {
    this("Unnamed", 0.0, 0);
}

public Product(String name, double price) {
    this(name, price, 0);
}

public Product(String name, double price, int quantity) {
    this.name = name;
    this.price = price;
    this.quantity = quantity;
}
```

Na forma tradicional, `this(...)` aparece antes das demais instruções do construtor. O encadeamento deve terminar em um construtor que inicialize o objeto; ciclos não compilam.

```java
// Product() { this("Unnamed"); }
// Product(String name) { this(); } // ciclo: não compila
```

## Java 25: corpo flexível de construtor

No Java 25, **Flexible Constructor Bodies** (JEP 513) é um recurso final da linguagem: instruções que não acessam a instância em construção podem aparecer antes de `this(...)` ou `super(...)`.

```java
public Product(String name) {
    String normalizedName = name.strip();
    this(normalizedName, 0.0, 0);
}
```

Esse trecho pertence ao **prólogo** do construtor. Ele pode trabalhar com parâmetros e variáveis locais, mas não pode ler a instância atual antes da invocação explícita.

Como o recurso é final, não é preciso `--enable-preview`. Basta compilar no nível 25 uma classe `Product` e um `Program` que a utiliza:

```text
javac --release 25 Product.java Program.java
java Program
```

O restante da seção não depende desse recurso. A regra tradicional é suficiente para os primeiros projetos e para versões anteriores de Java.

## Referências

- [JLS 25 - Overloading](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.9).
- [JLS 25 - Constructor Overloading](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.8).
- [Java 25 Language Guide - Flexible Constructor Bodies](https://docs.oracle.com/en/java/javase/25/language/flexible-constructor-bodies.html).

---

<div align="center">

⬅️ [A2 · A palavra `this`](./A2%20-%20A%20palavra%20this.md) &nbsp;·&nbsp; 📂 [Seção 8](./README.md) &nbsp;·&nbsp; [A4 · Ordem de inicialização](./A4%20-%20Ordem%20de%20inicializacao.md) ➡️

</div>
