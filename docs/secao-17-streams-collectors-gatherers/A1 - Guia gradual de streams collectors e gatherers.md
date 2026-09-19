# Guia gradual de streams, collectors e gatherers

## 1. Pipeline

```java
List<String> result = names.stream()
        .filter(name -> !name.isBlank())
        .map(String::toUpperCase)
        .sorted()
        .toList();
```

Fonte → operações intermediárias → operação terminal. Intermediárias são lazy e devolvem outro stream. Um stream consumido não pode ser reutilizado.

## 2. Criação

```java
Stream.of("a", "b");
Stream.empty();
list.stream();
Arrays.stream(array);
Stream.iterate(1, n -> n + 1).limit(5);
Stream.generate(Math::random).limit(3);
```

Streams infinitas precisam de curto-circuito ou limite antes de operações que exigem todos os elementos.

## 3. Intermediárias

- `filter`: mantém elementos;
- `map`: transforma um por um;
- `flatMap`: transforma e achata streams internas;
- `distinct`: remove duplicados por `equals`/`hashCode`;
- `sorted`: ordena;
- `limit`/`skip`: recortam;
- `peek`: observa, não deve sustentar lógica essencial.

```java
List<String> words = lines.stream()
        .flatMap(line -> line.lines())
        .flatMap(line -> Arrays.stream(line.split("\\s+")))
        .distinct()
        .toList();
```

## 4. Terminais e `Optional`

```java
long count = stream.count();
boolean any = stream.anyMatch(predicate);
Optional<String> first = stream.findFirst();
stream.forEach(System.out::println);
```

`findFirst`, `findAny`, `min`, `max` e algumas reduções devolvem `Optional`. Não chame `get()` sem garantir presença; use `orElse`, `orElseGet`, `orElseThrow`, `ifPresent` ou transformações.

## 5. Streams primitivas

```java
int total = IntStream.rangeClosed(1, 5).sum();
OptionalDouble average = values.stream()
        .mapToInt(String::length)
        .average();
```

`IntStream`, `LongStream` e `DoubleStream` evitam boxing e oferecem `sum`, `average`, `summaryStatistics`. Use `boxed()` para voltar a `Stream<Integer>` e métodos `mapTo...` para conversões.

## 6. Redução

```java
int sum = numbers.stream().reduce(0, Integer::sum);
Optional<Integer> max = numbers.stream().reduce(Integer::max);
```

Em execução paralela, identidade, acumulador e combinador precisam ser associativos e compatíveis. Efeitos colaterais em estado compartilhado tornam o resultado frágil.

## 7. Collectors

```java
Map<Integer, List<String>> byLength = names.stream()
        .collect(Collectors.groupingBy(String::length));

Map<Boolean, List<String>> partition = names.stream()
        .collect(Collectors.partitioningBy(String::isBlank));

String joined = names.stream()
        .collect(Collectors.joining(", "));
```

Conheça `toList`, `toSet`, `toMap`, `joining`, `counting`, `mapping`, `groupingBy`, `partitioningBy`, `averaging...`, `summarizing...` e `teeing`. Em `toMap`, chaves repetidas exigem função de merge.

## 8. Gatherers

`gather` é uma operação intermediária extensível. A API final inclui gatherers prontos:

```java
import java.util.stream.Gatherers;

var windows = Stream.of(1, 2, 3, 4, 5)
        .gather(Gatherers.windowFixed(2))
        .toList();
// [[1, 2], [3, 4], [5]]
```

Também estude `windowSliding`, `fold`, `scan` e `mapConcurrent`. Collector produz um resultado terminal; Gatherer participa no meio do pipeline e pode emitir zero, um ou vários elementos por entrada.

## 9. Paralelismo

```java
long count = values.parallelStream()
        .filter(predicate)
        .count();
```

Paralelo não significa sempre mais rápido. Operações devem evitar estado compartilhado, respeitar associatividade e distinguir ordem de encontro de ordem de execução. `forEachOrdered` preserva a ordem de encontro, com custo.

## Revisão OCPJ25

Classifique cada chamada como fonte, intermediária ou terminal; marque alterações de tipo; determine finitude e ordem; verifique curto-circuito, `Optional`, associatividade e efeitos colaterais.

## Referências

- [API Java 25 — Stream](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Stream.html)
- [API Java 25 — Collectors](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Collectors.html)
- [API Java 25 — Gatherers](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/stream/Gatherers.html)
