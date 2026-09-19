# Construtores

<sub>📚 [Documentação](../README.md) › [Seção 8 · Construtores, palavra this, sobrecarga e encapsulamento](./README.md) › Material 1 de 8</sub>

Na Seção 7, um produto era criado vazio e preenchido em várias instruções:

```java
Product product = new Product();
product.name = "TV";
product.price = 900.00;
product.quantity = 10;
```

Durante esse intervalo, o objeto existe com valores padrão e ainda não representa o produto desejado. Um **construtor** permite fornecer o estado inicial no momento da criação.

## Declarando um construtor

```java
public class Product {
    public String name;
    public double price;
    public int quantity;

    public Product(String productName, double productPrice, int initialQuantity) {
        name = productName;
        price = productPrice;
        quantity = initialQuantity;
    }
}
```

Um construtor:

- tem o mesmo nome da classe;
- não declara tipo de retorno, nem mesmo `void`;
- pode receber parâmetros;
- é selecionado durante a criação com `new`.

Uso:

```java
Product product = new Product("TV", 900.00, 10);
```

## Construtor não é método comum

Este código declara um método chamado `Product`, não um construtor:

```java
public void Product() {
    System.out.println("This is a method");
}
```

O `void` é suficiente para mudar o significado da declaração. Um método pode ser chamado depois; um construtor participa da criação da instância.

## Construtor padrão

Se uma classe não declara nenhum construtor, o compilador fornece um **construtor padrão** sem parâmetros:

```java
public class Product {
    public String name;
}
```

Nesse caso, `new Product()` compila.

Quando qualquer construtor é declarado, o compilador não acrescenta o padrão:

```java
public class Product {
    public String name;

    public Product(String productName) {
        name = productName;
    }
}
```

Agora:

```java
Product first = new Product("TV");
// Product second = new Product(); // não compila
```

Se a classe deve aceitar a criação sem argumentos, o programador precisa declarar esse construtor explicitamente:

```java
public Product() {
}
```

Esse construtor escrito no código é um **construtor sem argumentos**, mas não é o construtor padrão gerado pelo compilador. A distinção é importante na certificação.

## Modificadores permitidos

Um construtor pode usar um modificador de acesso:

```java
public Product(...) { }
private Product(...) { }
```

Construtores não podem ser `static`, `final` ou `abstract`. Esses modificadores não combinam com sua função de inicializar uma nova instância.

## Campos ainda recebem valores padrão

Antes da execução do corpo do construtor, os campos recebem seus valores padrão. Se o construtor não atribuir um campo, ele permanece com esse valor ou com o valor de um inicializador explícito.

```java
public class Item {
    public String name;
    public int quantity;

    public Item(String itemName) {
        name = itemName;
    }
}
```

Após `new Item("Book")`, `quantity` vale `0`.

## Referências

- [JLS 25 - Constructor Declarations](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8).
- [JLS 25 - Default Constructor](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.8.9).

---

<div align="center">

📂 [Seção 8](./README.md) &nbsp;·&nbsp; [A2 · A palavra `this`](./A2%20-%20A%20palavra%20this.md) ➡️

</div>
