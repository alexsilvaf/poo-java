# Estrutura switch-case

<sub>📚 [Documentação](../README.md) › [Seção 4 · Estrutura condicional](./README.md) › Material 5 de 8</sub>

Um encadeamento `if-else` pode comparar uma mesma variável com vários valores exatos:

```java
int dia = 2;

if (dia == 1) {
    System.out.println("Domingo");
} else if (dia == 2) {
    System.out.println("Segunda-feira");
} else if (dia == 3) {
    System.out.println("Terca-feira");
} else {
    System.out.println("Dia invalido");
}
```

Quando a decisão tem essa forma, `switch-case` organiza as alternativas pelo valor da variável.

## Estrutura básica

```java
int dia = 2;

switch (dia) {
    case 1:
        System.out.println("Domingo");
        break;
    case 2:
        System.out.println("Segunda-feira");
        break;
    case 3:
        System.out.println("Terca-feira");
        break;
    default:
        System.out.println("Dia invalido");
        break;
}
```

O funcionamento ocorre em etapas:

1. Java avalia a expressão entre parênteses, neste caso `dia`;
2. procura um `case` com o mesmo valor;
3. começa a executar a partir desse ponto;
4. o `break` encerra o `switch`;
5. se nenhum caso combinar, executa `default`.

`default` é opcional, mas é útil para entradas inválidas ou valores que não foram previstos.

## Por que o `break` é importante

Na sintaxe tradicional, sem `break`, a execução continua nos casos seguintes. Esse comportamento é chamado *fall-through*.

```java
int opcao = 1;

switch (opcao) {
    case 1:
        System.out.println("Cadastrar");
    case 2:
        System.out.println("Consultar");
    default:
        System.out.println("Sair");
}
```

Saída:

```text
Cadastrar
Consultar
Sair
```

O programa encontrou `case 1`, mas nada interrompeu o fluxo. Por isso, executou todos os rótulos abaixo dele. Enquanto o conteúdo é novo, termine cada alternativa com `break`.

## Agrupando valores

Às vezes, vários valores devem executar o mesmo bloco. Os casos podem ser agrupados de propósito:

```java
int mes = 2;

switch (mes) {
    case 1:
    case 2:
    case 3:
        System.out.println("Primeiro trimestre");
        break;
    case 4:
    case 5:
    case 6:
        System.out.println("Segundo trimestre");
        break;
    default:
        System.out.println("Mes fora do exemplo");
        break;
}
```

Os casos `1` e `2` não têm instruções nem `break`; eles encaminham a execução para o mesmo bloco do caso `3`.

## Tipos adequados nesta etapa

Para os exemplos do curso, use `switch` com:

- `int` e tipos inteiros menores;
- `char`;
- `String`.

```java
char conceito = 'B';

switch (conceito) {
    case 'A':
        System.out.println("Excelente");
        break;
    case 'B':
        System.out.println("Bom");
        break;
    default:
        System.out.println("Conceito nao reconhecido");
        break;
}
```

Um `case` deve usar um valor constante e compatível com o tipo selecionado. Não se escreve uma comparação depois de `case`:

```java
// case idade >= 18: // não é assim que switch tradicional funciona
```

Para intervalos, continue usando `if-else`.

## Sintaxe com setas

Java moderno também aceita uma forma de `switch` que usa `->` e não continua no próximo caso:

```java
int dia = 2;

switch (dia) {
    case 1 -> System.out.println("Domingo");
    case 2 -> System.out.println("Segunda-feira");
    case 3 -> System.out.println("Terca-feira");
    default -> System.out.println("Dia invalido");
}
```

Essa forma elimina o `break` e o *fall-through*. O curso começa pela forma tradicional porque ela aparece em muitos códigos e porque entender o `break` será útil nas estruturas repetitivas. A forma com setas é apresentada apenas para reconhecimento.

## `switch` ou `if-else`?

| Situação | Estrutura mais direta |
| --- | --- |
| comparar uma variável com valores exatos | `switch` |
| testar faixas, como `nota >= 6` | `if-else` |
| combinar condições com `&&` e `||` | `if-else` |
| ter apenas dois caminhos simples | normalmente `if-else` |
| montar um menu numérico | `switch` |

As duas estruturas resolvem muitas das mesmas decisões. A escolha deve favorecer a leitura.

## Um programa completo

```java
import java.util.Scanner;

public class Menu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("1 - Somar dois numeros");
        System.out.println("2 - Calcular o dobro");
        System.out.println("0 - Sair");
        System.out.print("Opcao: ");
        int opcao = sc.nextInt();

        switch (opcao) {
            case 1: {
                System.out.print("Digite dois numeros: ");
                double a = sc.nextDouble();
                double b = sc.nextDouble();
                System.out.println("Soma: " + (a + b));
                break;
            }
            case 2: {
                System.out.print("Digite um numero: ");
                double numero = sc.nextDouble();
                System.out.println("Dobro: " + (numero * 2));
                break;
            }
            case 0: {
                System.out.println("Programa encerrado.");
                break;
            }
            default: {
                System.out.println("Opcao invalida.");
                break;
            }
        }

        sc.close();
    }
}
```

As chaves adicionais fazem as variáveis `a`, `b` e `numero` existirem apenas dentro de seus respectivos casos. Esse assunto será organizado no material sobre escopo.

## Referências

- [OCPJ21 Study Guide - Chapter 5: Making Decisions](../ocpj21-book/ch05.md), seção *The switch Statement*.
- [Java Language Specification 25 - The switch Statement](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.11).

---

<div align="center">

⬅️ [A4 · Operadores de atribuição cumulativa](./A4%20-%20Operadores%20de%20atribuicao%20cumulativa.md) &nbsp;·&nbsp; 📂 [Seção 4](./README.md) &nbsp;·&nbsp; [A6 · Expressão condicional ternária](./A6%20-%20Expressao%20condicional%20ternaria.md) ➡️

</div>
