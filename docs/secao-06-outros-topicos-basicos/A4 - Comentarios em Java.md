# Comentários em Java

<sub>📚 [Documentação](../README.md) › [Seção 6 · Outros tópicos básicos sobre Java](./README.md) › Material 4 de 8</sub>

Comentários explicam decisões importantes e não fazem parte da execução do programa. Eles não devem repetir literalmente o que o código já diz.

## Comentário de linha

Começa com `//` e termina na quebra de linha:

```java
double taxa = 0.10; // percentual aplicado ao cliente frequente
```

## Comentário de bloco

Começa com `/*` e termina com `*/`:

```java
/*
 * Este cálculo usa juros simples.
 * A taxa e o período precisam usar a mesma unidade.
 */
double juros = capital * taxa * periodo;
```

Comentários de bloco não podem ser aninhados. O primeiro `*/` encerra o comentário; o restante passa a ser interpretado como código.

## Comentário de documentação

`/** ... */` é reconhecido pela ferramenta `javadoc`:

```java
/**
 * Reúne cálculos básicos usados nos exercícios do curso.
 */
public class Calculadora {
}
```

Neste momento, basta reconhecer o formato. Depois da introdução aos métodos, `@param` poderá descrever um parâmetro e `@return` poderá descrever o valor devolvido.

## Marcadores dentro de textos

Marcadores dentro de uma `String` são apenas caracteres:

```java
String endereco = "https://exemplo.com";
String trecho = "/* isto faz parte do texto */";
```

O compilador reconhece primeiro os limites do literal. Por isso, `//` dentro da URL não inicia comentário.

## Comentários úteis

Prefira explicar o motivo:

```java
// Usa 2.0 para evitar divisão inteira.
double media = (nota1 + nota2) / 2.0;
```

Evite narrar a sintaxe:

```java
// Soma 1 a contador.
contador++;
```

Nomes claros e métodos pequenos reduzem a necessidade de comentários. O comentário deve registrar uma decisão, uma restrição ou um detalhe que não está evidente.

## Referências

- [Java Language Specification 25 - Comments](https://docs.oracle.com/javase/specs/jls/se25/html/jls-3.html#jls-3.7).
- [JDK 25 Documentation Comment Specification](https://docs.oracle.com/en/java/javase/25/javadoc/doc-comment-spec.html).

---

<div align="center">

⬅️ [A3 · Funções interessantes para String](./A3%20-%20Funcoes%20interessantes%20para%20String.md) &nbsp;·&nbsp; 📂 [Seção 6](./README.md) &nbsp;·&nbsp; [A5 · Métodos: declaração e chamada](./A5%20-%20Metodos%20declaracao%20e%20chamada.md) ➡️

</div>
