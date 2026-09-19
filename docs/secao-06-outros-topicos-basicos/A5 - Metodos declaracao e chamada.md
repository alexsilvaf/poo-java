# Métodos: declaração e chamada

<sub>📚 [Documentação](../README.md) › [Seção 6 · Outros tópicos básicos sobre Java](./README.md) › Material 5 de 8</sub>

Um método reúne instruções que realizam uma tarefa. Ele permite dar nome a uma operação e chamá-la sempre que for necessária.

Até aqui, todo o código foi escrito dentro de `main`. Considere o cálculo repetido:

```java
double media1 = (7.0 + 8.0) / 2.0;
double media2 = (5.5 + 9.0) / 2.0;
```

O cálculo pode receber um nome:

```java
static double calcularMedia(double primeira, double segunda) {
    return (primeira + segunda) / 2.0;
}
```

## Partes da declaração

| Trecho | Função |
| --- | --- |
| `static` | permite que o método seja chamado diretamente pelo `main` nesta etapa do curso |
| `double` | tipo do valor devolvido |
| `calcularMedia` | nome do método |
| `double primeira, double segunda` | parâmetros recebidos |
| `{ ... }` | corpo com as instruções |
| `return` | encerra o método e devolve um valor |

O significado completo de `static` será estudado na Seção 7, junto com membros de classe e de instância. Por enquanto, o `main` e os métodos auxiliares usam `static`.

## Declaração e chamada

Declarar define a operação. Chamar executa essa operação:

```java
double resultado = calcularMedia(7.0, 8.0);
```

Os valores `7.0` e `8.0` são **argumentos**. Durante a chamada, eles fornecem valores para os parâmetros `primeira` e `segunda`.

## Programa completo

```java
public class CalculadoraMedia {
    public static void main(String[] args) {
        double media = calcularMedia(7.0, 8.0);
        System.out.printf("Media: %.1f%n", media);
    }

    static double calcularMedia(double primeira, double segunda) {
        return (primeira + segunda) / 2.0;
    }
}
```

A execução segue esta sequência:

1. a JVM inicia pelo `main`;
2. o `main` chama `calcularMedia`;
3. o cálculo produz `7.5`;
4. `return` devolve esse valor;
5. `media` recebe o resultado;
6. o `printf` mostra a saída.

O método pode aparecer antes ou depois do `main` dentro da classe. Ele não pode ser declarado dentro de outro método.

## Métodos que não devolvem valor

Use `void` quando a tarefa apenas realiza uma ação:

```java
static void mostrarLinha() {
    System.out.println("--------------------");
}
```

Chamada:

```java
mostrarLinha();
```

Não tente guardar o resultado de um método `void`:

```java
// String linha = mostrarLinha(); // não compila
```

## Parâmetros precisam de tipo

```java
static int maior(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}
```

Cada parâmetro funciona como uma variável local e possui tipo e nome. A ordem dos argumentos precisa acompanhar a ordem dos parâmetros.

## Todo caminho precisa devolver o valor prometido

Este método não compila:

```java
static int sinal(int numero) {
    if (numero > 0) {
        return 1;
    }
    // falta retorno quando numero <= 0
}
```

Uma correção:

```java
static int sinal(int numero) {
    if (numero > 0) {
        return 1;
    }
    return -1;
}
```

Um método diferente pode devolver `0` para o caso de igualdade, mas essa é uma decisão do problema, não uma regra de sintaxe.

## Métodos pequenos e nomes claros

Um bom método costuma:

- executar uma tarefa bem definida;
- receber apenas os dados necessários;
- ter nome que descreve o resultado ou a ação;
- evitar depender de variáveis escondidas fora dele.

Compare `f(7, 8)` com `calcularMedia(7, 8)`. O segundo nome documenta a intenção da chamada.

## O que fica para depois

- métodos de instância e o uso de objetos;
- sobrecarga de métodos;
- parâmetros em quantidade variável (`varargs`);
- recursão e detalhes da pilha de chamadas;
- modificadores de acesso além do necessário nos exemplos.

## Referências

- [Java Language Specification 25 - Method Declarations](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4).
- [Java Language Specification 25 - Method Invocation Expressions](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.12).

---

<div align="center">

⬅️ [A4 · Comentários em Java](./A4%20-%20Comentarios%20em%20Java.md) &nbsp;·&nbsp; 📂 [Seção 6](./README.md) &nbsp;·&nbsp; [A6 · Parâmetros, retorno e passagem de valores](./A6%20-%20Parametros%20retorno%20e%20passagem%20de%20valores.md) ➡️

</div>
