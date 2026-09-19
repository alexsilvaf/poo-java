# Parâmetros, retorno e passagem de valores

<sub>📚 [Documentação](../README.md) › [Seção 6 · Outros tópicos básicos sobre Java](./README.md) › Material 6 de 8</sub>

Os parâmetros recebem valores quando o método é chamado. Em Java, a passagem de argumentos ocorre **por valor**: o parâmetro recebe uma cópia do valor fornecido.

## Cópia de um valor primitivo

```java
public class PassagemValor {
    public static void main(String[] args) {
        int numero = 10;

        dobrarLocalmente(numero);

        System.out.println(numero); // 10
    }

    static void dobrarLocalmente(int valor) {
        valor *= 2;
        System.out.println(valor); // 20
    }
}
```

Alterar `valor` não altera `numero`. São variáveis diferentes. O parâmetro começa com uma cópia do valor 10.

Para que o chamador receba o cálculo, devolva o resultado:

```java
static int dobro(int valor) {
    return valor * 2;
}
```

```java
int numero = 10;
numero = dobro(numero);

System.out.println(numero); // 20
```

## Passagem de `String`

```java
public class Normalizacao {
    public static void main(String[] args) {
        String nome = "  Ana  ";

        normalizarLocalmente(nome);
        System.out.println("[" + nome + "]"); // [  Ana  ]

        nome = normalizar(nome);
        System.out.println("[" + nome + "]"); // [ANA]
    }

    static void normalizarLocalmente(String texto) {
        texto = texto.strip().toUpperCase();
    }

    static String normalizar(String texto) {
        return texto.strip().toUpperCase();
    }
}
```

O primeiro método muda apenas seu parâmetro local. Além disso, `String` é imutável: `strip` e `toUpperCase` produzem outro texto. O segundo método devolve o novo valor para que o `main` possa guardá-lo.

Referências mutáveis serão estudadas depois da criação de classes e objetos. A regra de linguagem continuará sendo passagem por valor; o que será copiado, naquele caso, é o valor da referência.

## Mais de um parâmetro

```java
static double aplicarDesconto(double preco, double percentual) {
    return preco * (1.0 - percentual);
}
```

```java
double final1 = aplicarDesconto(200.0, 0.10); // 180.0
double final2 = aplicarDesconto(80.0, 0.25);  // 60.0
```

Cada argumento precisa ser compatível com o tipo do parâmetro correspondente.

## `return` encerra o método

```java
static boolean ehPar(int numero) {
    return numero % 2 == 0;
}
```

Também é possível usar retorno antecipado:

```java
static String classificar(int nota) {
    if (nota < 0 || nota > 10) {
        return "invalida";
    }

    if (nota >= 7) {
        return "aprovado";
    }

    return "reprovado";
}
```

Depois que `return` executa, nenhuma instrução posterior daquele caminho é executada.

## Escopo dos parâmetros e variáveis locais

Um parâmetro existe apenas dentro do método:

```java
static int quadrado(int numero) {
    int resultado = numero * numero;
    return resultado;
}
```

Nem `numero` nem `resultado` podem ser usados pelo `main`. O `main` recebe somente o valor devolvido.

Métodos diferentes podem usar o mesmo nome de parâmetro sem conflito:

```java
static int dobro(int numero) {
    return numero * 2;
}

static int triplo(int numero) {
    return numero * 3;
}
```

## Compondo chamadas

O resultado de um método pode servir de argumento para outro:

```java
static int quadrado(int numero) {
    return numero * numero;
}

static int dobro(int numero) {
    return numero * 2;
}
```

```java
int resultado = dobro(quadrado(3)); // dobro(9), resultado 18
```

Leia de dentro para fora: primeiro `quadrado(3)`, depois `dobro(9)`.

## Referências

- [Java Language Specification 25 - Formal Parameters](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4.1).
- [Java Language Specification 25 - The return Statement](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.17).

---

<div align="center">

⬅️ [A5 · Métodos: declaração e chamada](./A5%20-%20Metodos%20declaracao%20e%20chamada.md) &nbsp;·&nbsp; 📂 [Seção 6](./README.md) &nbsp;·&nbsp; [A7 · Prática integrada](./A7%20-%20Pratica%20integrada.md) ➡️

</div>
