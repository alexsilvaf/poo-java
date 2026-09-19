# Entrada de dados em Java

<sub>📚 [Documentação](../README.md) › [Seção 3 · Estrutura sequencial](./README.md) › Material 6 de 8</sub>

Entrada é como o programa recebe dados de fora. No console, a fonte é `System.in`, e a classe usada para lê-la é `java.util.Scanner`.

## Criando e usando um `Scanner`

```java
import java.util.Scanner;

public class Entrada {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nome = sc.nextLine();

        System.out.println("Ola, " + nome + "!");

        sc.close();
    }
}
```

Três coisas são obrigatórias:

1. o `import java.util.Scanner;` no topo do arquivo;
2. a criação do objeto: `Scanner sc = new Scanner(System.in);`
3. o `sc.close()` ao final, para liberar o recurso.

> [!NOTE]
> `Scanner` não é primitivo: é uma classe, e por isso precisa de `new`. Esse é o primeiro contato do curso com criação de objetos — o assunto é retomado a fundo na Seção 7.

## Métodos de leitura

| Método | Lê | Devolve |
|---|---|---|
| `sc.nextInt()` | o próximo token como inteiro | `int` |
| `sc.nextLong()` | o próximo token como inteiro longo | `long` |
| `sc.nextDouble()` | o próximo token como decimal | `double` |
| `sc.next()` | o próximo token (uma "palavra") | `String` |
| `sc.nextLine()` | o resto da linha atual, inclusive espaços | `String` |
| `sc.nextBoolean()` | `true` ou `false` | `boolean` |
| `sc.next().charAt(0)` | o primeiro caractere do token | `char` |

Não existe `nextChar()`. Para ler um único caractere, lê-se um token e pega-se a primeira posição.

## Token e linha: a distinção que causa mais confusão

Um **token** é um pedaço de texto delimitado por espaço em branco — espaço, tabulação ou quebra de linha. `next()`, `nextInt()` e `nextDouble()` leem **tokens**; `nextLine()` lê **até o fim da linha**.

```java
System.out.print("Digite tres valores: ");
int a = sc.nextInt();
int b = sc.nextInt();
int c = sc.nextInt();
System.out.println(a + b + c);
```

```
Digite tres valores: 10 20 30
60
```

Os três valores podem ser digitados na mesma linha, separados por espaço, ou em linhas diferentes: para o `Scanner`, dá no mesmo.

## A pegadinha do `nextLine` depois do `nextInt`

```java
System.out.print("Idade: ");
int idade = sc.nextInt();
System.out.print("Nome: ");
String nome = sc.nextLine();     // volta vazio, sem esperar o usuário digitar
```

`nextInt()` consome apenas os dígitos e **deixa a quebra de linha no buffer**. O `nextLine()` seguinte encontra essa quebra pendente, entende que a linha acabou ali e devolve uma `String` vazia.

A solução é consumir a quebra de linha pendente com um `nextLine()` extra:

```java
System.out.print("Idade: ");
int idade = sc.nextInt();
sc.nextLine();                   // descarta o resto da linha
System.out.print("Nome: ");
String nome = sc.nextLine();     // agora funciona
```

> [!WARNING]
> Esta é, de longe, a causa número um de "meu programa pulou a leitura". Sempre que um `nextLine()` vier depois de um `nextInt()`, `nextDouble()` ou `next()`, é preciso limpar o buffer.

## Vírgula ou ponto na leitura de decimais

`nextDouble()` respeita o idioma configurado. Em uma máquina em português do Brasil, ele espera **vírgula**:

```
Digite o preco: 3.14
```

```
InputMismatchException
```

Duas formas de resolver:

```java
Locale.setDefault(Locale.US);        // antes de criar o Scanner
Scanner sc = new Scanner(System.in);
```

```java
Scanner sc = new Scanner(System.in);
sc.useLocale(Locale.US);             // depois de criado
```

Escolha uma convenção e mantenha-a: misturar formatação `US` na saída com leitura `pt-BR` na entrada é fonte garantida de confusão.

## Fechando o `Scanner`

`sc.close()` libera o recurso, e a IDE avisa quando ele é esquecido. Duas ressalvas:

- fechar um `Scanner` ligado a `System.in` **fecha também a entrada padrão**: depois disso, nenhum outro `Scanner` conseguirá ler do teclado;
- por isso, use um único `Scanner` por programa e feche-o apenas no final do `main`.

## Entrada com `IO.readln` (Java 25)

Em arquivos-fonte compactos, a classe `java.lang.IO` cobre o caso simples sem precisar de `Scanner`:

```java
void main() {
    String nome = IO.readln("Digite seu nome: ");
    IO.println("Ola, " + nome + "!");
}
```

`IO.readln` devolve texto. A conversão desse texto para números será apresentada somente quando houver necessidade; nos exercícios desta seção, o curso usa `Scanner`, que já fornece `nextInt` e `nextDouble`.

## Erros comuns

| Sintoma | Causa |
|---|---|
| `Scanner cannot be resolved to a type` | faltou `import java.util.Scanner;` |
| `InputMismatchException` | o texto digitado não corresponde ao método (`nextInt()` recebendo `abc`, ou `nextDouble()` recebendo ponto em locale pt-BR) |
| `NoSuchElementException` | não há mais dados para ler, ou o `Scanner` já foi fechado |
| Leitura "pulada" | quebra de linha pendente antes de um `nextLine()` |
| Nome truncado no primeiro espaço | usou `next()` onde deveria usar `nextLine()` |

## Referências

- [OCPJ21 Study Guide — Chapter 12: File I/O](../ocpj21-book/ch12.md), seção *Standard Streams*.

---

<div align="center">

⬅️ [A5 · Processamento de dados e casting](./A5%20-%20Processamento%20de%20dados%20e%20casting.md) &nbsp;·&nbsp; 📂 [Seção 3](./README.md) &nbsp;·&nbsp; [A7 · Funções matemáticas em Java](./A7%20-%20Funcoes%20matematicas%20em%20Java.md) ➡️

</div>
