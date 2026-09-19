# Criando o primeiro projeto em Java

<sub>📚 [Documentação](../README.md) › [Seção 2 · Introdução à linguagem Java](./README.md) › Material 6 de 8</sub>

## Regras de nomes

- Nome do projeto sem espaço em branco, sem acento, nomes simples;
- Arquivos que contêm uma classe pública usam o mesmo nome da classe, normalmente em `PascalCase`;
- O nome da classe pública deve ser idêntico ao nome do arquivo, sem a extensão `.java`.

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
| `static`        | Faz parte da assinatura tradicional usada pelo curso; seu papel será retomado ao estudar membros estáticos. |
| `void`          | O método não devolve valor para quem o chamou. |
| `main`          | O nome que a JVM procura, todo em minúsculas. |
| `String[] args` | Parte da assinatura tradicional; os colchetes serão explicados quando arrays forem estudados. |

Não é necessário entender arrays nem argumentos de linha de comando neste momento. O aluno deve copiar essa parte exatamente como aparece e concentrar-se no fluxo: a JVM entra no `main` e executa as instruções entre as chaves, de cima para baixo.

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

public class OlaCurso {         // 2. declaração de tipo
    public static void main(String[] args) {
        System.out.println("Olá, curso de Java!");
    }
}
```

As declarações `import` serão usadas pela primeira vez quando o curso apresentar entrada de dados com `Scanner`, na Seção 3.

## Erros mais comuns no primeiro programa

| Mensagem | Causa provável |
|----------|----------------|
| `class X is public, should be declared in a file named X.java` | O nome do arquivo não bate com o nome da classe pública. |
| `Could not find or load main class X` | O nome da classe foi digitado errado, ou o comando foi executado no diretório errado, ou o pacote não foi informado. |
| `cannot find symbol` | Nome escrito errado, ou falta um `import`, ou a variável não foi declarada. |
| `';' expected` | Falta o ponto e vírgula ao final da instrução. |
| `NoClassDefFoundError` | A classe compilou, mas não está no *classpath* na hora de executar. |

> [!NOTE]
> A partir do Java 25 existe uma forma ainda mais curta de escrever esse primeiro programa, dispensando a classe e o `public static`. Esse assunto está no material [A7 - Sintaxe simplificada do Java 25](./A7%20-%20Sintaxe%20simplificada%20do%20Java%2025.md).

---

<div align="center">

⬅️ [A5 · Instalação do JDK e da IDE](./A5%20-%20Instalacao%20do%20JDK%20e%20da%20IDE.md) &nbsp;·&nbsp; 📂 [Seção 2](./README.md) &nbsp;·&nbsp; [A7 · Sintaxe simplificada do Java 25](./A7%20-%20Sintaxe%20simplificada%20do%20Java%2025.md) ➡️

</div>
