# Encapsulamento, getters e setters

<sub>📚 [Documentação](../README.md) › [Seção 8 · Construtores, palavra this, sobrecarga e encapsulamento](./README.md) › Material 5 de 8</sub>

Na Seção 7, os campos ficaram públicos para facilitar o primeiro contato com objetos. Isso permite estados inválidos:

```java
product.price = -100.0;
product.quantity = -500;
```

**Encapsular** significa ocultar detalhes internos e oferecer operações controladas para usar o objeto.

## Campos privados

```java
public class Product {
    private String name;
    private double price;
    private int quantity;

    public Product(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
}
```

O modificador `private` permite acesso direto apenas dentro da própria classe. Este código deixa de compilar em `Program`:

```java
// product.price = 100.0;
```

## Métodos de consulta

Um getter devolve um dado que a classe decidiu expor:

```java
public String getName() {
    return name;
}

public double getPrice() {
    return price;
}

public int getQuantity() {
    return quantity;
}
```

Uso:

```java
System.out.println(product.getPrice());
```

## Métodos de alteração

Um setter pode validar antes de modificar:

```java
public void setPrice(double price) {
    if (price >= 0.0) {
        this.price = price;
    }
}
```

Para o nome:

```java
public void setName(String name) {
    if (name != null && !name.isBlank()) {
        this.name = name;
    }
}
```

## Nem todo campo precisa de setter

A quantidade do estoque já possui operações com significado:

```java
public void addProducts(int amount) {
    if (amount > 0) {
        quantity += amount;
    }
}

public void removeProducts(int amount) {
    if (amount > 0 && amount <= quantity) {
        quantity -= amount;
    }
}
```

Um `setQuantity(int quantity)` permitiria substituir o estoque sem expressar se houve entrada, saída ou correção. A ausência do setter preserva melhor a regra do domínio.

Também não é necessário criar um campo para todo resultado calculado:

```java
public double totalValueInStock() {
    return price * quantity;
}
```

O total é derivado do estado atual. Guardá-lo em outro campo criaria o risco de valores inconsistentes.

## Encapsulamento não é apenas gerar métodos

Esta classe possui getters e setters, mas quase não protege seu estado:

```java
public void setQuantity(int quantity) {
    this.quantity = quantity;
}
```

O ponto central é controlar as operações válidas, não criar acesso mecânico para todos os campos.

## Validação no construtor

O objeto também precisa começar válido. Como exceções ainda não foram estudadas, usaremos uma regra simples:

```java
public Product(String name, double price, int quantity) {
    this.name = name;
    this.price = price >= 0.0 ? price : 0.0;
    this.quantity = quantity >= 0 ? quantity : 0;
}
```

Mais adiante, o curso poderá rejeitar argumentos inválidos com exceções. Por agora, o importante é perceber que a regra pertence à classe e deve ser aplicada tanto na criação quanto nas alterações.

## Benefícios

- a representação interna pode mudar sem alterar todos os consumidores;
- regras ficam concentradas em um local;
- o objeto evita estados que não fazem sentido;
- nomes de operações expressam intenção.

## Referência

- [JLS 25 - Determining Accessibility](https://docs.oracle.com/javase/specs/jls/se25/html/jls-6.html#jls-6.6.1).

---

<div align="center">

⬅️ [A4 · Ordem de inicialização](./A4%20-%20Ordem%20de%20inicializacao.md) &nbsp;·&nbsp; 📂 [Seção 8](./README.md) &nbsp;·&nbsp; [A6 · Modificadores de acesso e geração pelo Eclipse](./A6%20-%20Modificadores%20de%20acesso%20e%20geracao%20pelo%20Eclipse.md) ➡️

</div>
