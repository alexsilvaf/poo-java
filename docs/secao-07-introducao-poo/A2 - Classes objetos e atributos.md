# Classes, objetos e atributos

<sub>📚 [Documentação](../README.md) › [Seção 7 · Introdução à Programação Orientada a Objetos](./README.md) › Material 2 de 8</sub>

Uma classe define um novo tipo. Ela descreve a estrutura que os objetos desse tipo terão. Para representar um triângulo, começaremos apenas com seus três lados.

## Declarando a classe

Crie o arquivo `Triangle.java`:

```java
public class Triangle {
    public double a;
    public double b;
    public double c;
}
```

Os campos `a`, `b` e `c` são **atributos**, também chamados de **campos de instância**. Cada objeto `Triangle` terá seu próprio conjunto desses três campos.

Nesta primeira modelagem os campos são `public` para que possamos concentrar a atenção na criação e no uso de objetos. Na Seção 8, o encapsulamento substituirá esse acesso direto.

## Classe não é objeto

- `Triangle` é a classe: a definição do tipo.
- `x` é uma variável capaz de guardar uma referência a um `Triangle`.
- `new Triangle()` cria um novo objeto.

```java
Triangle x;
x = new Triangle();
```

Também é possível declarar e inicializar na mesma instrução:

```java
Triangle y = new Triangle();
```

Cada avaliação de `new Triangle()` produz um objeto novo.

## Acessando campos com o ponto

Crie `Program.java`:

```java
public class Program {
    public static void main(String[] args) {
        Triangle x = new Triangle();
        Triangle y = new Triangle();

        x.a = 3.0;
        x.b = 4.0;
        x.c = 5.0;

        y.a = 7.5;
        y.b = 4.5;
        y.c = 4.02;

        System.out.println(x.a);
        System.out.println(y.a);
    }
}
```

O operador ponto seleciona um membro do objeto referenciado pela variável:

```text
x.a
│ └─ campo a
└── referência usada para chegar ao objeto
```

Alterar `x.a` não altera `y.a`, porque `x` e `y` referenciam objetos diferentes.

## Valores iniciais dos campos

Quando um objeto é criado, seus campos recebem valores padrão antes de qualquer atribuição explícita:

| Tipo do campo | Valor padrão |
| --- | --- |
| tipos inteiros | `0` |
| ponto flutuante | `0.0` |
| `boolean` | `false` |
| `char` | caractere de valor zero |
| tipos de referência | `null` |

Por isso este código compila e mostra `0.0`:

```java
Triangle triangle = new Triangle();
System.out.println(triangle.a);
```

Isso é diferente de uma variável local. A variável local precisa receber um valor antes de ser lida:

```java
double side;
// System.out.println(side); // não compila
```

## Nome do arquivo

Uma classe de topo declarada `public` deve estar em um arquivo com o mesmo nome, inclusive respeitando maiúsculas e minúsculas:

```text
Triangle.java  -> public class Triangle
Program.java   -> public class Program
```

## Verificação rápida

Considere:

```java
Triangle first = new Triangle();
Triangle second = new Triangle();
first.a = 8.0;
second.a = first.a;
first.a = 10.0;
```

Ao final, `second.a` continua valendo `8.0`. O campo é do tipo primitivo `double`; a atribuição copiou seu valor.

## Referências

- [JLS 25 - Class Declarations](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.1).
- [JLS 25 - Class Instance Creation Expressions](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.9).
- [JLS 25 - Initial Values of Variables](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html#jls-4.12.5).

---

<div align="center">

⬅️ [A1 · O problema dos triângulos sem orientação a objetos](./A1%20-%20O%20problema%20dos%20triangulos%20sem%20orientacao%20a%20objetos.md) &nbsp;·&nbsp; 📂 [Seção 7](./README.md) &nbsp;·&nbsp; [A3 · Métodos de instância](./A3%20-%20Metodos%20de%20instancia.md) ➡️

</div>
