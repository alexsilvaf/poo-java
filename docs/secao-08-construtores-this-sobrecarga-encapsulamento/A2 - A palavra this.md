# A palavra `this`

<sub>📚 [Documentação](../README.md) › [Seção 8 · Construtores, palavra this, sobrecarga e encapsulamento](./README.md) › Material 2 de 8</sub>

Dentro de um método ou construtor de instância, `this` representa a instância atual: o objeto no qual aquele código está sendo executado.

## Nomes iguais para campo e parâmetro

É comum dar aos parâmetros os mesmos nomes dos campos:

```java
public class Product {
    public String name;
    public double price;
    public int quantity;

    public Product(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
}
```

Em `this.name = name`:

- `this.name` é o campo do objeto atual;
- `name` é o parâmetro mais próximo.

Sem `this`, a instrução abaixo apenas atribuiria o parâmetro a ele mesmo:

```java
name = name;
```

O campo continuaria com seu valor anterior.

## Sombreamento de nomes

Quando uma variável local ou um parâmetro tem o mesmo nome de um campo, o nome mais próximo **sombreia** o campo. `this.campo` torna explícito que queremos o membro da instância.

```java
public void setPrice(double price) {
    this.price = price;
}
```

Não é obrigatório usar `this` quando não há ambiguidade:

```java
public double totalValueInStock() {
    return price * quantity;
}
```

O código abaixo também compila, mas costuma ser mais verboso:

```java
public double totalValueInStock() {
    return this.price * this.quantity;
}
```

## Chamando outro método da mesma instância

```java
public String label() {
    return this.name + ": " + this.totalValueInStock();
}
```

O `this.` é opcional nessas chamadas quando não existe ambiguidade:

```java
return name + ": " + totalValueInStock();
```

## Passando a instância atual

`this` também pode ser fornecido como argumento:

```java
public void print() {
    Printer.printProduct(this);
}
```

Para compreender a ideia, basta saber que o argumento é uma referência ao objeto atual. O projeto da classe `Printer` não é necessário nesta etapa.

## Onde `this` não existe

Um contexto `static` não possui instância atual:

```java
public static void show() {
    // System.out.println(this); // não compila
}
```

Isso explica por que o `main` precisa de uma variável como `product` para acessar membros de instância.

## `this` e `this(...)`

Não confunda:

- `this` é uma expressão que representa a instância atual;
- `this(...)` é uma invocação de outro construtor da mesma classe.

O encadeamento com `this(...)` será apresentado depois da sobrecarga, na próxima aula.

## Referência

- [JLS 25 - The `this` Expression](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.8.3).

---

<div align="center">

⬅️ [A1 · Construtores](./A1%20-%20Construtores.md) &nbsp;·&nbsp; 📂 [Seção 8](./README.md) &nbsp;·&nbsp; [A3 · Sobrecarga e encadeamento de construtores](./A3%20-%20Sobrecarga%20e%20encadeamento%20de%20construtores.md) ➡️

</div>
