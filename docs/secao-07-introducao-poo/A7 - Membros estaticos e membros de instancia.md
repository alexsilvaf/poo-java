# Membros estáticos e membros de instância

<sub>📚 [Documentação](../README.md) › [Seção 7 · Introdução à Programação Orientada a Objetos](./README.md) › Material 7 de 8</sub>

Campos e métodos de instância pertencem aos objetos. Membros `static` pertencem à classe.

## Estado de cada objeto

```java
public class Product {
    public String name;
    public double price;
}
```

Cada `Product` possui seus próprios valores:

```java
Product first = new Product();
first.name = "TV";

Product second = new Product();
second.name = "Notebook";
```

`name` é um campo de instância. Alterá-lo em `first` não altera `second`.

## Um valor compartilhado pela classe

```java
public class Product {
    public static int createdCount;
    public String name;
}
```

Existe uma única variável `createdCount` associada à classe `Product`, não uma cópia para cada produto. O acesso recomendado usa o nome da classe:

```java
Product.createdCount = 2;
System.out.println(Product.createdCount);
```

Java permite acessar um campo estático por uma referência, mas isso confunde o leitor e pode aparecer como armadilha em questões:

```java
Product product = null;
System.out.println(product.createdCount); // compila, mas evite
```

Prefira `Product.createdCount`.

## Métodos `static`

Um método estático é chamado pela classe e não possui um objeto atual implícito. Um exemplo conhecido é `Math.sqrt`.

Podemos criar um utilitário de conversão:

```java
public class CurrencyConverter {
    public static final double IOF = 0.06;

    public static double dollarsToReais(double dollarPrice, double dollars) {
        double basicValue = dollarPrice * dollars;
        return basicValue * (1.0 + IOF);
    }
}
```

Uso:

```java
double amount = CurrencyConverter.dollarsToReais(5.20, 100.00);
System.out.printf("Amount to be paid: %.2f%n", amount);
```

`IOF` é uma constante da classe:

- `static`: existe uma vez para a classe;
- `final`: recebe valor uma vez;
- nome em maiúsculas: convenção para constantes.

## Contexto estático

Um método `static` não pode acessar diretamente um campo de instância:

```java
public class Account {
    public double balance;

    public static void printBalance() {
        // System.out.println(balance); // não compila
    }
}
```

Qual saldo seria usado se nenhum objeto `Account` foi indicado? O acesso precisa ocorrer por uma referência recebida ou criada:

```java
public static void printBalance(Account account) {
    System.out.println(account.balance);
}
```

O caminho inverso é permitido: um método de instância pode acessar membros estáticos da classe.

## Inicialização estática básica

Um campo estático pode receber valor na própria declaração:

```java
public static final double PI = 3.14159;
```

Também existe o bloco inicializador estático:

```java
public class Configuration {
    public static String mode;

    static {
        mode = "training";
        System.out.println("Configuration loaded");
    }
}
```

O bloco é executado quando a classe é inicializada pela JVM. Ele não é executado uma vez por objeto. Nesta seção, use-o apenas para reconhecer a sintaxe; regras completas de inicialização aparecerão na Seção 8.

## Como decidir

Pergunte: a informação ou operação depende de um objeto específico?

- sim: membro de instância;
- não, representa algo compartilhado ou uma operação da classe: pode ser `static`.

Evite transformar tudo em `static` apenas para facilitar a chamada pelo `main`. Isso eliminaria justamente o estado independente dos objetos.

## Referências

- [JLS 25 - Static Fields](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.3.1.1).
- [JLS 25 - Static Methods](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.3.2).
- [JLS 25 - Static Initializers](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.7).

---

<div align="center">

⬅️ [A6 · Problema de exemplo: estoque de produtos](./A6%20-%20Problema%20de%20exemplo%20estoque%20de%20produtos.md) &nbsp;·&nbsp; 📂 [Seção 7](./README.md) &nbsp;·&nbsp; [A8 · A certificação OCP Java SE 25 e esta seção](./A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md) ➡️

</div>
