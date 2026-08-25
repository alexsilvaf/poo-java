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

Este é o assunto mais cobrado da seção. Do que **esta seção ensina**, a prova exige saber:

- declarar um módulo em `module-info.java` e usar `requires` e `exports`;
- que todo módulo depende implicitamente de `java.base`, sem precisar de `requires`;
- a diferença entre **classpath** e **module path**, e como cada um afeta o encapsulamento;
- compilar, empacotar e executar pela linha de comando com `javac`, `jar`, `java --module-path`;
- criar imagens de runtime com `jlink` e analisar dependências com `jdeps`.

> No estudo em inglês, esse conteúdo corresponde ao **Capítulo 13** do [OCPJ21 Study Guide](../ocpj21-book/ch13.md), que continua válido: o sistema de módulos não mudou entre o Java 21 e o Java 25.

> **Vai além desta seção:** `exports ... to`, `opens`, `uses`, `provides`, a diferença entre **named**, **automatic** e **unnamed modules**, a ferramenta `jmod` e estratégias de migração para módulos. Esses tópicos também estão no grupo *Packaging and Deploying Java Code*, mas pedem um estudo do sistema de módulos mais aprofundado do que o que a Seção 2 cobre. Fica para quando for estudar diretamente para a prova.

### Pacotes, classes e arquivos-fonte (material A4)

Cobrado dentro de *Applying Object-Oriented Principles*, do que **esta seção ensina**:

- a ordem obrigatória `package` → `import` → declarações de tipo;
- a regra de uma única classe `public` por arquivo, com o nome do arquivo igual ao da classe;
- `java.lang` importado automaticamente e classes do mesmo pacote dispensando `import`;
- que `import pacote.*` **não** alcança subpacotes.

> Corresponde ao **Capítulo 1** do [OCPJ21 Study Guide](../ocpj21-book/ch01.md), na seção *Organizing Classes into Packages*.

> **Vai além desta seção:** `import static`, e conflitos de nome simples entre dois imports comuns (o conflito entre `import module`, esse sim, está no A7). Fica para quando for estudar diretamente para a prova.

### O método `main` e a sintaxe do Java 25 (materiais A5 e A7)

Aqui está a diferença real entre a prova do Java 21 e a do Java 25 — e o que a Seção 2 ensina quase todo:

- todas as assinaturas válidas de `main`, incluindo as de instância;
- a **ordem de escolha do ponto de entrada** pelo lançador;
- que `private void main()` não é ponto de entrada, porque o acesso não pode ser privado;
- as restrições dos arquivos-fonte compactos: sem `package`, sem construtor, sem `extends`/`implements`, não referenciável por nome, membros de nível superior sendo de instância, precisa ter um `main`;
- os métodos de `java.lang.IO`;
- `import module`, o conflito de nomes simples entre módulos importados e a precedência do `import` comum.

> **Vai além desta seção:** a exigência de um construtor sem argumentos e não privado para um `main` de instância depende do conceito de construtor, que só é ensinado na Seção 8. O A7 menciona a regra, mas a Seção 2 não ensina o suficiente sobre construtores para justificá-la a fundo.

### Execução e ferramentas (material A3)

- o papel de `javac`, `java`, `jar`, `jlink`, `jdeps` e `jshell`;
- a execução direta de um arquivo-fonte com `java Arquivo.java`.

> **Vai além desta seção:** que o coletor de lixo é acionado pela JVM, que `System.gc()` é apenas uma sugestão, e o que torna um objeto elegível para coleta. A Seção 2 ensina que o GC existe e libera memória automaticamente, mas não esses detalhes de comportamento.

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

Todos os exemplos abaixo se resolvem só com o que os materiais A1, A3, A4, A5 e A7 desta seção ensinam.

### Versões (material A1)

**1.** Qual das versões abaixo é LTS?

`(a)` Java 22 &nbsp;&nbsp; `(b)` Java 23 &nbsp;&nbsp; `(c)` Java 24 &nbsp;&nbsp; `(d)` Java 25

<details>
<summary>Resposta</summary>

**(d) Java 25.** As versões LTS cobertas no material são 8, 11, 17, 21 e 25, sempre com dois anos de intervalo. 22, 23 e 24 são *feature releases*, com suporte só até a versão seguinte.
</details>

### Plataforma e ferramentas (material A3)

**2.** Qual comando gera um arquivo `.jar` a partir de classes já compiladas?

`(a)` `javac` &nbsp;&nbsp; `(b)` `java` &nbsp;&nbsp; `(c)` `jar` &nbsp;&nbsp; `(d)` `jlink`

<details>
<summary>Resposta</summary>

**(c) `jar`.** `javac` compila `.java` em `.class`; `java` executa; `jlink` gera uma imagem de runtime, não um `.jar`.
</details>

**3.** A partir de qual versão do Java é possível rodar `java Ola.java` diretamente, sem gerar o `.class` manualmente antes?

<details>
<summary>Resposta</summary>

**Java 11** (JEP 330). Nesse modo o compilador roda em memória; é conveniente para exercícios e testes rápidos, mas o arquivo continua podendo ter a estrutura tradicional, com `package`, classe pública e `main` estático.
</details>

### Pacotes, classes e módulos (material A4)

**4.** O arquivo abaixo compila?

```java
// Arquivo: Conta.java
public class Conta { }

public class Cliente { }
```

<details>
<summary>Resposta</summary>

**Não.** Um arquivo-fonte só pode ter uma classe `public`; aqui há duas (`Conta` e `Cliente`).
</details>

**5.** Com `import java.util.*;` no topo do arquivo, o código consegue usar `java.util.concurrent.atomic.AtomicInteger` escrevendo só `AtomicInteger`?

<details>
<summary>Resposta</summary>

**Não.** `import pacote.*` importa os tipos do próprio pacote, mas não alcança subpacotes. Seria preciso `import java.util.concurrent.atomic.AtomicInteger;` ou o nome totalmente qualificado.
</details>

**6.** Dado `module com.app { }`, o código dentro desse módulo pode usar `java.util.List`?

<details>
<summary>Resposta</summary>

**Sim.** `java.util` é exportado por `java.base`, e todo módulo depende de `java.base` implicitamente, sem precisar de `requires java.base;`.
</details>

### Primeiro programa (material A5)

**7.** O que acontece ao tentar compilar este arquivo?

```java
// Arquivo: Programa.java
public class Aplicacao {
    public static void main(String[] args) {
        System.out.println("Início");
    }
}
```

<details>
<summary>Resposta</summary>

**Erro de compilação** — `class Aplicacao is public, should be declared in a file named Aplicacao.java` — porque o nome do arquivo (`Programa.java`) não bate com o nome da classe pública (`Aplicacao`).
</details>

**8.** Executando `java Argumentos` sem passar nenhum argumento, o que este programa imprime?

```java
public class Argumentos {
    public static void main(String[] args) {
        System.out.println(args.length);
    }
}
```

<details>
<summary>Resposta</summary>

**`0`.** `args` nunca é `null`; sem argumentos, ele é simplesmente um array de tamanho zero.
</details>

### Sintaxe do Java 25 (material A7)

**9.** Qual método é executado?

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

**`A`.** A ordem de escolha prioriza os métodos **estáticos declarados na própria classe** antes dos de instância. Entre os estáticos, `main(String[])` viria primeiro, mas ele não existe aqui; então o `static void main()` é escolhido.
</details>

**10.** O arquivo abaixo compila?

```java
package com.exemplo;

void main() {
    IO.println("teste");
}
```

<details>
<summary>Resposta</summary>

**Não.** Um arquivo-fonte compacto não pode declarar `package`; sua classe implícita fica obrigatoriamente no pacote sem nome.
</details>

**11.** O que acontece ao executar `java Programa`?

```java
public class Programa {
    private void main() {
        System.out.println("nunca roda");
    }
}
```

<details>
<summary>Resposta</summary>

**Falha ao iniciar** — algo como `Error: Main method not found in class Programa`. `private void main()` não é considerado ponto de entrada: o método `main` precisa ter acesso não privado.
</details>

**12.** Dois módulos importados com `import module` exportam, cada um, uma classe chamada `Chart`. O código usa `Chart` diretamente, sem qualificar o pacote. Compila?

<details>
<summary>Resposta</summary>

**Não, do jeito que está.** O nome simples fica ambíguo entre os dois módulos. A solução é acrescentar um `import` comum do tipo desejado (por exemplo, `import graficos.Chart;`), que tem precedência sobre os tipos trazidos por `import module`.
</details>

## Materiais de estudo

- **Página oficial da prova:** <https://education.oracle.com/java-se-25-developer-professional/pexam_1Z0-831>
- **[OCPJ21 Study Guide](../ocpj21-book/)**, de Esteban Herrera, incluído neste repositório. Cobre o Java 21 e continua válido para a maior parte do conteúdo; precisa ser complementado com os recursos novos do Java 25.
- **Enthuware** e **Selikoff/Boyarsky (Sybex)** publicam simulados e livro para o 1Z0-831.

> **Não existe um `ocpj25-book`.** O autor do `ocpj21-book`, Esteban Herrera, mantém no GitHub os repositórios `ocpj8-book`, `ocpj8-notes`, `ocpj17-book` e `ocpj21-book`, mas nenhum voltado ao Java 25 até esta data. Enquanto isso, o `ocpj21-book` continua sendo a base, com os complementos deste material.
