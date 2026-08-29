# As três operações básicas de programação

Por mais complexo que um sistema pareça, ele é construído sobre três operações elementares:

![As três operações básicas](./operacoes-basicas.svg)

1. **Entrada de dados** — trazer para dentro do programa informações que vêm de fora: teclado, arquivo, rede, sensor.
2. **Processamento de dados** — calcular, transformar e guardar resultados em variáveis.
3. **Saída de dados** — devolver o resultado para o mundo: tela, arquivo, resposta de rede.

## Estrutura sequencial

Esta seção trata da **estrutura sequencial**: as instruções são executadas **uma após a outra, de cima para baixo**, sem desvios e sem repetições. É a estrutura mais simples das três que o curso vai estudar:

| Estrutura | O que faz | Onde é estudada |
|---|---|---|
| **Sequencial** | executa tudo em ordem, uma vez | Seção 3 |
| Condicional | escolhe entre caminhos alternativos | Seção 4 |
| Repetitiva | repete um trecho enquanto valer uma condição | Seção 5 |

## O programa completo, na ordem

```java
package curso;

import java.util.Scanner;

public class MediaAluno {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. ENTRADA
        System.out.print("Nome do aluno: ");
        String nome = sc.nextLine();
        System.out.print("Primeira nota: ");
        double nota1 = sc.nextDouble();
        System.out.print("Segunda nota: ");
        double nota2 = sc.nextDouble();

        // 2. PROCESSAMENTO
        double media = (nota1 + nota2) / 2.0;

        // 3. SAÍDA
        System.out.printf("%s obteve media %.2f%n", nome, media);

        sc.close();
    }
}
```

Esse esqueleto — ler, calcular, mostrar — vai se repetir em praticamente todos os exercícios da seção.

## Nem todo programa tem as três

- Um programa que só imprime "Olá, mundo!" tem **apenas saída**.
- Um programa que calcula a área de um retângulo com medidas fixas no código tem **processamento e saída**.
- Um programa que pede as medidas ao usuário tem **as três**.

O que praticamente nunca existe é um programa **sem saída**: se ele não devolve nada, não há como saber que funcionou.

## Ordem importa

Como a execução é sequencial, trocar a ordem das instruções muda o resultado ou impede a compilação:

```java
double media = (nota1 + nota2) / 2.0;   // erro: nota1 e nota2 ainda não existem
double nota1 = 7.0;
double nota2 = 8.0;
```

```java
int x = 5;
x = x + 3;
System.out.println(x);   // 8

int y = 5;
System.out.println(y);   // 5  — imprimiu antes de somar
y = y + 3;
```

> Uma variável só pode ser usada **depois** de declarada e inicializada. Essa é uma consequência direta da execução sequencial, e é o primeiro modelo mental que o aluno precisa formar.

## Teste de mesa

Antes de rodar o programa, vale simular a execução no papel, linha a linha, anotando o valor de cada variável. Essa técnica se chama **teste de mesa**, e é a forma mais barata de encontrar um erro de lógica:

```java
int a = 10;
int b = 3;
int c = a / b;
a = c + b;
```

| Linha | `a` | `b` | `c` |
|---|---:|---:|---:|
| `int a = 10;` | 10 | — | — |
| `int b = 3;` | 10 | 3 | — |
| `int c = a / b;` | 10 | 3 | 3 |
| `a = c + b;` | 6 | 3 | 3 |

Repare que `c` vale `3`, e não `3.33`: a divisão entre dois `int` é inteira, como visto no material [A2](./A2%20-%20Expressoes%20aritmeticas.md).

O teste de mesa volta a aparecer na Seção 5, junto com o depurador do Eclipse.
