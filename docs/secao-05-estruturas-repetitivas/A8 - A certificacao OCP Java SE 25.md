# A certificação OCP Java SE 25 e esta seção

<sub>📚 [Documentação](../README.md) › [Seção 5 · Estruturas repetitivas](./README.md) › Material 8 de 8</sub>

Este material relaciona a Seção 5 com a certificação **Oracle Certified Professional, Java SE 25 Developer** (exame **1Z0-831**). Os exemplos usam somente decisões e repetições estudadas até aqui.

## Grupo de objetivos relacionado

| Grupo de objetivos | Conteúdo desta seção |
| --- | --- |
| Implementing Program Flow Control | `while`, `do-while`, `for`, laços aninhados, `break` e `continue` |
| Applying Object-Oriented Principles | escopo e inicialização das variáveis de controle |

## O que desta seção cai na prova

### `while` e `do-while`

É necessário prever:

- que `while` testa antes e pode executar zero vezes;
- que `do-while` testa depois e executa pelo menos uma vez;
- que as condições precisam produzir `boolean`;
- que o ponto e vírgula final faz parte da sintaxe do `do-while`;
- que um ponto e vírgula logo depois de `while (condicao)` cria um corpo vazio;
- como a atualização da variável faz o laço terminar.

### `for` tradicional

- a inicialização acontece uma vez;
- a condição é verificada antes de cada iteração;
- a atualização acontece depois do corpo;
- as três partes podem ser omitidas, mas os dois pontos e vírgulas permanecem;
- sem condição, o `for` se comporta como um laço infinito;
- uma variável declarada na inicialização fica limitada ao `for`;
- inicialização e atualização podem conter mais de uma expressão compatível.

O `for-each` também faz parte do exame, mas depende de arrays ou coleções. Ele será estudado quando esses conteúdos aparecerem no curso e não é pré-requisito desta seção.

### `break` e `continue`

- `break` encerra o laço mais interno;
- `continue` encerra a iteração atual;
- em um `for`, `continue` ainda leva à etapa de atualização;
- em um `while`, `continue` volta diretamente à condição;
- código colocado imediatamente depois de um `break` ou `continue` incondicional no mesmo bloco não pode ser alcançado.

### Escopo e inicialização

- o contador declarado no cabeçalho do `for` não existe depois do laço;
- uma variável declarada dentro do corpo não existe fora dele;
- um `while` pode executar zero vezes, então uma atribuição apenas dentro dele não garante inicialização para uso posterior;
- o `do-while` executa o corpo ao menos uma vez, mas a variável usada na condição precisa estar em escopo.

## O que é ferramenta didática

O depurador do Eclipse e o teste de mesa não são objetivos isolados do exame. Eles treinam a habilidade que a prova mais exige nesta parte: simular a ordem exata de execução e prever valores e saída.

## Questões no estilo da prova

**1. Qual é a saída?**

```java
int x = 1;

while (x < 4) {
    System.out.print(x + " ");
    x++;
}
```

<details>
<summary><b>💡 Resposta</b></summary>

`1 2 3 `. Quando `x` chega a 4, a condição fica falsa.
</details>

**2. Quantas vezes o corpo executa?**

```java
int x = 10;

while (x < 5) {
    x++;
}
```

<details>
<summary><b>💡 Resposta</b></summary>

Zero vezes. `while` testa a condição antes do corpo.
</details>

**3. Qual é a saída?**

```java
int x = 10;

do {
    System.out.print(x);
    x++;
} while (x < 5);
```

<details>
<summary><b>💡 Resposta</b></summary>

`10`. O corpo executa uma vez antes da primeira condição.
</details>

**4. Qual é a saída?**

```java
for (int i = 0; i < 5; i += 2) {
    System.out.print(i + " ");
}
```

<details>
<summary><b>💡 Resposta</b></summary>

`0 2 4 `. Depois de imprimir 4, a atualização leva `i` a 6 e a condição fica falsa.
</details>

**5. O código compila?**

```java
for (int i = 1; i <= 3; i++) {
    System.out.println(i);
}

System.out.println(i);
```

<details>
<summary><b>💡 Resposta</b></summary>

Não. `i` foi declarado no cabeçalho do `for` e está fora de escopo depois do laço.
</details>

**6. Qual é a saída?**

```java
int soma = 0;

for (int i = 1; i <= 5; i++) {
    if (i == 3) {
        continue;
    }
    soma += i;
}

System.out.println(soma);
```

<details>
<summary><b>💡 Resposta</b></summary>

`12`. O valor 3 é pulado; a soma é `1 + 2 + 4 + 5`.
</details>

**7. Qual é a saída?**

```java
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        if (j == 2) {
            break;
        }
        System.out.print(i + "" + j + " ");
    }
}
```

<details>
<summary><b>💡 Resposta</b></summary>

`11 21 31 `. O `break` encerra somente o `for` de `j`; o laço de `i` continua.
</details>

**8. O que acontece?**

```java
int x = 1;

while (x <= 3); {
    x++;
}
```

<details>
<summary><b>💡 Resposta</b></summary>

O programa fica no laço vazio `while (x <= 3);`. Como `x` não muda dentro desse laço, o bloco seguinte nunca é alcançado.
</details>

**9. O código compila?**

```java
boolean executar = false;
int resultado;

while (executar) {
    resultado = 10;
}

System.out.println(resultado);
```

<details>
<summary><b>💡 Resposta</b></summary>

Não. Um `while` pode executar zero vezes, então `resultado` não está definitivamente inicializado antes da impressão.
</details>

**10. Qual é a saída?**

```java
int i = 0;

for (; i < 3; ) {
    System.out.print(i + " ");
    i++;
}

System.out.println(i);
```

<details>
<summary><b>💡 Resposta</b></summary>

`0 1 2 3`. A variável foi declarada antes do `for`, então continua em escopo e vale 3 depois do laço.
</details>

## Referências

- [OCPJ21 Study Guide - Chapter 5: Making Decisions](../ocpj21-book/ch05.md)
- [Java Language Specification 25 - The while Statement](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.12)
- [Java Language Specification 25 - The do Statement](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.13)
- [Java Language Specification 25 - The for Statement](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.14)
- [Certificação Oracle Certified Professional, Java SE 25 Developer](https://education.oracle.com/java-se-25-developer-professional/pexam_1Z0-831)

---

<div align="center">

⬅️ [A7 · Escolhendo a estrutura de repetição](./A7%20-%20Escolhendo%20a%20estrutura%20de%20repeticao.md) &nbsp;·&nbsp; 📂 [Seção 5](./README.md) &nbsp;·&nbsp; [Seção 6 · Outros tópicos básicos sobre Java](../secao-06-outros-topicos-basicos/README.md) ➡️

</div>
