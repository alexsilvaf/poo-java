# Guia gradual de wrappers, texto e tempo

## 1. Wrappers

Cada primitivo possui wrapper, como `Integer`, `Long`, `Double`, `Boolean` e `Character`.

```java
Integer boxed = 10;          // autoboxing
int primitive = boxed;       // unboxing
int parsed = Integer.parseInt("42");
Integer object = Integer.valueOf("42");
```

Unboxing de `null` lança `NullPointerException`. `==` entre wrappers pode comparar referências; use `equals` para valor. Caches tornam alguns resultados de `==` aparentemente verdadeiros, portanto não baseie lógica neles.

## 2. `String`, identidade e pool

```java
String a = "java";
String b = "ja" + "va";       // constante compilada
String c = new String("java");

System.out.println(a == b);      // true
System.out.println(a == c);      // false
System.out.println(a.equals(c)); // true
```

`String` é imutável. Métodos devolvem uma nova referência ou a própria quando permitido; eles não alteram o objeto original.

## 3. `StringBuilder`

```java
StringBuilder builder = new StringBuilder("Java");
builder.append(" 25")
       .insert(0, "OCP ")
       .replace(0, 3, "Exam")
       .reverse();
```

É mutável. Conheça `length`, `capacity`, `append`, `insert`, `delete`, `deleteCharAt`, `replace`, `reverse`, `charAt`, `setCharAt`, `substring` e `toString`. `substring` devolve `String` e não altera o builder.

## 4. Text blocks

```java
String json = """
        {
          "name": "Java"
        }
        """;
```

O conteúdo começa após a quebra de linha obrigatória que segue `"""`. A indentação incidental é removida. `\` no fim de linha suprime a quebra; `\s` preserva um espaço.

## 5. Tipos centrais de data e hora

```java
LocalDate date = LocalDate.of(2026, 9, 19);
LocalTime time = LocalTime.of(14, 30);
LocalDateTime dateTime = LocalDateTime.of(date, time);
Instant instant = Instant.now();
ZoneId zone = ZoneId.of("America/Sao_Paulo");
ZonedDateTime zoned = dateTime.atZone(zone);
```

Classes de `java.time` são imutáveis:

```java
date.plusDays(1);       // resultado ignorado
date = date.plusDays(1); // atualização da referência
```

## 6. `Period` e `Duration`

- `Period`: quantidade baseada em datas, como anos, meses e dias;
- `Duration`: quantidade baseada em tempo, como segundos e nanos.

```java
Period month = Period.ofMonths(1);
Duration hour = Duration.ofHours(1);
Duration gap = startInstant.until(endInstant); // disponível no Java 25
```

Nem toda unidade é compatível com todo tipo temporal.

## 7. Fusos e horário de verão

`ZonedDateTime` aplica as regras da região. Ao atravessar mudança de horário de verão, somar um dia de calendário pode representar duração diferente de 24 horas. `ZoneOffset` é apenas um deslocamento; `ZoneId` de região conhece regras históricas.

## 8. Parsing e formatação

```java
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/uuuu");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse("19/09/2026", formatter);
```

Use `u` para ano proleptico em parsing rigoroso. `DateTimeFormatter` é imutável e thread-safe.

## Revisão OCPJ25

Armadilhas: `==` versus `equals`, unboxing de `null`, índices de `StringBuilder`, resultado ignorado de objeto imutável, formato incompatível e diferenças entre `Period`, `Duration`, `Instant` e `ZonedDateTime`.

## Referências

- [API Java 25 — java.lang](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/package-summary.html)
- [API Java 25 — java.time](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/time/package-summary.html)
- [Java 25 — Language Changes](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-summary.html)
