# Métodos de instância

<sub>📚 [Documentação](../README.md) › [Seção 7 · Introdução à Programação Orientada a Objetos](./README.md) › Material 3 de 8</sub>

Na Seção 6, os métodos auxiliares foram declarados com `static` e chamados pelo nome da classe. Agora o cálculo da área pode pertencer a cada objeto `Triangle`.

## O comportamento junto dos dados

Atualize `Triangle.java`:

```java
public class Triangle {
    public double a;
    public double b;
    public double c;

    public double area() {
        double p = (a + b + c) / 2.0;
        return Math.sqrt(p * (p - a) * (p - b) * (p - c));
    }
}
```

`area()` é um **método de instância**. Ele não possui `static` e é executado em relação a um objeto específico.

## Chamando o método

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

        double areaX = x.area();
        double areaY = y.area();

        System.out.printf("Triangle X area: %.4f%n", areaX);
        System.out.printf("Triangle Y area: %.4f%n", areaY);

        if (areaX > areaY) {
            System.out.println("Larger area: X");
        } else {
            System.out.println("Larger area: Y");
        }
    }
}
```

Na chamada `x.area()`, o método lê os campos do objeto referenciado por `x`. Na chamada `y.area()`, o mesmo código lê os campos do objeto referenciado por `y`.

## Parâmetro ou campo?

O método `area()` não recebe parâmetros porque os dados necessários já pertencem ao objeto. Outro método pode receber apenas o dado que vem de fora:

```java
public void scale(double factor) {
    a *= factor;
    b *= factor;
    c *= factor;
}
```

Chamada:

```java
x.scale(2.0);
```

Depois dessa chamada, os lados do objeto `x` foram alterados. Os lados de `y` não mudaram.

## Método de instância e método `static`

| Método de instância | Método `static` |
| --- | --- |
| chamado em relação a um objeto | chamado em relação à classe |
| pode acessar diretamente campos de instância | não possui um objeto atual implícito |
| exemplo: `x.area()` | exemplo conhecido: `Math.sqrt(9.0)` |

O método `main` é `static`. Por isso ele não pode chamar `area()` sem indicar um objeto:

```java
// double value = area(); // não compila dentro de main
double value = x.area();  // compila
```

## Responsabilidade da classe

Colocar `area()` em `Triangle` traz duas vantagens imediatas:

- o cálculo não é duplicado no programa principal;
- o código expressa a intenção: “pedir a área deste triângulo”.

Isso não significa colocar toda regra dentro de qualquer classe. O método deve usar ou alterar o estado daquele tipo, ou representar uma operação natural dele.

## Exercício guiado

Adicione à classe um método que devolva o perímetro:

```java
public double perimeter() {
    return a + b + c;
}
```

Depois, chame `x.perimeter()` e `y.perimeter()` no `main`.

## O que fica para depois

- usar `this` para deixar explícito o objeto atual;
- sobrecarregar métodos;
- ocultar campos com `private`;
- sobrescrever métodos herdados além de `toString`.

## Referência

- [JLS 25 - Method Declarations](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html#jls-8.4).

---

<div align="center">

⬅️ [A2 · Classes, objetos e atributos](./A2%20-%20Classes%20objetos%20e%20atributos.md) &nbsp;·&nbsp; 📂 [Seção 7](./README.md) &nbsp;·&nbsp; [A4 · Referências, stack, heap e coleta de lixo](./A4%20-%20Referencias%20stack%20heap%20e%20coleta%20de%20lixo.md) ➡️

</div>
