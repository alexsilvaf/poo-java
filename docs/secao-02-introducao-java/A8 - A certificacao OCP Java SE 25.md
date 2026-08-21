# A certificação OCP Java SE 25 e esta seção

Este material relaciona o conteúdo da Seção 2 com o que a Oracle cobra na certificação **Oracle Certified Professional, Java SE 25 Developer**.

> Esta seção do curso é introdutória. A certificação é voltada a quem já programa em Java. O objetivo aqui não é preparar para a prova, mas mostrar, desde o início, quais conceitos continuam relevantes muito além da primeira aula.

## Identificação da prova

| Item | Valor |
|------|-------|
| Nome | Java SE 25 Developer Professional |
| Código | **1Z0-831** |
| Disponibilidade | Desde 1º de maio de 2026 |
| Prova anterior | 1Z0-830 (Java SE 21) |

O formato divulgado por fontes de preparação é de **50 questões de múltipla escolha, 120 minutos e 68% de aproveitamento**, o mesmo do 1Z0-830. Confirme sempre na página oficial antes de agendar, porque a Oracle ajusta esses números sem aviso.

## Objetivos oficiais do 1Z0-831

| Grupo de objetivos | Novidades em relação ao Java 21 |
|--------------------|----------------------------------|
| Handling Date, Time, Text, Numeric and Boolean Values | — |
| Implementing Program Flow Control | — |
| Applying Object-Oriented Principles | Corpos de construtor flexíveis, variáveis sem nome |
| Implementing Exception Handling | — |
| Using Arrays and Collections | *Sequenced collections* explicitadas |
| Processing Data with Streams and Lambda Expressions | Operação `gather` |
| **Packaging and Deploying Java Code** | **Importação de módulos, arquivos-fonte compactos, `main` de instância** |
| Implementing Multithreading | *Scoped values* |
| Performing Input/Output Operations | — |
| Developing Applications with Localization Support | — |

O grupo em destaque é o que toca diretamente esta seção.

## O que desta seção cai na prova

### Módulos e empacotamento (materiais A3 e A4)

Este é o assunto mais cobrado da seção. A prova exige saber:

- declarar um módulo em `module-info.java` e usar `requires`, `exports`, `exports ... to`, `opens`, `uses` e `provides`;
- a diferença entre **named modules**, **automatic modules** e **unnamed module**, e o que cada um consegue enxergar;
- que todo módulo depende implicitamente de `java.base`, sem precisar de `requires`;
- a diferença entre **classpath** e **module path**, e como cada um afeta o encapsulamento;
- compilar, empacotar e executar pela linha de comando com `javac`, `jar`, `java --module-path`;
- criar imagens de runtime com `jlink` e analisar dependências com `jdeps` e `jmod`;
- estratégias de migração de uma aplicação não modular para módulos.

> No estudo em inglês, esse conteúdo corresponde ao **Capítulo 13** do [OCPJ21 Study Guide](../ocpj21-book/ch13.md), que continua válido: o sistema de módulos não mudou entre o Java 21 e o Java 25.

### Pacotes, classes e arquivos-fonte (material A4)

Cobrado dentro de *Applying Object-Oriented Principles*:

- a ordem obrigatória `package` → `import` → declarações de tipo;
- a regra de uma única classe `public` por arquivo, com o nome do arquivo igual ao da classe;
- `java.lang` importado automaticamente e classes do mesmo pacote dispensando `import`;
- que `import pacote.*` **não** alcança subpacotes;
- imports redundantes, conflitos de nome simples e uso de nome totalmente qualificado;
- `import static` para membros estáticos.

> Corresponde ao **Capítulo 1** do [OCPJ21 Study Guide](../ocpj21-book/ch01.md), na seção *Organizing Classes into Packages*.

### O método `main` e a sintaxe do Java 25 (materiais A5 e A7)

Aqui está a diferença real entre a prova do Java 21 e a do Java 25:

- todas as assinaturas válidas de `main`, incluindo as de instância;
- a **ordem de escolha do ponto de entrada** pelo lançador;
- a exigência de construtor sem argumentos e não privado para um `main` de instância;
- que `private void main()` não é ponto de entrada;
- as restrições dos arquivos-fonte compactos: sem `package`, sem construtor, sem `extends`/`implements`, não referenciável por nome, membros de nível superior sendo de instância;
- os métodos de `java.lang.IO`;
- `import module`, o conflito de nomes simples entre módulos importados e a precedência do `import` comum.

### Execução e ferramentas (material A3)

- o papel de `javac`, `java`, `jar`, `jlink`, `jdeps` e `jshell`;
- a execução direta de um arquivo-fonte com `java Arquivo.java`;
- que o coletor de lixo é acionado pela JVM e que `System.gc()` é apenas uma sugestão;
- o que torna um objeto elegível para coleta.

## O que desta seção **não** cai na prova

Vale saber para não perder tempo de estudo com isso:

- histórico do Java, Sun Microsystems, aquisição pela Oracle;
- edições Java ME, Java SE e Java EE;
- diferença conceitual entre linguagens compiladas, interpretadas e híbridas;
- funcionamento interno do JIT, áreas de memória da JVM e algoritmos de coleta de lixo;
- instalação do JDK, escolha e configuração de IDE, uso do Eclipse;
- datas de lançamento e lista de recursos por versão.

Esses assuntos são fundamentais para entender a plataforma, mas a prova cobra **comportamento de código**, e não história ou teoria de arquitetura.

## Exemplos no estilo da prova

**1.** Considere o arquivo `App.java`:

```java
public class App {
    private App() { }

    void main() {
        System.out.println("olá");
    }
}
```

O que acontece ao executar `java App.java`?

<details>
<summary>Resposta</summary>

Falha em tempo de execução. O `main` de instância exige que a classe tenha um construtor **não privado** e sem argumentos, para que o lançador consiga instanciá-la. Aqui o único construtor é `private`.
</details>

**2.** Qual método é executado?

```java
public class Entrada {
    static void main() {
        System.out.println("A");
    }

    void main(String[] args) {
        System.out.println("B");
    }
}
```

<details>
<summary>Resposta</summary>

`A`. A ordem de escolha prioriza os métodos **estáticos declarados na própria classe** antes dos de instância. Entre os estáticos, `main(String[])` viria primeiro, mas ele não existe aqui; então o `static void main()` é escolhido.
</details>

**3.** O arquivo abaixo compila?

```java
package com.exemplo;

void main() {
    IO.println("teste");
}
```

<details>
<summary>Resposta</summary>

Não. Um arquivo-fonte compacto não pode declarar `package`; sua classe implícita fica obrigatoriamente no pacote sem nome.
</details>

**4.** Dado `module com.app { }`, o código dentro desse módulo pode usar `java.util.List`?

<details>
<summary>Resposta</summary>

Sim. `java.util` é exportado por `java.base`, e todo módulo depende de `java.base` implicitamente, sem precisar de `requires java.base;`.
</details>

## Materiais de estudo

- **Página oficial da prova:** <https://education.oracle.com/java-se-25-developer-professional/pexam_1Z0-831>
- **[OCPJ21 Study Guide](../ocpj21-book/)**, de Esteban Herrera, incluído neste repositório. Cobre o Java 21 e continua válido para a maior parte do conteúdo; precisa ser complementado com os recursos novos do Java 25.
- **Enthuware** e **Selikoff/Boyarsky (Sybex)** publicam simulados e livro para o 1Z0-831.

> **Não existe um `ocpj25-book`.** O autor do `ocpj21-book`, Esteban Herrera, mantém no GitHub os repositórios `ocpj8-book`, `ocpj8-notes`, `ocpj17-book` e `ocpj21-book`, mas nenhum voltado ao Java 25 até esta data. Enquanto isso, o `ocpj21-book` continua sendo a base, com os complementos deste material.
