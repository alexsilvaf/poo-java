# Sintaxe simplificada do Java 25

<sub>📚 [Documentação](../README.md) › [Seção 2 · Introdução à linguagem Java](./README.md) › Material 7 de 8</sub>

O programa mínimo tradicional exige que o iniciante copie uma estrutura que ainda será explicada ao longo do curso:

```java
public class OlaMundo {
    public static void main(String[] args) {
        System.out.println("Olá, mundo!");
    }
}
```

O Java 25 também permite escrever um programa introdutório assim:

```java
void main() {
    IO.println("Olá, mundo!");
}
```

As duas formas iniciam um programa e imprimem a mesma mensagem. O curso continuará usando a forma tradicional para manter compatibilidade com projetos e materiais existentes; a forma compacta é apresentada para reconhecimento.

## Arquivo fonte compacto

O segundo exemplo pode ser salvo diretamente como `OlaMundo.java` e executado com:

```bash
java OlaMundo.java
```

Nesse formato, o aluno não precisa declarar uma classe. O compilador cria internamente a estrutura necessária para executar o arquivo.

Nesta etapa, basta observar quatro elementos:

| Trecho | Função neste programa |
| --- | --- |
| `void` | indica que o ponto de entrada não produz um valor de resposta |
| `main` | é o nome pelo qual a execução começa |
| `{ }` | delimitam as instruções do programa |
| `IO.println` | mostra uma mensagem e quebra a linha |

Detalhes sobre métodos, objetos, membros de instância, construtores e herança pertencem às seções de orientação a objetos e não são necessários para executar o primeiro exemplo.

## Saída sem criar outros conceitos

`IO` oferece duas operações suficientes para os primeiros testes:

```java
void main() {
    IO.print("Olá, ");
    IO.println("turma!");
}
```

Saída:

```text
Olá, turma!
```

`print` mantém o cursor na mesma linha. `println` escreve e termina a linha. A formatação completa da saída será estudada na Seção 3.

## A forma tradicional continua sendo a referência

| Situação | Forma usada no curso |
| --- | --- |
| reconhecimento da novidade do Java 25 | arquivo compacto com `void main()` |
| exercícios e projetos das próximas seções | classe explícita com `public static void main(String[] args)` |

Essa escolha evita alternar entre duas estruturas enquanto variáveis, entrada, processamento e saída ainda estão sendo aprendidos.

## Importação de módulo

O Java 25 também acrescentou a declaração:

```java
import module java.base;
```

Ela torna disponíveis os pacotes exportados por um módulo. Neste ponto, basta reconhecer a sintaxe e relacioná-la à hierarquia vista no A4. Os tipos fornecidos pelo módulo serão usados somente quando cada biblioteca for apresentada.

Em arquivos fonte compactos, a importação de `java.base` já é fornecida automaticamente, por isso `IO` pode ser usado sem escrever `import`.

## O que fica para depois

Para manter a progressão, este material não explora:

- outras assinaturas possíveis para `main`;
- ordem de escolha entre vários pontos de entrada;
- membros de instância e membros estáticos;
- construtores, herança e modificadores de acesso;
- conflitos entre importações de módulo.

Esses assuntos exigem orientação a objetos ou estudo específico para certificação. Eles não são pré-requisitos das Seções 3, 4 e 5.

## Referências

- [JEP 512: Compact Source Files and Instance Main Methods](https://openjdk.org/jeps/512)
- [JEP 511: Module Import Declarations](https://openjdk.org/jeps/511)

---

<div align="center">

⬅️ [A6 · Criando o primeiro projeto em Java](./A6%20-%20Primeiro%20programa%20em%20Java.md) &nbsp;·&nbsp; 📂 [Seção 2](./README.md) &nbsp;·&nbsp; [A8 · A certificação OCP Java SE 25 e esta seção](./A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md) ➡️

</div>
