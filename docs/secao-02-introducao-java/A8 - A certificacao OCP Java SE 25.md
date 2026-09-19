# A certificação OCP Java SE 25 e esta seção

<sub>📚 [Documentação](../README.md) › [Seção 2 · Introdução à linguagem Java](./README.md) › Material 8 de 8</sub>

Este material relaciona a Seção 2 com a certificação **Oracle Certified Professional Java SE 25 Developer**, exame **1Z0-831**.

> [!NOTE]
> Este é um material opcional de referência. A certificação pressupõe experiência com toda a linguagem; nesta seção, serão relacionados somente os conceitos que o aluno já encontrou. Os assuntos futuros não serão usados para explicar os atuais.

## Relação com os objetivos da prova

O grupo mais próximo desta seção é **Packaging and Deploying Java Code**. Ele inclui temas como:

- arquivos fonte e classes;
- pacotes e importações;
- módulos;
- ferramentas `javac`, `java`, `jar`, `jlink` e `jdeps`;
- formas de iniciar um programa Java 25.

Aqui, o objetivo é apenas reconhecer a estrutura básica. O estudo completo para a prova deve acontecer depois das seções de orientação a objetos.

## O que já pode ser aproveitado

### Ferramentas da plataforma

| Ferramenta | Conhecimento suficiente neste ponto |
| --- | --- |
| `javac` | transforma um arquivo `.java` em bytecode `.class` |
| `java` | inicia a JVM e executa o programa |
| `jar` | empacota classes e recursos |
| `jshell` | executa pequenos trechos interativamente |
| `jlink` | cria uma imagem de execução com os módulos necessários |
| `jdeps` | analisa dependências |

### Classes e arquivos

Do conteúdo atual, é importante saber:

- um arquivo pode ter no máximo uma classe `public`;
- quando há uma classe `public`, o arquivo deve ter o mesmo nome dela;
- Java diferencia maiúsculas e minúsculas;
- a declaração de pacote vem antes das importações e das classes.

### Pacotes e módulos

- pacotes agrupam classes relacionadas;
- módulos agrupam pacotes relacionados;
- todo módulo depende implicitamente de `java.base`;
- `module-info.java` descreve um módulo;
- `import module` é uma declaração disponível no Java 25.

Não é necessário, nesta etapa, escrever uma aplicação modular completa.

### Ponto de entrada

O curso usa como referência:

```java
public class OlaMundo {
    public static void main(String[] args) {
        System.out.println("Olá, mundo!");
    }
}
```

O aluno precisa reconhecer que a JVM começa pelo `main`. Os detalhes de `static`, arrays e objetos serão estudados no momento correspondente.

Também deve reconhecer a forma compacta do Java 25:

```java
void main() {
    IO.println("Olá, mundo!");
}
```

## O que não é exigido agora

O exame completo inclui assuntos que ainda não apareceram no curso. Para preservar a progressão, ficam fora deste material:

- escolha entre várias assinaturas de `main`;
- construtores e criação automática de objetos;
- herança e modificadores de acesso;
- conflitos complexos entre importações;
- serviços de módulos e módulos automáticos;
- arrays, coleções, exceções, concorrência e fluxos de dados.

Esses tópicos serão relacionados à certificação somente depois de ensinados.

## Questões de revisão

**1. Qual ferramenta compila `OlaMundo.java`?**

<details>
<summary><b>💡 Resposta</b></summary>

`javac`. O comando `javac OlaMundo.java` gera o bytecode em `OlaMundo.class`.
</details>

**2. Qual ferramenta inicia a JVM para executar o programa?**

<details>
<summary><b>💡 Resposta</b></summary>

`java`. Depois da compilação, o comando tradicional é `java OlaMundo`.
</details>

**3. Este arquivo compila?**

```java
// Arquivo: Programa.java
public class Aplicacao {
}
```

<details>
<summary><b>💡 Resposta</b></summary>

Não. A classe pública se chama `Aplicacao`, então o arquivo precisa se chamar `Aplicacao.java`.
</details>

**4. Qual ordem está correta no arquivo fonte?**

`(a)` classe, import, package
`(b)` package, import, classe
`(c)` import, classe, package

<details>
<summary><b>💡 Resposta</b></summary>

**(b)**. A declaração `package` vem primeiro, depois as importações e, por fim, as declarações de tipo.
</details>

**5. Qual arquivo descreve um módulo Java?**

<details>
<summary><b>💡 Resposta</b></summary>

`module-info.java`.
</details>

**6. As duas formas abaixo podem imprimir a mesma mensagem no Java 25?**

```java
public class Ola {
    public static void main(String[] args) {
        System.out.println("Olá");
    }
}
```

```java
void main() {
    IO.println("Olá");
}
```

<details>
<summary><b>💡 Resposta</b></summary>

Sim. A primeira é a forma tradicional adotada nos projetos do curso; a segunda usa um arquivo fonte compacto do Java 25.
</details>

## Referências

- [Certificação Oracle Certified Professional Java SE 25 Developer](https://education.oracle.com/java-se-25-developer-professional/pexam_1Z0-831)
- [OCPJ21 Study Guide - Chapter 13: Java Platform Module System](../ocpj21-book/ch13.md)
- [JEP 512: Compact Source Files and Instance Main Methods](https://openjdk.org/jeps/512)
- [JEP 511: Module Import Declarations](https://openjdk.org/jeps/511)

---

<div align="center">

⬅️ [A7 · Sintaxe simplificada do Java 25](./A7%20-%20Sintaxe%20simplificada%20do%20Java%2025.md) &nbsp;·&nbsp; 📂 [Seção 2](./README.md) &nbsp;·&nbsp; [Seção 3 · Estrutura sequencial](../secao-03-estrutura-sequencial/README.md) ➡️

</div>
