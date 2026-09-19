# Guia gradual de herança e polimorfismo

## 1. Relação entre tipos

```java
class Employee {
    protected String name;

    Employee(String name) {
        this.name = name;
    }

    double payment() {
        return 1_000.0;
    }
}

class Manager extends Employee {
    Manager(String name) {
        super(name);
    }
}
```

`Manager` é um `Employee`. Construtores não são herdados. O construtor da subclasse precisa iniciar a parte da superclasse, explicitamente com `super(...)` ou por uma chamada implícita a `super()`.

## 2. Ordem de construção

A inicialização da superclasse ocorre antes da inicialização dos campos e do corpo do construtor da subclasse. Uma chamada `this(...)` escolhe outro construtor da mesma classe; `super(...)` escolhe um da superclasse. Um construtor não pode usar ambos como invocações explícitas na mesma cadeia.

No Java 25, corpos flexíveis de construtores são permanentes. Um prólogo pode validar ou preparar argumentos antes de `super(...)`, sem ler a instância em construção:

```java
Manager(String name) {
    String normalized = name.strip();
    super(normalized);
}
```

## 3. Sobrescrita

```java
class Manager extends Employee {
    Manager(String name) { super(name); }

    @Override
    double payment() {
        return 2_000.0;
    }
}
```

Uma sobrescrita preserva a assinatura e usa retorno compatível. Não pode reduzir o acesso nem declarar checked exceptions mais amplas. Métodos `final`, `private` e `static` não são sobrescritos: `private` não é herdado e `static` pode ser ocultado.

## 4. Campos e métodos não se comportam igual

```java
class Parent {
    String label = "parent";
    String label() { return "parent method"; }
}

class Child extends Parent {
    String label = "child";
    @Override String label() { return "child method"; }
}

Parent ref = new Child();
System.out.println(ref.label);   // parent
System.out.println(ref.label()); // child method
```

Campos são escolhidos pelo tipo da referência; métodos de instância sobrescritos são escolhidos pelo objeto em tempo de execução.

## 5. Polimorfismo e casting

```java
Employee employee = new Manager("Ana"); // upcasting implícito
Manager manager = (Manager) employee;    // downcasting explícito
```

O cast não altera o objeto. Ele apenas pede ao compilador que trate a referência como outro tipo compatível. Um cast aceito na compilação pode lançar `ClassCastException` em tempo de execução.

## 6. `instanceof` e padrão de tipo

```java
if (employee instanceof Manager manager) {
    System.out.println(manager.payment());
}
```

A variável de padrão só está em escopo onde o teste garante o tipo. `null instanceof Manager` é `false`.

```java
if (!(employee instanceof Manager manager)) {
    return;
}
System.out.println(manager.payment());
```

O fluxo também prova o tipo após o `return`.

## 7. `final`

- classe `final`: não pode ser estendida;
- método `final`: não pode ser sobrescrito;
- variável `final`: não pode ser reatribuída depois da inicialização.

Uma referência `final` ainda pode apontar para um objeto mutável.

## Revisão OCPJ25

Verifique sempre, nesta ordem:

1. o acesso permite enxergar o membro?
2. a assinatura realmente sobrescreve ou apenas sobrecarrega?
3. o tipo da referência permite a chamada?
4. qual é o tipo real do objeto?
5. o membro é campo, método de instância ou `static`?

## Referências

- [JLS 25 — Superclasses and Subclasses](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.1.4)
- [JLS 25 — Overriding](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.8.1)
- [Java 25 — Flexible Constructor Bodies](https://docs.oracle.com/en/java/javase/25/language/flexible-constructor-bodies.html)
