# Teste de mesa com for

<sub>📚 [Documentação](../README.md) › [Seção 5 · Estruturas repetitivas](./README.md) › Material 5 de 8</sub>

O teste de mesa de um `for` precisa respeitar uma ordem específica: inicialização, condição, corpo, atualização e nova condição.

## Exemplo básico

```java
int soma = 0;

for (int i = 1; i <= 4; i++) {
    soma += i;
}

System.out.println(soma);
```

| Etapa | `i` | `soma` | `i <= 4` | Ação |
| --- | ---: | ---: | :---: | --- |
| inicialização | 1 | 0 | - | prepara o laço |
| 1ª condição | 1 | 0 | `true` | soma recebe 1 |
| atualização | 2 | 1 | - | executa `i++` |
| 2ª condição | 2 | 1 | `true` | soma recebe 3 |
| atualização | 3 | 3 | - | executa `i++` |
| 3ª condição | 3 | 3 | `true` | soma recebe 6 |
| atualização | 4 | 6 | - | executa `i++` |
| 4ª condição | 4 | 6 | `true` | soma recebe 10 |
| atualização | 5 | 10 | - | executa `i++` |
| 5ª condição | 5 | 10 | `false` | encerra |

A saída é `10`. A inicialização acontece uma vez, mas condição e atualização participam do ciclo.

## Forma compacta da tabela

Depois de dominar a ordem, a mesma execução pode ser resumida por iteração:

| Iteração | `i` usado no corpo | `soma` depois do corpo |
| ---: | ---: | ---: |
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |
| 4 | 4 | 10 |

Anote também que, ao final, `i` seria `5`, embora a variável esteja fora de escopo depois do `for`.

## Prevendo a quantidade de repetições

```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}
```

Os valores usados no corpo são `0`, `1`, `2`, `3` e `4`: cinco repetições. A condição `i < 5` exclui o 5, mas inclui o 0.

Compare:

| Cabeçalho | Valores usados | Repetições |
| --- | --- | ---: |
| `for (int i = 1; i <= 5; i++)` | 1, 2, 3, 4, 5 | 5 |
| `for (int i = 1; i < 5; i++)` | 1, 2, 3, 4 | 4 |
| `for (int i = 0; i < 5; i++)` | 0, 1, 2, 3, 4 | 5 |
| `for (int i = 0; i <= 5; i++)` | 0, 1, 2, 3, 4, 5 | 6 |

## Passo diferente de 1

```java
int soma = 0;

for (int i = 2; i <= 8; i += 2) {
    soma += i;
}
```

| Iteração | `i` | `soma` |
| ---: | ---: | ---: |
| 1 | 2 | 2 |
| 2 | 4 | 6 |
| 3 | 6 | 12 |
| 4 | 8 | 20 |

Depois da quarta atualização, `i` vira `10` e a condição fica falsa.

## Contagem regressiva

```java
for (int i = 5; i >= 1; i--) {
    System.out.println(i);
}
```

| Iteração | `i` impresso | `i` após `i--` |
| ---: | ---: | ---: |
| 1 | 5 | 4 |
| 2 | 4 | 3 |
| 3 | 3 | 2 |
| 4 | 2 | 1 |
| 5 | 1 | 0 |

Com `i = 0`, a condição `i >= 1` é falsa e o laço termina.

## Condição interna

```java
int somaPares = 0;

for (int i = 1; i <= 6; i++) {
    if (i % 2 == 0) {
        somaPares += i;
    }
}
```

| `i` | `i % 2 == 0` | `somaPares` |
| ---: | :---: | ---: |
| 1 | `false` | 0 |
| 2 | `true` | 2 |
| 3 | `false` | 2 |
| 4 | `true` | 6 |
| 5 | `false` | 6 |
| 6 | `true` | 12 |

O `for` controla quais números são visitados; o `if` controla quais entram na soma.

## Duas variáveis de controle

```java
for (int a = 1, b = 5; a <= b; a++, b--) {
    System.out.println(a + " " + b);
}
```

| Iteração | `a` | `b` | Saída |
| ---: | ---: | ---: | --- |
| 1 | 1 | 5 | `1 5` |
| 2 | 2 | 4 | `2 4` |
| 3 | 3 | 3 | `3 3` |

Depois da terceira atualização, `a` vale `4` e `b` vale `2`; a condição `a <= b` fica falsa.

## Laços aninhados

```java
for (int linha = 1; linha <= 2; linha++) {
    for (int coluna = 1; coluna <= 3; coluna++) {
        System.out.println(linha + " " + coluna);
    }
}
```

| `linha` | `coluna` | Saída |
| ---: | ---: | --- |
| 1 | 1 | `1 1` |
| 1 | 2 | `1 2` |
| 1 | 3 | `1 3` |
| 2 | 1 | `2 1` |
| 2 | 2 | `2 2` |
| 2 | 3 | `2 3` |

Para cada iteração externa, o laço interno começa novamente em `coluna = 1`. O total é `2 * 3 = 6` execuções do corpo interno.

## Erros típicos encontrados pela tabela

| Sintoma | Verificação |
| --- | --- |
| uma repetição a menos | o limite deveria usar `<=` em vez de `<`? |
| uma repetição a mais | o contador começou cedo demais ou o limite incluiu um valor extra? |
| laço infinito | a atualização aproxima o contador do fim? |
| contador fora do esperado | a atualização ocorre também dentro do corpo? |
| soma errada | o acumulador começou em 0 e usa `+=`? |

## Prática guiada

```java
int resultado = 1;

for (int i = 1; i <= 4; i++) {
    resultado *= 2;
}

System.out.println(resultado);
```

<details>
<summary><b>💡 Resposta</b></summary>

`resultado` assume `2`, `4`, `8` e `16`. A saída é `16`. O acumulador multiplicativo começa em `1`, o elemento neutro da multiplicação.
</details>

## Referências

- [OCPJ21 Study Guide - Chapter 5: Making Decisions](../ocpj21-book/ch05.md), seção *The for Loop*.

---

<div align="center">

⬅️ [A4 · Estrutura repetitiva for](./A4%20-%20Estrutura%20repetitiva%20for.md) &nbsp;·&nbsp; 📂 [Seção 5](./README.md) &nbsp;·&nbsp; [A6 · Estrutura repetitiva do-while](./A6%20-%20Estrutura%20repetitiva%20do-while.md) ➡️

</div>
