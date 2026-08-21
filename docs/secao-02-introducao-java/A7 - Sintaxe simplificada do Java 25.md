# Sintaxe simplificada do Java 25

O programa mínimo tradicional em Java obriga o iniciante a escrever conceitos que ele ainda não aprendeu: classe, visibilidade, membro estático, tipo de retorno e array de `String`.

```java
public class OlaMundo {
    public static void main(String[] args) {
        System.out.println("Olá, mundo!");
    }
}
```

O Java 25 finalizou a **JEP 512 — Compact Source Files and Instance Main Methods**, que permite escrever o mesmo programa assim:

```java
void main() {
    IO.println("Olá, mundo!");
}
```

O recurso passou por quatro rodadas de prévia (JEPs 445, 463, 477 e 495) antes de se tornar definitivo no Java 25.

## Arquivo-fonte compacto

Um **arquivo-fonte compacto** (*compact source file*) é um arquivo `.java` cujo conteúdo de nível superior são campos, métodos e não uma declaração de classe. O compilador envolve esse conteúdo em uma **classe declarada implicitamente**, que o programador nunca escreve nem enxerga.

```java
// Arquivo: Saudacao.java

String nome = "turma";          // vira um campo de instância

void main() {
    IO.println(mensagem());
}

String mensagem() {
    return "Olá, " + nome + "!";
}
```

```bash
java Saudacao.java
```

### Regras e limitações

- O arquivo **não pode ter declaração de `package`**: a classe implícita fica no pacote sem nome.
- A classe implícita é `final`, herda de `Object` e **não pode declarar `extends` nem `implements`**.
- **Não pode declarar construtor.** O compilador fornece um construtor sem argumentos.
- A classe implícita **não pode ser referenciada pelo nome** a partir de outro código, porque ela não tem um nome utilizável no código-fonte.
- Os membros declarados no nível superior são **de instância** por padrão, mas `static` continua sendo permitido.
- A classe implícita **precisa ter um método `main`**, caso contrário o arquivo não compila.
- O arquivo recebe automaticamente `import module java.base;`, ou seja, `List`, `Map`, `Scanner`, `Path` e os demais tipos exportados pelo `java.base` ficam disponíveis sem `import`.

> Um arquivo-fonte compacto é apenas açúcar sintático. Ele é compilado para um `.class` comum, executado pela mesma JVM, sem qualquer tratamento especial em tempo de execução.

## Método `main` de instância

Independentemente de usar arquivo compacto ou não, o método `main` deixou de precisar ser `public static void main(String[] args)`. Todas estas formas são válidas:

```java
public static void main(String[] args) { }   // forma tradicional
static void main() { }
void main(String[] args) { }
void main() { }
```

O que o método **ainda** precisa ser:

- chamado `main`;
- de retorno `void`;
- de acesso **não privado**, ou seja, `public`, `protected` ou de pacote. Um `private void main()` não é considerado ponto de entrada.

Quando o `main` escolhido é um **método de instância**, o lançador cria um objeto da classe antes de chamá-lo. Para isso, a classe precisa ter um **construtor sem argumentos e não privado**.

### Ordem de escolha do ponto de entrada

Havendo mais de um candidato, o lançador escolhe o **primeiro** desta lista:

1. `static void main(String[] args)` não privado, **declarado na própria classe**;
2. `static void main()` não privado, **declarado na própria classe**;
3. `void main(String[] args)` de instância, não privado, declarado na classe **ou herdado de uma superclasse**;
4. `void main()` de instância, não privado, declarado na classe **ou herdado de uma superclasse**.

```java
public class Ordem {
    void main() {
        System.out.println("main() de instância");
    }

    public static void main(String[] args) {
        System.out.println("main(String[]) estático");   // este é executado
    }
}
```

> Repare que a versão com `String[]` tem prioridade sobre a sem argumentos, e que os métodos estáticos da própria classe têm prioridade sobre os de instância. Esse é exatamente o tipo de detalhe que a prova de certificação explora.

## A classe `java.lang.IO`

O Java 25 introduziu a classe `IO` no pacote `java.lang`, que é importado automaticamente. Ela concentra as operações básicas de console:

| Método | Função |
|--------|--------|
| `IO.println(Object obj)` | Escreve o objeto e quebra a linha. |
| `IO.println()` | Escreve apenas uma quebra de linha. |
| `IO.print(Object obj)` | Escreve o objeto sem quebrar a linha. |
| `IO.readln()` | Lê uma linha digitada pelo usuário. |
| `IO.readln(String prompt)` | Escreve o texto informado e então lê uma linha. |

```java
void main() {
    String nome = IO.readln("Digite seu nome: ");
    IO.println("Olá, " + nome + "!");
}
```

Isso substitui, para casos simples, a combinação de `System.out.println` com `Scanner`.

## Importação de módulo

A **JEP 511 — Module Import Declarations**, também finalizada no Java 25, permite importar de uma vez todos os pacotes exportados por um módulo:

```java
import module java.base;

public class Exemplo {
    public static void main(String[] args) {
        List<Integer> numeros = List.of(3, 1, 2);   // java.util
        Path arquivo = Path.of("dados.txt");        // java.nio.file
        System.out.println(numeros);
    }
}
```

Detalhes que valem para a prova:

- `import module` só funciona com **nomes de módulo**, não com nomes de pacote.
- O código que usa `import module` **não precisa estar dentro de um módulo**.
- Se dois módulos importados exportam tipos de mesmo nome simples, o uso desse nome fica **ambíguo** e não compila. A solução é acrescentar um `import` comum do tipo desejado, que tem precedência.
- Em arquivos-fonte compactos, `import module java.base;` é implícito.

## Quando usar cada forma

| Situação | Forma recomendada |
|----------|-------------------|
| Exercício rápido, script, aula introdutória | Arquivo-fonte compacto com `void main()` |
| Classe que faz parte de um projeto real | Classe explícita, com `package` e `public static void main` |
| Código que precisa ser chamado por outras classes | Classe explícita, obrigatoriamente |

> O recurso não substitui a orientação a objetos: ele apenas adia o momento em que o aluno precisa aprendê-la. Todo o restante do curso continua usando classes declaradas explicitamente.

## Referências

- [JEP 512: Compact Source Files and Instance Main Methods](https://openjdk.org/jeps/512)
- [JEP 511: Module Import Declarations](https://openjdk.org/jeps/511)
