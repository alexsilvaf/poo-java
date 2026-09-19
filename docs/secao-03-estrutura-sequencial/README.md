# Seção 3 — Estrutura sequencial

<sub>📚 [Documentação](../README.md) › Seção 3</sub>

| 🎓 Aulas do curso | 🎬 Aulas de referência | ⏱️ Duração na grade | 🖥️ Slides |
| :---: | :---: | :---: | :---: |
| 21 a 32 | 26 a 37 | 1 h 14 min | [abrir](./apresentacao.html) |

## 🎯 Objetivos

Ao final desta seção, o aluno deverá ser capaz de:

- declarar variáveis, escolher o tipo primitivo adequado e reconhecer os oito tipos primitivos;
- distinguir tipos primitivos de tipos por referência, reconhecendo `String` como o primeiro exemplo por referência;
- avaliar expressões aritméticas e prever o resultado da divisão inteira e da divisão real;
- usar o operador `%` e a precedência de operadores para traduzir fórmulas para código;
- identificar as três operações básicas — entrada, processamento e saída — em um programa sequencial;
- imprimir resultados com `print`, `println` e `printf`, controlando casas decimais e alinhamento;
- aplicar conversão implícita e casting explícito, e prever a promoção numérica em expressões;
- ler dados do teclado com `Scanner`, evitando as armadilhas de `nextLine` e de `Locale`;
- usar as funções da classe `Math` mais frequentes;
- fazer o teste de mesa de um programa sequencial antes de executá-lo.

## 🖥️ Apresentação

[apresentacao.html](./apresentacao.html) reúne os seis blocos da aula em slides, incluindo os diagramas desta seção. Basta abrir o arquivo no navegador; navegação por <kbd>←</kbd> <kbd>→</kbd> ou <kbd>Espaço</kbd>, <kbd>Esc</kbd> para a visão geral e <kbd>F</kbd> para tela cheia.

> [!NOTE]
> A imagem do Duke (`duke.svg`) é de autoria de sbmehta, obtida no Wikimedia Commons e distribuída sob **licença BSD** — o Duke foi liberado como código aberto pela Sun Microsystems em 2006.

## 📚 Conteúdos

- **A1** · [Variáveis e tipos básicos em Java](./A1%20-%20Variaveis%20e%20tipos%20basicos.md)
- **A2** · [Expressões aritméticas](./A2%20-%20Expressoes%20aritmeticas.md)
- **A3** · [As três operações básicas de programação](./A3%20-%20As%20tres%20operacoes%20basicas.md)
- **A4** · [Saída de dados em Java](./A4%20-%20Saida%20de%20dados%20em%20Java.md)
- **A5** · [Processamento de dados e casting](./A5%20-%20Processamento%20de%20dados%20e%20casting.md)
- **A6** · [Entrada de dados em Java](./A6%20-%20Entrada%20de%20dados%20em%20Java.md)
- **A7** · [Funções matemáticas em Java](./A7%20-%20Funcoes%20matematicas%20em%20Java.md)
- **A8** · [A certificação OCP Java SE 25 e esta seção](./A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md)

## 🗓️ Planejamento da aula

| Tempo | Conteúdo | Condução sugerida |
| :---: | --- | --- |
| 0–15 min | Variáveis e tipos básicos | Usar a tabela e o diagrama do A1; mostrar ao vivo os erros de literal (`long` sem `L`, `float` sem `f`) |
| 15–25 min | Expressões aritméticas | Percorrer o A2 no `jshell` ou na IDE, insistindo em `10 / 3` contra `10.0 / 3` e nos usos do `%` |
| 25–32 min | As três operações básicas | Apresentar o diagrama do A3 e fazer um teste de mesa no quadro |
| 32–47 min | Saída de dados | Escrever ao vivo os exemplos de `printf` do A4, incluindo a tabela alinhada e o `Locale.setDefault` |
| 47–57 min | Processamento e casting | Demonstrar o casting do A5 e a promoção numérica que impede `byte soma = a + b;` |
| 57–75 min | Entrada de dados com `Scanner` | Codar o programa completo do A6, provocando de propósito a falha do `nextLine` depois do `nextInt` |
| 75–85 min | Funções matemáticas | Resolver o exercício da distância entre dois pontos do A7 |
| 85–90 min | Fechamento e exercícios | Retomar os erros comuns e encaminhar a lista de exercícios para iniciantes |

> [!TIP]
> A seção é a mais longa das primeiras: 1 h 14 min de vídeo na grade de referência. Se o encontro for de 60 minutos, o corte natural é deixar o A7 (funções matemáticas) como leitura, já que ele é o material mais autoexplicativo.

## 📝 Observações

- Cada um dos seis blocos da apresentação termina com um slide **Mão na massa**: cinco exercícios para o aluno fazer na IDE, na ordem em que o conteúdo foi apresentado. São exercícios de digitar e executar — vários pedem que o erro seja provocado de propósito antes da correção. Se o encontro estiver curto, eles funcionam como tarefa de casa sem depender de material extra.
- O `Locale` aparece duas vezes com efeitos opostos: na **saída** (`printf`) e na **entrada** (`Scanner`). Vale fixar uma convenção com a turma logo no começo — o curso usa `Locale.setDefault(Locale.US)` — para não misturar vírgula e ponto entre a leitura e a impressão.
- A falha do `nextLine()` depois de um `nextInt()` é a dúvida mais recorrente da seção. Provocar o erro ao vivo, antes de mostrar a correção, costuma fixar melhor do que apenas avisar.
- `var` e *text blocks* aparecem apenas para reconhecimento. Os exemplos principais continuam usando declarações explícitas e strings comuns.
- Operadores cumulativos, incremento, comparações e condições foram retirados desta seção e ficam concentrados na Seção 4.
- Arrays, separação de texto e validação condicional da entrada ficam para as seções em que esses recursos forem ensinados.
- Os exercícios para iniciantes (aulas 31 e 32) ficam no Estudante360 e não são versionados neste repositório.

---

<div align="center">

⬅️ [Seção 2 · Introdução à linguagem Java](../secao-02-introducao-java/README.md) &nbsp;·&nbsp; 📚 [Documentação](../README.md) &nbsp;·&nbsp; [Seção 4 · Estrutura condicional](../secao-04-estrutura-condicional/README.md) ➡️

</div>
