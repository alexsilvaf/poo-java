# Guia gradual de lambdas e method references

## 1. Tipo-alvo

Uma lambda não possui tipo sozinha. O contexto fornece uma interface funcional:

```java
Predicate<String> longName = text -> text.length() > 5;
```

Formas equivalentes:

```java
x -> x * 2
(x) -> x * 2
(int x) -> x * 2
(int x) -> { return x * 2; }
```

Se declarar o tipo de um parâmetro, declare todos. Parênteses são obrigatórios para zero ou vários parâmetros.

## 2. Interfaces padrão

| Interface | Entrada | Saída | Método |
| --- | --- | --- | --- |
| `Predicate<T>` | `T` | `boolean` | `test` |
| `Consumer<T>` | `T` | `void` | `accept` |
| `Supplier<T>` | — | `T` | `get` |
| `Function<T,R>` | `T` | `R` | `apply` |
| `UnaryOperator<T>` | `T` | `T` | `apply` |
| `BinaryOperator<T>` | `T,T` | `T` | `apply` |

Existem variantes `Bi...` e especializações primitivas, como `IntPredicate`, `ToIntFunction<T>` e `IntFunction<R>`, que evitam boxing.

## 3. Composição

```java
Predicate<String> present = s -> s != null;
Predicate<String> nonBlank = s -> !s.isBlank();
Predicate<String> valid = present.and(nonBlank);

Function<String, String> trim = String::strip;
Function<String, Integer> size = String::length;
Function<String, Integer> trimmedSize = trim.andThen(size);
```

Conheça `and`, `or`, `negate`, `compose` e `andThen` e observe a ordem de execução.

## 4. Captura de variáveis

```java
int minimum = 5;
Predicate<String> accepted = value -> value.length() >= minimum;
```

Uma variável local capturada deve ser final ou efetivamente final. Campos não seguem essa restrição. O escopo da lambda não cria uma nova variável com o mesmo nome de uma local externa.

## 5. Method references

Quatro categorias:

```java
Function<String, Integer> a = Integer::parseInt; // static
Supplier<String> b = "java"::toUpperCase;        // instância conhecida
Function<String, String> c = String::strip;       // instância do primeiro argumento
Supplier<ArrayList<String>> d = ArrayList::new;   // construtor
```

A forma curta precisa ser compatível com os parâmetros e retorno do tipo-alvo. O nome do método sozinho não decide qual sobrecarga será usada.

## 6. Lambdas em collections

```java
names.removeIf(String::isBlank);
names.replaceAll(String::strip);
names.forEach(System.out::println);
names.sort(Comparator.comparingInt(String::length));
```

Mapas oferecem `forEach`, `computeIfAbsent`, `merge` e outros métodos que recebem funções.

## 7. Parâmetro sem nome

```java
map.forEach((key, _) -> System.out.println(key));
```

No Java 25, `_` informa que o segundo parâmetro não será usado. Cada `_` é uma variável sem nome e não pode ser referenciada no corpo.

## 8. Lambda versus classe anônima

Dentro da lambda, `this` é o `this` do contexto envolvente. Em classe anônima, `this` é a nova instância anônima. Lambdas também dependem de uma interface funcional e não introduzem um novo escopo de nomes da mesma forma.

## Revisão OCPJ25

Determine primeiro o tipo-alvo, depois a assinatura funcional. Só então verifique sintaxe, captura, boxing, possíveis overloads e retorno de cada caminho do corpo.

## Referências

- [JLS 25 — Lambda Expressions](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.27)
- [JLS 25 — Method References](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.13)
- [API Java 25 — java.util.function](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/function/package-summary.html)
