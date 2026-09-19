# Problema de exemplo: estoque de produtos

<sub>📚 [Documentação](../README.md) › [Seção 7 · Introdução à Programação Orientada a Objetos](./README.md) › Material 6 de 8</sub>

Vamos reunir atributos e métodos de instância em uma classe que representa um produto em estoque.

O programa deve:

1. ler nome, preço e quantidade inicial;
2. mostrar os dados e o valor total em estoque;
3. adicionar produtos;
4. remover produtos;
5. mostrar o estado após cada operação.

## Classe `Product`

Crie `Product.java`:

```java
public class Product {
    public String name;
    public double price;
    public int quantity;

    public double totalValueInStock() {
        return price * quantity;
    }

    public void addProducts(int amount) {
        quantity += amount;
    }

    public void removeProducts(int amount) {
        quantity -= amount;
    }

    @Override
    public String toString() {
        return name
                + ", $ "
                + String.format("%.2f", price)
                + ", "
                + quantity
                + " units, Total: $ "
                + String.format("%.2f", totalValueInStock());
    }
}
```

Observe as responsabilidades:

- `totalValueInStock()` consulta o estado e devolve um resultado;
- `addProducts()` altera a quantidade;
- `removeProducts()` altera a quantidade;
- `toString()` produz uma descrição, sem alterar o estado.

## Programa principal

Crie `Program.java`:

```java
import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        Product product = new Product();

        System.out.println("Enter product data:");
        System.out.print("Name: ");
        product.name = sc.nextLine();
        System.out.print("Price: ");
        product.price = sc.nextDouble();
        System.out.print("Quantity in stock: ");
        product.quantity = sc.nextInt();

        System.out.println("Product data: " + product);

        System.out.print("Enter the number of products to be added in stock: ");
        int quantity = sc.nextInt();
        product.addProducts(quantity);
        System.out.println("Updated data: " + product);

        System.out.print("Enter the number of products to be removed from stock: ");
        quantity = sc.nextInt();
        product.removeProducts(quantity);
        System.out.println("Updated data: " + product);

        sc.close();
    }
}
```

## A variável local e o campo têm papéis diferentes

Neste trecho:

```java
int quantity = sc.nextInt();
product.addProducts(quantity);
```

`quantity` é uma variável local do `main`. Já `product.quantity` é um campo do objeto. O argumento fornece um valor ao parâmetro `amount`; o método usa esse valor para atualizar o campo.

## Ainda existe uma fragilidade

Qualquer trecho pode executar:

```java
product.quantity = -500;
```

O acesso direto impede a classe de proteger suas regras. Isso é intencional nesta etapa: primeiro observamos objetos e métodos; na Seção 8, campos `private`, construtores e métodos de acesso resolverão essa fragilidade.

## Exercício

Crie uma classe `Employee` com:

- campos `name`, `grossSalary` e `tax`;
- método `netSalary()`;
- método `increaseSalary(double percentage)`;
- `toString()` com nome e salário líquido.

Use somente os recursos apresentados até aqui. Não crie construtores nem campos privados ainda.

---

<div align="center">

⬅️ [A5 · `Object` e `toString`](./A5%20-%20Object%20e%20toString.md) &nbsp;·&nbsp; 📂 [Seção 7](./README.md) &nbsp;·&nbsp; [A7 · Membros estáticos e membros de instância](./A7%20-%20Membros%20estaticos%20e%20membros%20de%20instancia.md) ➡️

</div>
