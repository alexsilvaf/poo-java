# Guia gradual de abstração, interfaces e `Object`

## 1. Classe abstrata

```java
abstract class Shape {
    private final String color;

    protected Shape(String color) {
        this.color = color;
    }

    public String getColor() { return color; }
    public abstract double area();
}
```

Uma classe abstrata não pode ser instanciada, mas pode ter campos, construtores e métodos concretos. Uma subclasse concreta deve implementar todos os métodos abstratos herdados.

## 2. Interfaces

```java
interface Taxable {
    double tax();

    default double total(double base) {
        return base + tax();
    }

    static boolean valid(double value) {
        return value >= 0.0;
    }
}
```

Campos declarados em interfaces são implicitamente `public static final`. Métodos abstratos são implicitamente `public abstract`. Métodos `default` e `static` têm corpo; métodos `private` auxiliam outros métodos da própria interface.

```java
class Invoice implements Taxable {
    private final double value;
    Invoice(double value) { this.value = value; }
    @Override public double tax() { return value * 0.1; }
}
```

Uma classe pode implementar várias interfaces, mas estender apenas uma classe.

## 3. Conflitos de `default`

```java
interface A { default String name() { return "A"; } }
interface B { default String name() { return "B"; } }

class C implements A, B {
    @Override
    public String name() {
        return A.super.name() + B.super.name();
    }
}
```

A classe deve resolver defaults incompatíveis. Um método concreto herdado de classe tem precedência sobre defaults de interface.

## 4. Interface funcional

Uma interface funcional possui exatamente um método abstrato, desconsiderando métodos de `Object` e permitindo métodos `default`, `static` e `private`.

```java
@FunctionalInterface
interface Formatter {
    String format(String value);
}
```

A anotação é uma verificação, não a causa da funcionalidade. Lambdas serão estudadas na Seção 16.

## 5. `Object`

Toda classe herda de `Object`. Métodos centrais:

- `toString()`: representação textual;
- `equals(Object)`: igualdade lógica;
- `hashCode()`: valor usado por estruturas baseadas em hash;
- `getClass()`: classe de execução.

## 6. Contrato de igualdade

```java
final class ProductCode {
    private final String value;

    ProductCode(String value) { this.value = value; }

    @Override
    public boolean equals(Object object) {
        if (this == object) return true;
        if (!(object instanceof ProductCode other)) return false;
        return value.equals(other.value);
    }

    @Override
    public int hashCode() {
        return value.hashCode();
    }
}
```

`equals` deve ser reflexivo, simétrico, transitivo, consistente e devolver `false` para `null`. Objetos iguais precisam ter o mesmo hash code; hashes iguais não obrigam igualdade.

## 7. Abstração ou interface?

Use classe abstrata quando tipos relacionados compartilham estado e implementação base. Use interface para expressar capacidade ou contrato que tipos diferentes podem implementar. A prova cobra as regras da linguagem; projetos reais também exigem clareza do modelo.

## Revisão OCPJ25

- métodos de interface implementados devem ser `public`;
- uma classe abstrata pode não implementar tudo;
- uma classe concreta não pode deixar método abstrato pendente;
- `static` de interface é chamado pelo nome da interface e não é herdado como método de instância;
- `equals` recebe `Object`, não o tipo específico, quando realmente sobrescreve.

## Referências

- [JLS 25 — Abstract Classes](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.1.1.1)
- [JLS 25 — Interfaces](https://docs.oracle.com/javase/specs/jls/se25/html/jls-9.html)
- [API Java 25 — Object](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/Object.html)
