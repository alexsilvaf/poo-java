# A certificação OCP Java SE 25 e esta seção

<sub>📚 [Documentação](../README.md) › [Seção 8 · Construtores, palavra this, sobrecarga e encapsulamento](./README.md) › Material 8 de 8</sub>

Esta seção amplia o domínio de orientação a objetos da OCP Java SE 25. As questões costumam combinar declaração, sobrecarga, acesso e ordem de inicialização.

## Pontos que precisam estar consolidados

- um construtor possui o nome da classe e não declara retorno;
- o compilador fornece um construtor padrão somente quando nenhum construtor foi declarado;
- um construtor sem argumentos escrito pelo programador não é o construtor padrão implícito;
- `this.campo` acessa o campo da instância atual;
- `this(...)` invoca outro construtor da mesma classe;
- sobrecarga exige listas de parâmetros diferentes;
- retorno e nomes dos parâmetros não fazem parte da assinatura usada para diferenciar sobrecargas;
- campos recebem valores padrão antes dos inicializadores e do construtor;
- inicializadores de instância executam na ordem textual;
- membros `private` são acessíveis somente na própria classe;
- uma classe de topo só pode ser `public` ou ter acesso de pacote;
- no Java 25, os corpos flexíveis de construtores permitem um prólogo restrito antes da invocação explícita de construtor.

## Questões de leitura de código

### 1. Método ou construtor?

```java
class Book {
    void Book() { }
}
```

`Book()` é um método porque declara `void`. Como nenhum construtor foi declarado, o compilador ainda fornece um construtor padrão.

### 2. Perda do construtor padrão

```java
class Book {
    Book(String title) { }
}

// Book book = new Book();
```

A criação sem argumentos não compila. Ao declarar `Book(String)`, a classe deixou de receber o construtor padrão.

### 3. Sombreamento

```java
class Box {
    int value;

    Box(int value) {
        value = value;
    }
}
```

Depois de `new Box(9)`, o campo `value` vale `0`. A instrução modificou apenas o parâmetro. A correção é `this.value = value`.

### 4. Assinaturas repetidas

```java
void run(int value) { }
// int run(int number) { return number; }
```

A segunda declaração não compila: nomes de parâmetros e tipo de retorno não diferenciam a assinatura.

### 5. Resolução simples

```java
static void show(int value)  { System.out.print("int"); }
static void show(long value) { System.out.print("long"); }

show(3);
show(3L);
```

Saída: `intlong`. Em cada chamada existe uma correspondência exata.

### 6. Encadeamento

```java
class Point {
    int x;
    int y;

    Point() {
        this(1, 2);
    }

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```

Depois de `new Point()`, `x` vale `1` e `y` vale `2`.

### 7. Ordem textual

```java
class Sequence {
    int a = 1;

    {
        a = 2;
    }

    int b = a;

    Sequence() {
        a = 3;
    }
}
```

Após a construção, `a` vale `3` e `b` vale `2`.

### 8. Inicialização estática e de instância

```java
class Demo {
    static { System.out.print("S"); }
    { System.out.print("I"); }
    Demo() { System.out.print("C"); }
}

new Demo();
new Demo();
```

Considerando a primeira inicialização da classe nesse ponto, a saída é `SICIC`.

### 9. Acesso de pacote

```java
class Service {
    void execute() { }
}
```

A classe e o método não são `private`; ambos possuem acesso de pacote.

### 10. Classe de topo

```java
// protected class Utility { }
```

Não compila. `protected` e `private` não são permitidos em classes de topo.

### 11. Campo `final`

```java
class Ticket {
    private final int number;

    Ticket(int number) {
        this.number = number;
    }
}
```

O campo em branco `final` recebe valor no construtor. Uma segunda atribuição não seria permitida.

### 12. Corpo flexível de construtor (Java 25)

```java
class Name {
    String value;

    Name(String value) {
        String normalized = value.strip();
        this(normalized, true);
    }

    Name(String value, boolean normalized) {
        this.value = value;
    }
}
```

Compila no Java 25: a variável local antes de `this(...)` é permitida porque não acessa a instância em construção. Em versões anteriores ao Java 25, esse código não compila sem recursos de preview.

## Armadilhas frequentes

- chamar todo construtor sem argumentos de “construtor padrão”;
- escrever um tipo de retorno e acreditar que declarou um construtor;
- criar sobrecarga mudando apenas o retorno;
- formar um ciclo entre chamadas `this(...)`;
- confundir `this` com `this(...)`;
- supor que o bloco estático executa para cada objeto;
- tratar acesso de pacote como se fosse `protected`;
- ignorar as restrições do prólogo nos corpos flexíveis de construtores, como ler a instância atual antes de `this(...)`.

## O que continua planejado

Esta seção não completa o domínio de orientação a objetos. Ainda faltam:

- ordem de construção em hierarquias e chamadas `super(...)`;
- sobrescrita, polimorfismo e casting de referências;
- classes abstratas e interfaces;
- `equals`, `hashCode` e imutabilidade de objetos próprios;
- enums, records, tipos selados e classes aninhadas;
- sobrecarga com boxing, unboxing, varargs e genéricos.

Esses tópicos permanecem registrados na matriz global e devem aparecer somente após seus pré-requisitos.

## Referências

- [JLS 25 - Classes](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html).
- [JLS 25 - Access Control](https://docs.oracle.com/javase/specs/jls/se25/html/jls-6.html#jls-6.6).
- [Java 25 Language Guide - Flexible Constructor Bodies](https://docs.oracle.com/en/java/javase/25/language/flexible-constructor-bodies.html).

---

<div align="center">

⬅️ [A7 · Prática integrada: conta bancária](./A7%20-%20Pratica%20integrada%20conta%20bancaria.md) &nbsp;·&nbsp; 📂 [Seção 8](./README.md)

</div>
