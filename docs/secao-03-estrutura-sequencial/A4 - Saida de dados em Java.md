# Saída de dados em Java

<sub>📚 [Documentação](../README.md) › [Seção 3 · Estrutura sequencial](./README.md) › Material 4 de 8</sub>

Saída é como o programa mostra resultados. No console, o curso usa `System.out`, ligado à saída padrão. Os detalhes sobre objetos e a classe `PrintStream` serão estudados mais adiante.

## `print`, `println` e `printf`

| Método | O que faz |
|---|---|
| `System.out.print(x)` | escreve e **não** quebra a linha |
| `System.out.println(x)` | escreve e quebra a linha |
| `System.out.println()` | escreve apenas uma quebra de linha |
| `System.out.printf(formato, ...)` | escreve com formatação, **sem** quebrar a linha |

```java
System.out.print("Bom ");
System.out.print("dia");
System.out.println("!");
System.out.println("Nova linha");
```

```
Bom dia!
Nova linha
```

> [!NOTE]
> Existe também `System.err`, que escreve na saída de erro. Na IDE ele costuma aparecer em vermelho. É onde as mensagens de erro devem ir, para não se misturarem com a saída normal do programa.

## Concatenação com `+`

Quando um dos lados do `+` é `String`, o outro é convertido para texto:

```java
String nome = "Maria";
int idade = 30;
System.out.println("Nome: " + nome + ", idade: " + idade);
```

```
Nome: Maria, idade: 30
```

A avaliação é da esquerda para a direita, e isso muda o resultado:

```java
System.out.println("Total: " + 2 + 3);   // Total: 23
System.out.println("Total: " + (2 + 3)); // Total: 5
System.out.println(2 + 3 + " itens");    // 5 itens
```

Assim que a primeira `String` entra na expressão, todo o resto vira concatenação.

## Sequências de escape

Dentro de uma `String`, a barra invertida introduz caracteres especiais:

| Escape | Significado |
|---|---|
| `\n` | quebra de linha |
| `\t` | tabulação |
| `\"` | aspas duplas |
| `\\` | barra invertida |
| `\'` | aspas simples (usado em `char`) |

```java
System.out.println("Linha 1\nLinha 2");
System.out.println("Nome:\tMaria");
System.out.println("Ele disse \"ola\"");
System.out.println("Caminho: C:\\Users\\Maria");
```

## `printf` e os especificadores de formato

`printf` é o caminho para controlar **como** o número aparece. O primeiro argumento é o texto de formato; os demais preenchem os marcadores, na ordem.

```java
double preco = 1234.56789;
System.out.printf("Preço: %.2f%n", preco);   // Preço: 1234,57
```

| Especificador | Serve para | Exemplo |
|---|---|---|
| `%d` | inteiros (`byte`, `short`, `int`, `long`) | `%d` com `42` → `42` |
| `%f` | ponto flutuante (`float`, `double`) | `%.2f` com `3.14159` → `3,14` |
| `%s` | texto e outros valores convertidos para texto | `%s` com `"Ana"` → `Ana` |
| `%c` | um caractere | `%c` com `'A'` → `A` |
| `%b` | booleano | `%b` com `true` → `true` |
| `%%` | um sinal de porcentagem literal | `%%` → `%` |
| `%n` | quebra de linha do sistema | — |

Os sete em um programa só:

```java
String nome = "Ana";
char inicial = 'A';
int idade = 30;
double altura = 1.6789;
boolean ativo = true;

System.out.printf("Nome: %s (%c)%n", nome, inicial);
System.out.printf("Idade: %d anos%n", idade);
System.out.printf("Altura: %.2f m%n", altura);
System.out.printf("Ativo: %b%n", ativo);
System.out.printf("Desconto de %d%%%n", 15);
```

```
Nome: Ana (A)
Idade: 30 anos
Altura: 1,68 m
Ativo: true
Desconto de 15%
```

Cada marcador consome um argumento, na ordem em que aparece — a primeira linha usa dois. E repare no `%.2f` com `1.6789`: sai `1,68`, porque o `printf` **arredonda** na hora de mostrar. O valor guardado na variável continua sendo `1.6789`.

### Largura, alinhamento e casas decimais

Um especificador pode ter mais partes do que só a letra do tipo. Lendo `%-10.2f` da esquerda para a direita:

| Parte | O que é |
|:---:|---|
| `%` | começa o marcador |
| `-` | alinha à **esquerda**; sem ele, o valor vai para a direita |
| `10` | **largura mínima**: o campo ocupa 10 caracteres |
| `.2` | duas casas decimais |
| `f` | o tipo: ponto flutuante |

```java
System.out.printf("[%10.2f]%n", 3.14159);   // [      3,14]  — largura 10, à direita
System.out.printf("[%-10.2f]%n", 3.14159);  // [3,14      ]  — o - alinha à esquerda
System.out.printf("[%05d]%n", 42);          // [00042]       — completa com zeros
System.out.printf("[%,d]%n", 1000000);      // [1.000.000]   — separador de milhar
```

Os colchetes não fazem parte do formato: estão ali só para revelar o preenchimento. `3,14` tem 4 caracteres, e os 6 restantes são espaços até fechar a largura 10 — não é tabulação, é o campo sendo completado. Sem os colchetes, `[%-10.2f]` pareceria imprimir `3,14` seguido de um espaço grande sem motivo.

Isso é o que permite montar tabelas alinhadas no console:

```java
System.out.printf("%-15s %8s%n", "Produto", "Preço");
System.out.printf("%-15s %8.2f%n", "Teclado", 89.9);
System.out.printf("%-15s %8.2f%n", "Monitor", 1250.0);
```

```
Produto            Preço
Teclado            89,90
Monitor          1250,00
```

### `%n` ou `\n`?

`\n` é sempre o caractere de nova linha (`LF`). `%n` usa a quebra de linha do sistema operacional — `\n` no Linux e no macOS, `\r\n` no Windows. Em `printf`, prefira `%n`.

## Vírgula ou ponto: o problema do `Locale`

`printf` formata números segundo o **idioma configurado no sistema**. Em uma máquina configurada em português do Brasil, `%.2f` imprime `3,14`; em uma configurada em inglês, imprime `3.14`.

Quando o exercício exige o ponto como separador decimal — o que é comum em plataformas de correção automática — force o idioma:

```java
import java.util.Locale;

public class Formatacao {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        System.out.printf("%.2f%n", 3.14159);   // 3.14
    }
}
```

`Locale.setDefault` deve ser chamado **uma única vez**, logo no início do `main`.

> [!NOTE]
> Isso afeta apenas a **formatação da saída**. A leitura de números pelo `Scanner` também é sensível ao idioma, como mostra o material [A6 - Entrada de dados em Java](./A6%20-%20Entrada%20de%20dados%20em%20Java.md).

## `String.format`

O mesmo mecanismo do `printf`, mas devolvendo a `String` em vez de imprimi-la:

```java
double media = 8.4567;
String texto = String.format("Media: %.2f", media);
System.out.println(texto);
```

Útil quando o texto formatado precisa ser guardado, comparado ou usado mais de uma vez.

## Texto em várias linhas: *text blocks*

Desde o Java 15, três aspas duplas abrem um bloco de texto que preserva as quebras de linha:

```java
String menu = """
        === MENU ===
        1 - Cadastrar
        2 - Consultar
        3 - Sair
        """;
System.out.print(menu);
```

A indentação comum a todas as linhas é removida automaticamente, então o bloco pode ficar alinhado com o código sem sujar a saída.

## Saída com `IO.println` (Java 25)

Em arquivos-fonte compactos, a classe `java.lang.IO` oferece uma forma mais curta:

```java
void main() {
    IO.println("Ola, mundo!");
}
```

`IO.println` cobre o caso simples, mas **não** tem equivalente a `printf`: quando é preciso formatar, o caminho continua sendo `System.out.printf` ou `String.format`. O curso segue usando `System.out`, e a forma compacta fica registrada no material [A7 da Seção 2](../secao-02-introducao-java/A7%20-%20Sintaxe%20simplificada%20do%20Java%2025.md).

## Erros comuns

| Sintoma | Causa |
|---|---|
| `Total: 23` em vez de `Total: 5` | faltou o parêntese na soma antes de concatenar |
| `3,14` quando se esperava `3.14` | `Locale` do sistema; falta `Locale.setDefault(Locale.US)` |
| `IllegalFormatConversionException` | `%d` recebendo um `double`, ou `%f` recebendo um `int` |
| `MissingFormatArgumentException` | mais marcadores no formato do que argumentos passados |
| Tudo saiu na mesma linha | usou `print` ou `printf` sem `%n` no fim |

## Referências

- [OCPJ21 Study Guide — Chapter 4: Working with Data](../ocpj21-book/ch04.md), seções *Formatting Strings* e *Text Blocks*.
- [OCPJ21 Study Guide — Chapter 14: Localization](../ocpj21-book/ch14.md), seção *The `Locale` Class*.

---

<div align="center">

⬅️ [A3 · As três operações básicas de programação](./A3%20-%20As%20tres%20operacoes%20basicas.md) &nbsp;·&nbsp; 📂 [Seção 3](./README.md) &nbsp;·&nbsp; [A5 · Processamento de dados e casting](./A5%20-%20Processamento%20de%20dados%20e%20casting.md) ➡️

</div>
