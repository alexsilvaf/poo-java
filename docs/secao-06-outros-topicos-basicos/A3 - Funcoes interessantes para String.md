# Funções interessantes para String

<sub>📚 [Documentação](../README.md) › [Seção 6 · Outros tópicos básicos sobre Java](./README.md) › Material 3 de 8</sub>

`String` representa texto. Até aqui, o curso usou textos para entrada e saída. Agora o aluno passa a consultar, comparar e transformar seu conteúdo.

> [!NOTE]
> Em Java, essas operações são chamadas de **métodos**. Nesta aula, basta observar como utilizá-las. A declaração de métodos próprios começa no A5.

## Índices começam em zero

```text
Texto:  J  a  v  a
Índice: 0  1  2  3
```

```java
String linguagem = "Java";

System.out.println(linguagem.length());  // 4
System.out.println(linguagem.charAt(0)); // J
System.out.println(linguagem.charAt(3)); // a
```

O último índice válido é sempre `length() - 1`.

Usar um índice negativo ou igual ao tamanho causa erro em tempo de execução.

## Extraindo partes com `substring`

```java
String texto = "programacao";

System.out.println(texto.substring(3));    // gramacao
System.out.println(texto.substring(0, 4)); // prog
```

Em `substring(inicio, fim)`, o início entra e o fim não entra. Para `substring(0, 4)`, são usados os índices 0, 1, 2 e 3.

## Buscando conteúdo

```java
String email = "aluno@exemplo.com";

System.out.println(email.contains("@"));          // true
System.out.println(email.startsWith("aluno"));    // true
System.out.println(email.endsWith(".com"));       // true
System.out.println(email.indexOf('@'));            // 5
System.out.println(email.indexOf("exemplo"));      // 6
System.out.println(email.indexOf("inexistente")); // -1
```

`indexOf` devolve o índice da primeira ocorrência ou `-1` quando não encontra.

## Comparando textos por conteúdo

```java
String resposta = "sim";

System.out.println(resposta.equals("sim"));           // true
System.out.println(resposta.equals("SIM"));           // false
System.out.println(resposta.equalsIgnoreCase("SIM")); // true
```

`==` não é a operação adequada para comparar o conteúdo de dois textos. A explicação completa envolve referências e objetos e será retomada na Seção 7. Até lá, a regra prática é clara: conteúdo de `String` se compara com `equals`.

## Transformando o texto

```java
String original = "  Curso Java  ";

System.out.println(original.toUpperCase());            // "  CURSO JAVA  "
System.out.println(original.toLowerCase());            // "  curso java  "
System.out.println(original.strip());                  // "Curso Java"
System.out.println(original.replace("Java", "JDK")); // "  Curso JDK  "
```

`strip()` considera os espaços em branco definidos por Unicode. `trim()` é mais antigo e remove apenas caracteres de código até U+0020.

Outras operações úteis:

```java
String palavra = "Java";

System.out.println(palavra.concat(" 25")); // Java 25
System.out.println(palavra.repeat(3));      // JavaJavaJava
System.out.println("".isEmpty());           // true
System.out.println("   ".isBlank());        // true
```

## `String` é imutável

Os métodos não alteram o texto existente. Eles produzem outro resultado:

```java
String nome = "  Ana  ";

nome.strip();
System.out.println(nome); // ainda contém os espaços
```

Para guardar o texto transformado, atribua o resultado:

```java
nome = nome.strip();
System.out.println(nome); // Ana
```

Também é possível encadear chamadas:

```java
String codigo = "  java-25  ";
String normalizado = codigo.strip().toUpperCase().replace('-', ' ');

System.out.println(normalizado); // JAVA 25
```

## Percorrendo um texto

```java
String palavra = "Java";

for (int i = 0; i < palavra.length(); i++) {
    System.out.println(palavra.charAt(i));
}
```

Esse exemplo não precisa de arrays. Métodos como `split()` e `toCharArray()` ficam para a seção em que arrays forem apresentados.

## Referências

- [Java SE 25 API - String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html).
- [OCPJ21 Study Guide - Chapter 4: Working with Data](../ocpj21-book/ch04.md), seções sobre `String`.

---

<div align="center">

⬅️ [A2 · Operadores bitwise](./A2%20-%20Operadores%20bitwise.md) &nbsp;·&nbsp; 📂 [Seção 6](./README.md) &nbsp;·&nbsp; [A4 · Comentários em Java](./A4%20-%20Comentarios%20em%20Java.md) ➡️

</div>
