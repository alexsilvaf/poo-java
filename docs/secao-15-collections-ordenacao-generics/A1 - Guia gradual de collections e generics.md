# Guia gradual de collections e generics

## 1. Escolhendo uma coleção

- `List`: sequência indexada, aceita repetição;
- `Set`: elementos distintos;
- `Map`: pares chave/valor;
- `Deque`: operações eficientes nas duas extremidades;
- sorted/navigable variants: ordem de comparação;
- sequenced interfaces: primeiro, último e visão reversa.

```java
List<String> list = new ArrayList<>();
Set<String> set = new HashSet<>();
Map<String, Integer> map = new HashMap<>();
Deque<String> deque = new ArrayDeque<>();
```

## 2. Operações e sobrecargas perigosas

```java
List<Integer> values = new ArrayList<>(List.of(10, 20, 30));
values.remove(1);                  // remove índice 1
values.remove(Integer.valueOf(30)); // remove o objeto 30
```

Collections criadas por `List.of`, `Set.of` e `Map.of` são não modificáveis e rejeitam `null`. `Arrays.asList` tem tamanho fixo e é apoiada pelo array. `new ArrayList<>(...)` cria uma lista mutável independente.

## 3. Hash e árvore

`HashSet` e `HashMap` dependem do contrato `equals`/`hashCode`. `TreeSet` e `TreeMap` dependem de ordem natural ou `Comparator`; comparação igual a zero determina duplicidade para a árvore.

## 4. Ordenação

```java
record Product(String name, double price) implements Comparable<Product> {
    @Override
    public int compareTo(Product other) {
        return name.compareTo(other.name);
    }
}

Comparator<Product> byPrice =
        Comparator.comparingDouble(Product::price)
                  .thenComparing(Product::name);
```

`Comparable` define ordem natural no tipo. `Comparator` define ordens externas. Contratos quebrados podem produzir resultados errados em coleções ordenadas e buscas binárias.

## 5. Collections sequenciadas

Java moderno fornece `SequencedCollection`, `SequencedSet` e `SequencedMap` para operações como `getFirst`, `getLast`, `addFirst`, `addLast` e `reversed`, conforme a capacidade da implementação.

```java
SequencedCollection<String> names = new ArrayList<>();
names.addFirst("Ana");
names.addLast("Caio");
System.out.println(names.reversed());
```

Uma implementação pode rejeitar uma operação opcional com `UnsupportedOperationException`.

## 6. Tipos genéricos

```java
class Box<T> {
    private T value;
    T get() { return value; }
    void set(T value) { this.value = value; }
}

static <T> T first(List<T> values) {
    return values.getFirst();
}
```

`List<Integer>` não é subtipo de `List<Number>`. Generics são invariantes.

## 7. Wildcards: PECS

```java
static double sum(List<? extends Number> values) { // producer
    double total = 0;
    for (Number value : values) total += value.doubleValue();
    return total;
}

static void addIntegers(List<? super Integer> target) { // consumer
    target.add(1);
}
```

Producer Extends, Consumer Super. Em `? extends Number`, leia como `Number`, mas não adicione valores específicos. Em `? super Integer`, adicione `Integer`, mas leia apenas como `Object`.

## 8. Erasure e restrições

Em execução, argumentos de tipo normalmente são apagados. Consequências:

- não criar `new T()` diretamente;
- não criar arrays genéricos comuns;
- não usar primitivos como argumento de tipo;
- não sobrecarregar métodos que tenham a mesma erasure;
- `instanceof List<String>` não é permitido; use `instanceof List<?>`.

## Revisão OCPJ25

Cheque mutabilidade, aceitação de `null`, ordem, duplicidade, sobrecarga de `remove`, contrato de comparação, invariância e direção dos wildcards.

## Referências

- [API Java 25 — Collections Framework](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/doc-files/coll-overview.html)
- [JLS 25 — Type Arguments](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.5.1)
- [API Java 25 — SequencedCollection](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/SequencedCollection.html)
