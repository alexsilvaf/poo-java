# Teste de mesa com while

<sub>📚 [Documentação](../README.md) › [Seção 5 · Estruturas repetitivas](./README.md) › Material 3 de 8</sub>

O teste de mesa simula o programa no papel. Com uma repetição, ele precisa registrar cada passagem pela condição e cada execução do corpo.

## Como montar a tabela

Para este código:

```java
int x = 1;
int soma = 0;

while (x <= 4) {
    soma += x;
    x++;
}

System.out.println(soma);
```

Siga sempre a ordem real:

1. anote os valores iniciais;
2. avalie a condição;
3. se for verdadeira, execute as linhas do corpo na ordem;
4. volte à condição;
5. pare quando ela for falsa.

| Chegada à condição | `x` | `soma` | `x <= 4` | Ação |
| ---: | ---: | ---: | :---: | --- |
| 1ª | 1 | 0 | `true` | soma recebe 1; x recebe 2 |
| 2ª | 2 | 1 | `true` | soma recebe 3; x recebe 3 |
| 3ª | 3 | 3 | `true` | soma recebe 6; x recebe 4 |
| 4ª | 4 | 6 | `true` | soma recebe 10; x recebe 5 |
| 5ª | 5 | 10 | `false` | sai do laço |

A saída é `10`. O corpo executa quatro vezes, mas a condição é avaliada cinco.

## Registre o momento do valor

Este código imprime antes de incrementar:

```java
int x = 1;

while (x <= 3) {
    System.out.println(x);
    x++;
}
```

Por isso, imprime `1`, `2` e `3`. Se a ordem mudar, a saída muda:

```java
int x = 1;

while (x <= 3) {
    x++;
    System.out.println(x);
}
```

Agora imprime `2`, `3` e `4`. A condição ainda foi verdadeira para `x = 3`, mas o incremento ocorreu antes da saída.

## Contando valores que atendem a uma condição

```java
int numero = 1;
int quantidadePares = 0;

while (numero <= 6) {
    if (numero % 2 == 0) {
        quantidadePares++;
    }
    numero++;
}
```

| Iteração | `numero` | É par? | `quantidadePares` depois do `if` |
| ---: | ---: | :---: | ---: |
| 1 | 1 | não | 0 |
| 2 | 2 | sim | 1 |
| 3 | 3 | não | 1 |
| 4 | 4 | sim | 2 |
| 5 | 5 | não | 2 |
| 6 | 6 | sim | 3 |

O contador só muda quando a condição interna é verdadeira. `numero`, por outro lado, precisa mudar em toda iteração.

## Entrada com sentinela

Considere as entradas `5`, `2`, `7` e `0`:

```java
int soma = 0;
int quantidade = 0;

int numero = sc.nextInt();

while (numero != 0) {
    soma += numero;
    quantidade++;
    numero = sc.nextInt();
}
```

| Valor lido | `numero != 0` | `soma` | `quantidade` | Ação seguinte |
| ---: | :---: | ---: | ---: | --- |
| 5 | `true` | 5 | 1 | lê 2 |
| 2 | `true` | 7 | 2 | lê 7 |
| 7 | `true` | 14 | 3 | lê 0 |
| 0 | `false` | 14 | 3 | encerra |

A sentinela `0` não é processada porque a condição é verificada antes do corpo.

## Calculando uma média

A média exige soma e quantidade:

```java
int soma = 0;
int quantidade = 0;
int numero = sc.nextInt();

while (numero != 0) {
    soma += numero;
    quantidade++;
    numero = sc.nextInt();
}

if (quantidade > 0) {
    double media = (double) soma / quantidade;
    System.out.println(media);
} else {
    System.out.println("Nenhum valor informado.");
}
```

O `if` evita dividir por zero quando a primeira entrada já é a sentinela. O casting força a divisão real.

## Encontrando um erro com o teste de mesa

```java
int x = 1;
int soma = 0;

while (x <= 3) {
    soma = x;
    x++;
}
```

| Iteração | `x` usado | `soma` depois de `soma = x` |
| ---: | ---: | ---: |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |

Se a intenção era somar `1 + 2 + 3`, o resultado deveria ser `6`. A tabela mostra o problema: `soma = x` substitui o valor anterior. O correto é `soma += x`.

## Checklist do teste de mesa

- Liste todas as variáveis que mudam.
- Anote os valores antes da primeira condição.
- Crie uma linha por chegada à condição ou por iteração e mantenha um padrão.
- Registre `true` ou `false` para cada teste.
- Atualize as variáveis na ordem exata do código.
- Inclua a última condição falsa.
- Confira a saída somente depois de encerrar a repetição.

## Prática guiada

Faça o teste de mesa sem executar:

```java
int x = 10;
int quantidade = 0;

while (x > 1) {
    x /= 2;
    quantidade++;
}

System.out.println(x + " " + quantidade);
```

<details>
<summary><b>💡 Resposta</b></summary>

| Iteração | `x` antes | `x` depois de `/= 2` | `quantidade` |
| ---: | ---: | ---: | ---: |
| 1 | 10 | 5 | 1 |
| 2 | 5 | 2 | 2 |
| 3 | 2 | 1 | 3 |

A condição seguinte é falsa, e a saída é `1 3`. A divisão é inteira.
</details>

## Referências

- [OCPJ21 Study Guide - Chapter 5: Making Decisions](../ocpj21-book/ch05.md), seção *The while Loop*.

---

<div align="center">

⬅️ [A2 · Estrutura repetitiva while](./A2%20-%20Estrutura%20repetitiva%20while.md) &nbsp;·&nbsp; 📂 [Seção 5](./README.md) &nbsp;·&nbsp; [A4 · Estrutura repetitiva for](./A4%20-%20Estrutura%20repetitiva%20for.md) ➡️

</div>
