# Versões do Java (desde a versão 8)

## Cadência de lançamentos

Desde o Java 9 a Oracle publica uma nova versão a cada seis meses, sempre em **março** e **setembro**. A cada dois anos uma dessas versões é marcada como **LTS** (*Long-Term Support*), ou seja, recebe correções e atualizações de segurança por vários anos.

- **Versões LTS:** usadas em produção, porque a empresa consegue permanecer nelas por anos.
- **Versões intermediárias (*feature releases*):** recebem suporte apenas até a versão seguinte. Servem para experimentar recursos novos.

Os recursos entram na linguagem por meio de **JEPs** (*JDK Enhancement Proposals*), que são as propostas formais de evolução da plataforma. Um recurso costuma passar por estágios antes de virar definitivo:

- **Incubator / Preview:** disponível para testes, precisa ser habilitado explicitamente na compilação e na execução (`--enable-preview`) e ainda pode mudar ou ser removido.
- **Final:** faz parte da linguagem e não pode mais ser retirado sem um processo de depreciação.

> Provas de certificação cobram apenas recursos **finais** da versão correspondente. Recursos em *preview* não são cobrados.

## Resumo das versões LTS

| Versão      | Lançamento     |
|-------------|----------------|
| **Java 25** | setembro/2025  |
| **Java 21** | setembro/2023  |
| **Java 17** | setembro/2021  |
| **Java 11** | setembro/2018  |
| **Java 8**  | março/2014     |

## Java 25 (LTS)

Lançado em setembro de 2025. É a versão usada neste curso e a versão cobrada pela certificação **Oracle Certified Professional, Java SE 25 Developer (1Z0-831)**.

- Arquivos-fonte compactos e método `main` de instância (JEP 512)
- Declarações de importação de módulo — `import module` (JEP 511)
- Corpos de construtor flexíveis (JEP 513)
- *Scoped Values* finalizados (JEP 506)
- Cabeçalhos de objeto compactos, reduzindo o consumo de memória (JEP 519)

## Java 24

Lançado em março de 2025.

- *Stream Gatherers* finalizados, permitindo criar operações intermediárias próprias (JEP 485)
- API de *Class-File* finalizada (JEP 484)
- Carregamento e ligação de classes antecipados, melhorando o tempo de inicialização (JEP 483)
- *Security Manager* permanentemente desativado (JEP 486)

## Java 23

Lançado em setembro de 2024.

- Comentários de documentação em Markdown (JEP 467)
- Importação de módulos em prévia (JEP 476)
- ZGC no modo geracional por padrão (JEP 474)

## Java 22

Lançado em março de 2024.

- API de Função e Memória Externa finalizada (JEP 454)
- Variáveis e padrões sem nome, usando `_` (JEP 456)
- Execução de programas com vários arquivos-fonte sem compilação prévia (JEP 458)

## Java 21 (LTS)

Lançado em setembro de 2023.

- *Virtual Threads* finalizadas (JEP 444)
- *Sequenced Collections* (JEP 431)
- *Record Patterns* e *Pattern Matching* para `switch` finalizados (JEP 440 e JEP 441)
- ZGC geracional (JEP 439)

## Java 20

Lançado em março de 2023.

- Novas prévias de *Virtual Threads*, *Scoped Values* e *Record Patterns*

## Java 19

Lançado em setembro de 2022.

- *Virtual Threads* em prévia (JEP 425)
- Concorrência estruturada em incubação (JEP 428)
- *Record Patterns* em prévia (JEP 405)

## Java 18

Lançado em março de 2022.

- Servidor web simples para testes (JEP 408)
- UTF-8 como conjunto de caracteres padrão (JEP 400)

## Java 17 (LTS)

Lançado em setembro de 2021.

- Classes seladas (*sealed classes*) finalizadas
- Nova API de números aleatórios
- Remoção do compilador experimental AOT e JIT em Java

## Java 16

Lançado em março de 2021.

- *Records* finalizados
- `instanceof` com *pattern matching* finalizado

## Java 15

Lançado em setembro de 2020.

- *Text Blocks* finalizados
- Classes seladas em prévia

## Java 14

Lançado em março de 2020.

- Expressões `switch` finalizadas
- *Records* em prévia
- Mensagens mais úteis para `NullPointerException`

## Java 13

Lançado em setembro de 2019.

- *Text Blocks* em prévia

## Java 12

Lançado em março de 2019.

- Melhorias no coletor G1
- Expressões `switch` em prévia

## Java 11 (LTS)

Lançado em setembro de 2018.

- Cliente HTTP padronizado
- Novos métodos de `String` e `Files`
- Execução direta de um único arquivo-fonte com `java Arquivo.java` (JEP 330)
- Remoção dos módulos Java EE e CORBA

## Java 10

Lançado em março de 2018.

- Inferência de tipo para variáveis locais com `var`

## Java 9

Lançado em setembro de 2017.

- Sistema de módulos, o *Project Jigsaw* (JEP 261)
- JShell, o console interativo do Java
- Início da cadência semestral de lançamentos

## Java 8 (LTS)

Lançado em março de 2014.

- Expressões lambda e referências de método
- API de *Streams*
- Nova API de data e hora (`java.time`)
- Métodos `default` em interfaces
