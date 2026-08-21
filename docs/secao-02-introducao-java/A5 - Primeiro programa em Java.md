# Criando o primeiro projeto em Java

## Regras de nomes

- Nome do projeto sem espaço em branco, sem acento, nomes simples;
- Arquivos devem ser *camel case* com iniciais maiúsculas (`PascalCase`);
- Nomes das classes devem possuir o mesmo nome do arquivo.

Além dessas convenções, existem regras que o compilador exige:

- Um identificador pode conter letras, dígitos, `_` e `$`, mas **não pode começar com um dígito**.
- Não pode ser uma palavra reservada da linguagem (`class`, `int`, `for`, `public`, ...).
- Pacotes são escritos em minúsculas, classes em `PascalCase`, métodos e variáveis em `camelCase`, constantes em `MAIUSCULAS_COM_UNDERLINE`.

## O programa mínimo

```java
public class OlaMundo {
    public static void main(String[] args) {
        System.out.println("Olá, mundo!");
    }
}
```

Esse arquivo precisa se chamar `OlaMundo.java`, porque a classe `OlaMundo` é `public`.

## Entendendo o método `main`

O método `main` é o **ponto de entrada** da aplicação: é por ele que a JVM começa a executar o programa. Cada parte da assinatura tem um motivo:

| Parte           | Por que é necessária |
|-----------------|----------------------|
| `public`        | Permite que a JVM chame o método a partir de fora da classe. |
| `static`        | Permite chamar o método sem criar um objeto da classe. |
| `void`          | O método não devolve valor para quem o chamou. |
| `main`          | O nome que a JVM procura, todo em minúsculas. |
| `String[] args` | Recebe os argumentos passados na linha de comando. |

O parâmetro `args` pode ter qualquer nome, e a forma `String... args` também é aceita:

```java
public static void main(String... args) { }   // válido
public static void main(String args[]) { }    // válido, sintaxe antiga do colchete
```

### Argumentos de linha de comando

```java
public class Argumentos {
    public static void main(String[] args) {
        if (args.length > 0) {
            for (String argumento : args) {
                System.out.println(argumento);
            }
        } else {
            System.out.println("Nenhum argumento informado.");
        }
    }
}
```

```bash
java Argumentos um dois tres
```

```
um
dois
tres
```

> `args` nunca é `null`. Quando nenhum argumento é passado, ele é um array de tamanho zero.

## Compilando e executando pela linha de comando

Mesmo usando uma IDE, é importante saber o que acontece por baixo dela:

```bash
javac OlaMundo.java   # gera OlaMundo.class com o bytecode
java OlaMundo         # executa a classe (sem a extensão .class)
```

Desde o Java 11 é possível executar um único arquivo-fonte direto, sem gerar o `.class`:

```bash
java OlaMundo.java
```

Nesse modo o compilador roda em memória, o que é conveniente para exercícios e testes rápidos.

## Estrutura completa de um arquivo-fonte

A ordem dos elementos é fixa e o compilador a exige:

```java
package com.exemplo.curso;      // 1. opcional, mas se existir vem primeiro

import java.util.Scanner;       // 2. opcional, depois do package

public class Entrada {          // 3. as declarações de tipo
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite seu nome: ");
        String nome = sc.nextLine();
        System.out.println("Olá, " + nome + "!");
        sc.close();
    }
}
```

## Erros mais comuns no primeiro programa

| Mensagem | Causa provável |
|----------|----------------|
| `class X is public, should be declared in a file named X.java` | O nome do arquivo não bate com o nome da classe pública. |
| `Could not find or load main class X` | O nome da classe foi digitado errado, ou o comando foi executado no diretório errado, ou o pacote não foi informado. |
| `cannot find symbol` | Nome escrito errado, ou falta um `import`, ou a variável não foi declarada. |
| `';' expected` | Falta o ponto e vírgula ao final da instrução. |
| `NoClassDefFoundError` | A classe compilou, mas não está no *classpath* na hora de executar. |

> A partir do Java 25 existe uma forma ainda mais curta de escrever esse primeiro programa, dispensando a classe e o `public static`. Esse assunto está no material [A7 - Sintaxe simplificada do Java 25](./A7%20-%20Sintaxe%20simplificada%20do%20Java%2025.md).
