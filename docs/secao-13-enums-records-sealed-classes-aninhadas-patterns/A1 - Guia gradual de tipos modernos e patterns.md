# Guia gradual de tipos modernos e patterns

## 1. Enums

```java
enum Level {
    LOW(1), MEDIUM(2), HIGH(3);

    private final int weight;

    Level(int weight) { this.weight = weight; }
    int weight() { return weight; }
}
```

Constantes são instâncias criadas quando a classe enum é inicializada. Construtores de enum não são chamados com `new` e não podem ser `public` ou `protected`. Métodos úteis herdados incluem `name()`, `ordinal()` e `values()`; não persista `ordinal`, pois a ordem pode mudar.

Uma constante pode ter corpo próprio e sobrescrever comportamento.

## 2. Records

```java
record Point(int x, int y) { }
```

O record declara componentes, campos `private final`, acessores `x()` e `y()`, construtor canônico e implementações de `equals`, `hashCode` e `toString` baseadas no estado.

Construtor compacto:

```java
record Product(String name, double price) {
    Product {
        name = name.strip();
        if (price < 0) throw new IllegalArgumentException();
    }
}
```

Não atribua `this.name` no compacto; a atribuição implícita ocorre ao final. Records são finais, podem implementar interfaces, ter membros estáticos e métodos de instância, mas não campos de instância adicionais.

## 3. Objetos imutáveis

`final` na referência impede reatribuição, não mutação do objeto referenciado. Para uma classe imutável própria:

- classe `final` ou construção que controle subclasses;
- campos `private final`;
- nenhuma operação mutadora;
- validação na construção;
- cópia defensiva de dados mutáveis na entrada e na saída.

Um record é superficialmente imutável: se um componente for uma lista mutável, a lista ainda pode mudar.

## 4. Hierarquias seladas

```java
sealed interface Payment permits Cash, Card { }
final class Cash implements Payment { }
non-sealed class Card implements Payment { }
```

Subtipos diretos permitidos devem ser `final`, `sealed` ou `non-sealed`. Normalmente ficam no mesmo módulo; em módulo sem nome, no mesmo pacote.

## 5. Classes aninhadas

- `static` nested class: não precisa de instância externa;
- inner member class: está ligada a uma instância externa;
- local class: declarada em bloco;
- anonymous class: declarada e instanciada em uma expressão.

```java
class Outer {
    private int value = 10;

    class Inner {
        int read() { return value; }
    }

    static class Nested { }
}

Outer outer = new Outer();
Outer.Inner inner = outer.new Inner();
Outer.Nested nested = new Outer.Nested();
```

Classes locais e anônimas só capturam variáveis locais finais ou efetivamente finais.

## 6. `switch` como expressão

```java
int days = switch (month) {
    case 2 -> 28;
    case 4, 6, 9, 11 -> 30;
    default -> 31;
};
```

Um bloco usa `yield` para fornecer o valor. Uma expressão `switch` precisa ser exaustiva.

## 7. Type e record patterns

```java
static String describe(Object value) {
    return switch (value) {
        case null -> "null";
        case Point(int x, int y) when x == y -> "diagonal " + x;
        case Point(int x, int y) -> x + "," + y;
        case String text -> text.strip();
        default -> "other";
    };
}
```

Casos dominados por anteriores não compilam. Coloque padrões mais específicos antes dos mais gerais. `when` é uma guarda. Record patterns podem ser aninhados.

## 8. `_` em patterns

```java
case Point(int x, _) -> "x=" + x;
```

`_` ignora um componente e não pode ser lido. Padrões de tipos de referência e record patterns são permanentes. Padrões com tipos primitivos são preview no Java 25 e só devem ser cobrados como preview quando a questão disser que o recurso está habilitado.

## Revisão OCPJ25

Cheque exaustividade, dominância, tratamento de `null`, escopo das variáveis de padrão, restrições de record e permissões da hierarquia selada.

## Referências

- [JLS 25 — Enum Classes](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.9)
- [JLS 25 — Record Classes](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.10)
- [JLS 25 — Sealed Classes](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.1.6)
- [JLS 25 — Patterns](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.30)
