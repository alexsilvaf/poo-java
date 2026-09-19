# Escolhendo a estrutura de repetição

<sub>📚 [Documentação](../README.md) › [Seção 5 · Estruturas repetitivas](./README.md) › Material 7 de 8</sub>

`while`, `for` e `do-while` repetem instruções. A principal diferença está em **quando** a condição é testada e em **como** o controle da repetição aparece no código.

## Comparação direta

| Estrutura | Teste da condição | Execuções mínimas | Uso mais natural |
| --- | --- | ---: | --- |
| `while` | antes do corpo | 0 | quantidade desconhecida, sentinela ou validação |
| `for` | antes do corpo | 0 | contador e quantidade conhecida de repetições |
| `do-while` | depois do corpo | 1 | menu ou ação que precisa ocorrer antes do teste |

As três estruturas conseguem resolver muitos dos mesmos problemas. A melhor escolha é a que deixa o controle mais visível.

## Mesmo problema com `while` e `for`

Com `while`:

```java
int i = 1;

while (i <= 5) {
    System.out.println(i);
    i++;
}
```

Com `for`:

```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}
```

Quando inicialização, condição e atualização giram em torno do mesmo contador, o `for` concentra o controle em uma linha.

## Problema mais natural com `while`

```java
System.out.print("Digite 0 para sair: ");
int numero = sc.nextInt();

while (numero != 0) {
    System.out.println("Dobro: " + (numero * 2));
    System.out.print("Digite outro numero ou 0 para sair: ");
    numero = sc.nextInt();
}
```

Não se sabe quantos números serão digitados. A condição depende da entrada, e não de uma contagem prevista.

## Problema mais natural com `do-while`

```java
int opcao;

do {
    System.out.println("1 - Continuar");
    System.out.println("0 - Sair");
    opcao = sc.nextInt();
} while (opcao != 0);
```

O menu precisa aparecer antes que exista uma escolha para testar.

## `break`: encerrar o laço

`break` termina imediatamente o laço mais interno que o contém. O programa continua na primeira instrução depois da repetição.

```java
int numero = 1;

while (numero <= 10) {
    if (numero == 4) {
        break;
    }

    System.out.println(numero);
    numero++;
}

System.out.println("Fim");
```

Saída:

```text
1
2
3
Fim
```

Quando `numero` chega a 4, o `break` encerra o `while` antes da impressão.

Um uso comum é combinar laço infinito com uma condição explícita de saída:

```java
while (true) {
    int numero = sc.nextInt();

    if (numero == 0) {
        break;
    }

    System.out.println("Dobro: " + (numero * 2));
}
```

Essa forma é válida, mas o laço `while (numero != 0)` costuma deixar a regra de continuidade mais visível para iniciantes.

## `continue`: pular o restante da iteração

`continue` encerra somente a iteração atual e parte para a próxima.

```java
for (int i = 1; i <= 6; i++) {
    if (i % 2 == 0) {
        continue;
    }

    System.out.println(i);
}
```

Saída:

```text
1
3
5
```

Nos valores pares, `continue` pula o `println`. No `for`, a atualização `i++` ainda ocorre antes da próxima condição.

## Cuidado com `continue` em `while`

No `while`, a atualização costuma estar no corpo. Se `continue` vier antes dela, o laço pode ficar preso:

```java
int i = 1;

while (i <= 5) {
    if (i == 3) {
        continue; // i continua valendo 3 para sempre
    }

    System.out.println(i);
    i++;
}
```

Uma correção é atualizar antes da decisão:

```java
int i = 0;

while (i < 5) {
    i++;

    if (i == 3) {
        continue;
    }

    System.out.println(i);
}
```

Saída: `1`, `2`, `4`, `5`.

## Quando não usar `break` ou `continue`

Às vezes, a própria condição expressa melhor o fim:

```java
int numero = sc.nextInt();

while (numero != 0) {
    System.out.println(numero);
    numero = sc.nextInt();
}
```

É mais direto que usar `while (true)` e um `break` escondido no meio de um corpo longo. Use transferências de fluxo quando elas simplificarem a leitura, não apenas para reduzir linhas.

## Laços aninhados

Em laços aninhados, `break` e `continue` sem rótulo afetam apenas o laço mais interno.

```java
for (int linha = 1; linha <= 3; linha++) {
    for (int coluna = 1; coluna <= 3; coluna++) {
        if (coluna == 2) {
            break;
        }
        System.out.println(linha + " " + coluna);
    }
}
```

Para cada linha, o laço interno imprime apenas a coluna 1 e termina ao chegar à coluna 2. O laço externo continua com a linha seguinte.

Recursos para sair de vários níveis existem, mas ficam fora deste primeiro contato. Estruturar laços pequenos evita essa necessidade na maioria dos exercícios iniciais.

## Decisão guiada

Pergunte na ordem:

1. **O corpo precisa executar ao menos uma vez?** Se sim, considere `do-while`.
2. **Existe um contador com início, limite e passo claros?** Se sim, considere `for`.
3. **O fim depende de uma condição ou entrada sem quantidade conhecida?** Se sim, considere `while`.

Depois confira:

- a condição pode começar falsa?
- alguma variável precisa mudar para que o laço termine?
- o limite é inclusivo ou exclusivo?
- a atualização acontece mesmo quando há `continue`?
- uma sentinela deve ser processada ou apenas encerrar?

## Exercício de classificação

Escolha a estrutura mais natural:

| Problema | Escolha sugerida | Motivo |
| --- | --- | --- |
| imprimir de 1 a 20 | `for` | quantidade e contador conhecidos |
| somar números até o usuário digitar 0 | `while` | quantidade desconhecida e sentinela |
| mostrar um menu até escolher sair | `do-while` | menu precisa aparecer ao menos uma vez |
| repetir exatamente 5 leituras | `for` | quantidade fixa |
| pedir novamente enquanto a nota for inválida | `while` ou `do-while` | depende de como a primeira leitura é organizada |

## Referências

- [OCPJ21 Study Guide - Chapter 5: Making Decisions](../ocpj21-book/ch05.md), seções *The while Loop* e *The for Loop*.
- [Java Language Specification 25 - The break Statement](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.15).
- [Java Language Specification 25 - The continue Statement](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.16).

---

<div align="center">

⬅️ [A6 · Estrutura repetitiva do-while](./A6%20-%20Estrutura%20repetitiva%20do-while.md) &nbsp;·&nbsp; 📂 [Seção 5](./README.md) &nbsp;·&nbsp; [A8 · A certificação OCP Java SE 25 e esta seção](./A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md) ➡️

</div>
