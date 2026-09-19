# O problema dos triângulos sem orientação a objetos

<sub>📚 [Documentação](../README.md) › [Seção 7 · Introdução à Programação Orientada a Objetos](./README.md) › Material 1 de 8</sub>

Antes de criar a primeira classe, vamos resolver um problema usando apenas os recursos já estudados.

Dois triângulos têm lados conhecidos. O programa deve calcular a área de cada um e informar qual possui a maior área. Pela fórmula de Heron, para lados `a`, `b` e `c`:

```text
p = (a + b + c) / 2
area = raizQuadrada(p * (p - a) * (p - b) * (p - c))
```

## Solução com variáveis separadas

```java
import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the measures of triangle X:");
        double xA = sc.nextDouble();
        double xB = sc.nextDouble();
        double xC = sc.nextDouble();

        System.out.println("Enter the measures of triangle Y:");
        double yA = sc.nextDouble();
        double yB = sc.nextDouble();
        double yC = sc.nextDouble();

        double p = (xA + xB + xC) / 2.0;
        double areaX = Math.sqrt(p * (p - xA) * (p - xB) * (p - xC));

        p = (yA + yB + yC) / 2.0;
        double areaY = Math.sqrt(p * (p - yA) * (p - yB) * (p - yC));

        System.out.printf("Triangle X area: %.4f%n", areaX);
        System.out.printf("Triangle Y area: %.4f%n", areaY);

        if (areaX > areaY) {
            System.out.println("Larger area: X");
        } else {
            System.out.println("Larger area: Y");
        }

        sc.close();
    }
}
```

Exemplo de entrada:

```text
3.00 4.00 5.00
7.50 4.50 4.02
```

## A solução funciona, mas o modelo está espalhado

Observe os grupos `xA`, `xB`, `xC` e `yA`, `yB`, `yC`. Cada trio descreve uma mesma ideia: um triângulo. Porém, o código não possui uma estrutura chamada “triângulo” que mantenha esses dados juntos.

Também foi necessário escrever o cálculo da área duas vezes. Um método `static`, como os da Seção 6, poderia eliminar a repetição do cálculo, mas os três valores continuariam separados. A orientação a objetos oferece outra organização:

- uma **classe** descreve quais dados e comportamentos formam um tipo;
- um **objeto** representa uma ocorrência concreta desse tipo;
- os dados e os comportamentos relacionados podem ficar juntos.

## Perguntas para observar o problema

1. Quantas variáveis seriam necessárias para representar dez triângulos desse modo?
2. O compilador sabe que `xA`, `xB` e `xC` pertencem ao mesmo triângulo?
3. Se outro cálculo também precisar dos três lados, onde ele ficará?

Essas perguntas motivam a criação da classe `Triangle` na próxima aula. Ainda não precisamos de construtores, `this` ou encapsulamento.

## O que fica para depois

- guardar vários triângulos em arrays ou coleções;
- validar se três lados realmente formam um triângulo;
- proteger os dados internos da classe;
- criar objetos já preenchidos por meio de construtores.

---

<div align="center">

📂 [Seção 7](./README.md) &nbsp;·&nbsp; [A2 · Classes, objetos e atributos](./A2%20-%20Classes%20objetos%20e%20atributos.md) ➡️

</div>
