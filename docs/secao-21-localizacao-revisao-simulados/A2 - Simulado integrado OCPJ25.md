# Simulado integrado OCPJ25

Resolva antes de abrir as respostas. Em cada questão, decida primeiro se o código compila.

## Questões

### 1. Arrays e referências

```java
int[] a = {1, 2};
int[] b = a;
b[0]++;
b = new int[] {9};
System.out.println(a[0] + ":" + b[0]);
```

### 2. Sobrescrita

```java
class A { Number value() { return 1; } }
class B extends A { @Override Integer value() { return 2; } }
A item = new B();
System.out.println(item.value());
```

### 3. Record pattern

```java
record Point(int x, int y) { }
Object value = new Point(3, 4);
String result = switch (value) {
    case Point(int x, int _) -> "x=" + x;
    default -> "other";
};
```

### 4. Exceções e recursos

Dois recursos `a` e `b` são declarados nessa ordem em try-with-resources. O corpo lança `IOException`, `b.close()` lança `SQLException` e `a.close()` não falha. Qual exceção é principal e qual fica suprimida?

### 5. Collections

```java
List<Integer> list = new ArrayList<>(List.of(1, 2, 3));
list.remove(1);
list.remove(Integer.valueOf(3));
System.out.println(list);
```

### 6. Wildcards

Qual declaração aceita `List<Integer>` e permite ler cada elemento como `Number` sem permitir adicionar um `Double`?

### 7. Lambda

```java
int limit = 3;
Predicate<String> test = s -> s.length() > limit;
// limit++;
```

Por que a linha comentada impediria a compilação da lambda?

### 8. Streams

```java
long count = Stream.of("a", "bb", "ccc")
        .peek(System.out::print)
        .filter(s -> s.length() > 1)
        .count();
System.out.println(":" + count);
```

### 9. Gatherer

Qual é a diferença estrutural entre `collect(...)` e `gather(...)` em um pipeline?

### 10. NIO.2

Explique por que um `Stream<String>` retornado por `Files.lines(path)` deve estar em try-with-resources.

### 11. Módulos

`exports p;` e `opens p;` oferecem o mesmo acesso? Explique.

### 12. Concorrência

`volatile int count; count++;` é suficiente para incremento atômico por várias threads?

### 13. Scoped values

Qual diferença central existe entre um scoped value e um campo global mutável?

### 14. Tempo

Por que `zoned.plusDays(1)` pode avançar 23 ou 25 horas na linha do tempo?

### 15. Localização

Por que usar `Locale.setDefault` em uma biblioteca pode ser arriscado?

## Respostas

<details>
<summary><b>1. Resposta</b></summary>

`2:9`. `a` e `b` apontavam para o mesmo array durante o incremento; depois apenas `b` foi reatribuído.
</details>

<details>
<summary><b>2. Resposta</b></summary>

Compila e imprime `2`. `Integer` é retorno covariante de `Number`; o método sobrescrito é escolhido pelo objeto `B`.
</details>

<details>
<summary><b>3. Resposta</b></summary>

Compila no Java 25 e produz `x=3`. `_` ignora o segundo componente e não pode ser lido.
</details>

<details>
<summary><b>4. Resposta</b></summary>

A `IOException` do corpo é principal. A `SQLException` de `b.close()` fica suprimida. Recursos fecham em ordem inversa.
</details>

<details>
<summary><b>5. Resposta</b></summary>

Imprime `[1]`. `remove(1)` remove o elemento no índice 1, e a segunda chamada remove o objeto `3`.
</details>

<details>
<summary><b>6. Resposta</b></summary>

`List<? extends Number>`. Ela é produtora de `Number`; não aceita adicionar um `Double` porque o tipo real pode ser `Integer`.
</details>

<details>
<summary><b>7. Resposta</b></summary>

A lambda captura `limit`, que precisa permanecer final ou efetivamente final. O incremento eliminaria essa propriedade.
</details>

<details>
<summary><b>8. Resposta</b></summary>

Imprime os elementos quando o pipeline terminal executa e termina com `:2`. `peek` é lazy e `bb`/`ccc` passam no filtro.
</details>

<details>
<summary><b>9. Resposta</b></summary>

`collect` é terminal e encerra o pipeline em um resultado. `gather` é intermediária e pode emitir zero, um ou vários elementos para etapas seguintes.
</details>

<details>
<summary><b>10. Resposta</b></summary>

O stream mantém aberto o recurso usado para ler o arquivo. Fechá-lo deterministicamente evita vazamento de descritores.
</details>

<details>
<summary><b>11. Resposta</b></summary>

Não. `exports` permite acesso normal aos tipos públicos do pacote; `opens` permite reflexão profunda em tempo de execução. Podem ser qualificados para módulos específicos.
</details>

<details>
<summary><b>12. Resposta</b></summary>

Não. `volatile` fornece visibilidade, mas `count++` é uma sequência composta. Use sincronização ou `AtomicInteger`.
</details>

<details>
<summary><b>13. Resposta</b></summary>

O binding do scoped value é imutável e limitado a um escopo dinâmico; um campo global mutável pode ser alterado e observado sem esse limite.
</details>

<details>
<summary><b>14. Resposta</b></summary>

Um dia de calendário preserva a hora local, mas mudanças de horário de verão alteram o deslocamento e, portanto, a duração real entre os instantes.
</details>

<details>
<summary><b>15. Resposta</b></summary>

Ela altera estado global do processo e pode afetar código não relacionado. APIs de biblioteca devem preferir locale explícito.
</details>
