# `Object` e `toString`

<sub>📚 [Documentação](../README.md) › [Seção 7 · Introdução à Programação Orientada a Objetos](./README.md) › Material 5 de 8</sub>

Toda classe possui `Object` como ancestral, direta ou indiretamente. Ainda não estudaremos herança; por enquanto, basta reconhecer que uma classe comum recebe alguns métodos básicos definidos por `Object`.

Um deles é `toString()`.

## A representação padrão

Considere:

```java
Product product = new Product();
product.name = "TV";
product.price = 900.00;
product.quantity = 10;

System.out.println(product);
```

Sem uma implementação própria, a saída costuma ter esta forma:

```text
Product@2f92e0f4
```

Ela identifica o tipo e fornece uma representação relacionada ao hash do objeto, mas não mostra os dados relevantes do produto. O sufixo não deve ser interpretado como endereço de memória.

## Fornecendo uma representação útil

```java
public class Product {
    public String name;
    public double price;
    public int quantity;

    @Override
    public String toString() {
        return name
                + ", $ "
                + String.format("%.2f", price)
                + ", "
                + quantity
                + " units";
    }
}
```

Agora:

```java
System.out.println(product);
```

pode mostrar:

```text
TV, $ 900.00, 10 units
```

## O que `@Override` informa

`@Override` é uma anotação. Ela pede ao compilador que confirme que o método substitui um método existente no ancestral. Se o nome for digitado incorretamente, o erro é percebido na compilação:

```java
@Override
public String tostring() { // não substitui toString
    return name;
}
```

O estudo geral de anotações e sobrescrita pertence a seções posteriores. Aqui usamos `@Override` como uma verificação de segurança.

## Conversão implícita para texto

Em alguns contextos, Java chama `toString()` automaticamente:

```java
System.out.println(product);
String message = "Product: " + product;
```

Essas expressões utilizam a representação textual do objeto. Também é possível chamar o método explicitamente:

```java
String text = product.toString();
```

Se a referência for `null`, há uma diferença:

```java
Product product = null;
System.out.println(product);       // imprime null
// product.toString();             // NullPointerException
```

## `toString` não altera o objeto

Uma boa implementação de `toString()` apenas descreve o estado atual. Ela não deve acrescentar itens ao estoque, mudar preço ou realizar outras alterações inesperadas.

## O que fica para depois

`Object` também define métodos como `equals()` e `hashCode()`. A comparação lógica de objetos e o contrato entre esses métodos serão ensinados quando houver mais tipos e coleções para motivá-los. Nesta aula, `equals` continua sendo usado apenas para conteúdos como `String`, conforme a Seção 6.

## Referências

- [API Java 25 - Object](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html).
- [API Java 25 - Object.toString](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html#toString()).

---

<div align="center">

⬅️ [A4 · Referências, stack, heap e coleta de lixo](./A4%20-%20Referencias%20stack%20heap%20e%20coleta%20de%20lixo.md) &nbsp;·&nbsp; 📂 [Seção 7](./README.md) &nbsp;·&nbsp; [A6 · Problema de exemplo: estoque de produtos](./A6%20-%20Problema%20de%20exemplo%20estoque%20de%20produtos.md) ➡️

</div>
