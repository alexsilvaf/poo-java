# Escopo e inicialização

<sub>📚 [Documentação](../README.md) › [Seção 4 · Estrutura condicional](./README.md) › Material 7 de 8</sub>

O **escopo** indica em qual parte do código um nome pode ser usado. A **inicialização** garante que a variável possui um valor antes da leitura. As duas ideias se encontram com frequência dentro de estruturas condicionais.

## Blocos criam escopos

Um bloco é um trecho entre chaves `{ }`. Uma variável local declarada dentro dele deixa de existir para o código que vem depois do fechamento.

```java
int idade = 20;

if (idade >= 18) {
    String mensagem = "Maior de idade";
    System.out.println(mensagem); // funciona
}

// System.out.println(mensagem); // erro: mensagem não existe aqui
```

`idade` foi declarada fora do `if`, então pode ser lida dentro e depois dele. `mensagem` nasceu no bloco do `if` e só pode ser usada ali.

## Blocos internos enxergam o lado de fora

```java
int numero = 10;

if (numero > 0) {
    int dobro = numero * 2;
    System.out.println(dobro);
}
```

O bloco interno enxerga `numero`, que foi declarado no bloco externo. O contrário não acontece: o bloco externo não enxerga `dobro` depois que o `if` termina.

## Não redeclare o mesmo nome em um bloco sobreposto

```java
int valor = 10;

if (valor > 0) {
    // int valor = 20; // erro: valor já está no escopo
    valor = 20;        // atribuir um novo valor é permitido
}
```

Java impede duas variáveis locais com o mesmo nome em escopos que se sobrepõem. Isso evita que uma declaração esconda a outra durante a leitura do método.

## Declarar não é inicializar

```java
int quantidade;      // declaração
quantidade = 5;      // primeira atribuição: inicialização
System.out.println(quantidade);
```

Uma variável local precisa estar **definitivamente inicializada** antes de ser lida. O compilador verifica todos os caminhos possíveis.

```java
int idade = 20;
String categoria;

if (idade >= 18) {
    categoria = "adulto";
}

// System.out.println(categoria); // erro: talvez o if não execute
```

Mesmo que `idade` valha `20` neste exemplo, a regra considera a estrutura do fluxo. Como não existe um `else`, há um caminho em que `categoria` continua sem valor.

## Inicialização nos dois caminhos

```java
int idade = 20;
String categoria;

if (idade >= 18) {
    categoria = "adulto";
} else {
    categoria = "menor";
}

System.out.println(categoria); // compila
```

Agora todo caminho que chega à saída atribuiu um valor a `categoria`.

Outra solução é fornecer um valor inicial antes da condição:

```java
String categoria = "menor";

if (idade >= 18) {
    categoria = "adulto";
}
```

Escolha um valor inicial apenas quando ele for verdadeiro para o problema. Não use valores inventados somente para silenciar o compilador.

## Variáveis em caminhos diferentes

Cada bloco possui seu próprio escopo:

```java
int numero = 5;

if (numero >= 0) {
    int resultado = numero * 2;
    System.out.println(resultado);
} else {
    int resultado = numero * -1;
    System.out.println(resultado);
}
```

As duas declarações de `resultado` são permitidas porque os blocos do `if` e do `else` não se sobrepõem. Nenhuma delas existe depois da estrutura.

Se o resultado precisa ser usado depois, declare a variável antes e atribua dentro dos caminhos:

```java
int numero = -5;
int resultado;

if (numero >= 0) {
    resultado = numero * 2;
} else {
    resultado = numero * -1;
}

System.out.println(resultado);
```

## Escopo no `switch`

Na forma tradicional, todos os `case` pertencem ao bloco do `switch`. Chaves adicionais tornam o escopo de cada caso explícito:

```java
int opcao = 1;

switch (opcao) {
    case 1: {
        int valor = 10;
        System.out.println(valor);
        break;
    }
    case 2: {
        int valor = 20; // permitido: está em outro bloco
        System.out.println(valor);
        break;
    }
    default: {
        System.out.println("Opcao invalida");
        break;
    }
}
```

Sem as chaves extras, uma variável declarada em um caso pode continuar em escopo nos casos seguintes, embora talvez não esteja inicializada. Para quem está começando, um bloco por caso evita essa confusão.

## Escopo não é tempo de vida do programa inteiro

Neste momento, basta usar o modelo prático:

- a variável passa a poder ser referenciada a partir de sua declaração;
- permanece acessível até o fim do bloco em que foi declarada;
- blocos internos podem ler variáveis dos blocos externos;
- ao sair do bloco, o nome deixa de estar disponível.

Detalhes de atributos, objetos e memória serão retomados quando o curso entrar em orientação a objetos.

## Um programa completo

```java
import java.util.Scanner;

public class Reajuste {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Salario atual: ");
        double salario = sc.nextDouble();
        double percentual;

        if (salario <= 2000.0) {
            percentual = 10.0;
        } else if (salario <= 5000.0) {
            percentual = 7.5;
        } else {
            percentual = 5.0;
        }

        double aumento = salario * percentual / 100.0;
        double novoSalario = salario + aumento;

        System.out.printf("Percentual: %.1f%%%n", percentual);
        System.out.printf("Novo salario: %.2f%n", novoSalario);

        sc.close();
    }
}
```

`percentual` é declarado antes da estrutura porque será usado depois. O encadeamento cobre todos os caminhos, então o compilador sabe que ele sempre recebe um valor.

## Erros comuns

| Mensagem ou sintoma | Causa provável |
| --- | --- |
| `cannot be resolved to a variable` | a variável está fora de escopo ou o nome foi digitado de forma diferente |
| `variable ... might not have been initialized` | existe pelo menos um caminho até o uso sem atribuição |
| `variable ... is already defined` | o mesmo nome foi redeclarado em um escopo sobreposto |
| valor artificial como `-1` sem significado | inicialização usada apenas para esconder um problema de fluxo |

## Referências

- [OCPJ21 Study Guide - Chapter 2: Controlling Program Flow](../ocpj21-book/ch02.md), seção *Variable Scopes*.
- [Java Language Specification 25 - Scope of a Declaration](https://docs.oracle.com/javase/specs/jls/se25/html/jls-6.html#jls-6.3).
- [Java Language Specification 25 - Definite Assignment](https://docs.oracle.com/javase/specs/jls/se25/html/jls-16.html).

---

<div align="center">

⬅️ [A6 · Expressão condicional ternária](./A6%20-%20Expressao%20condicional%20ternaria.md) &nbsp;·&nbsp; 📂 [Seção 4](./README.md) &nbsp;·&nbsp; [A8 · A certificação OCP Java SE 25 e esta seção](./A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md) ➡️

</div>
