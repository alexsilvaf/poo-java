# Guia gradual de arrays, `for-each`, `var` e varargs

## 1. Criando arrays

Um array é um objeto de tamanho fixo que guarda elementos de um único tipo.

```java
int[] scores = new int[3];
scores[0] = 7;
scores[1] = 9;
scores[2] = 8;
```

Os índices começam em zero e terminam em `length - 1`. `scores[3]` compila, mas lança `ArrayIndexOutOfBoundsException` durante a execução.

Inicialização abreviada:

```java
String[] names = {"Ana", "Bia", "Caio"};
int[] primes = new int[] {2, 3, 5, 7};
```

Após a declaração, a forma `{...}` isolada não pode ser usada em uma atribuição. Use `new int[] {...}`.

## 2. Valores padrão e referências

```java
int[] numbers = new int[2];       // [0, 0]
boolean[] flags = new boolean[2]; // [false, false]
Product[] products = new Product[2]; // [null, null]
```

Criar `new Product[2]` cria o array, não dois produtos. Cada posição precisa receber uma referência:

```java
products[0] = new Product("TV", 900.0, 1);
```

`int[] copy = numbers` copia a referência. Para copiar o conteúdo, use `numbers.clone()` ou `Arrays.copyOf`.

## 3. Percorrendo

O `for` tradicional oferece o índice:

```java
for (int i = 0; i < names.length; i++) {
    System.out.println(i + ": " + names[i]);
}
```

O `for-each` oferece cada valor:

```java
for (String name : names) {
    System.out.println(name);
}
```

Reatribuir a variável do `for-each` não substitui o elemento do array:

```java
for (String name : names) {
    name = name.toUpperCase();
}
```

Para atualizar posições, use o índice.

## 4. Matrizes e arrays irregulares

```java
int[][] matrix = new int[2][3];
int[][] irregular = new int[3][];
irregular[0] = new int[1];
irregular[1] = new int[4];
irregular[2] = new int[2];
```

Cada linha é outro array e pode ter tamanho diferente. Percurso seguro:

```java
for (int[] row : irregular) {
    for (int value : row) {
        System.out.print(value + " ");
    }
}
```

Rótulos permitem sair de laços aninhados:

```java
search:
for (int[] row : matrix) {
    for (int value : row) {
        if (value == 9) break search;
    }
}
```

## 5. `Arrays`

```java
import java.util.Arrays;

int[] values = {4, 1, 3};
Arrays.sort(values);                    // [1, 3, 4]
int index = Arrays.binarySearch(values, 3); // 1
int[] copy = Arrays.copyOf(values, 5);  // [1, 3, 4, 0, 0]
boolean same = Arrays.equals(values, new int[] {1, 3, 4});
System.out.println(Arrays.toString(values));
```

`binarySearch` só produz resultado significativo quando o array está ordenado de forma compatível.

## 6. Inferência local com `var`

`var` pede ao compilador que deduza o tipo de uma variável local:

```java
var count = 10;              // int
var labels = new String[3];  // String[]
```

Não é tipo dinâmico. O tipo não muda depois. Restrições importantes:

```java
// var value;             // sem inicializador
// var empty = null;      // tipo não pode ser inferido
// var[] data = new int[2];
```

`var` não declara campos, parâmetros comuns nem tipos de retorno.

## 7. Varargs

```java
static int sum(int... values) {
    int total = 0;
    for (int value : values) total += value;
    return total;
}
```

Chamadas válidas:

```java
sum();
sum(1, 2, 3);
sum(new int[] {4, 5});
```

Regras:

- só pode existir um varargs;
- ele deve ser o último parâmetro;
- `int...` e `int[]` representam a mesma assinatura, portanto não podem ser sobrecargas entre si;
- dentro do método, `values` é `int[]` e pode ser `null` se o chamador passar `null` explicitamente.

## 8. Variáveis sem nome

Java 25 permite `_` em posições onde o valor recebido não será usado, como um parâmetro de lambda ou uma variável local inicializada apenas pelo efeito colateral:

```java
for (int _ : values) {
    System.out.println("one element");
}
```

Uma variável `_` não pode ser lida. Não confunda esse uso finalizado com padrões primitivos, que continuam preview no Java 25.

## Revisão OCPJ25

Preveja:

```java
int[][] data = {{1, 2}, null, {3}};
System.out.println(data.length);
System.out.println(data[0].length);
```

As saídas são `3` e `2`. Acessar `data[1].length` lançaria `NullPointerException`.

Checklist: índices, `length` sem parênteses, valores padrão, aliasing, matrizes irregulares, `Arrays`, `var`, varargs e `_`.

## Referências

- [JLS 25 — Arrays](https://docs.oracle.com/javase/specs/jls/se25/html/jls-10.html)
- [JLS 25 — Local Variable Type Inference](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.4)
- [JLS 25 — Unnamed Variables](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.4.2)
