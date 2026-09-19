# Seção 4 — Estrutura condicional

<sub>📚 [Documentação](../README.md) › Seção 4</sub>

| 🎓 Aulas do curso | 🎬 Aulas de referência | ⏱️ Duração na grade | 🖥️ Slides |
| :---: | :---: | :---: | :---: |
| 33 a 43 | 38 a 48 | 54 min | [abrir](./apresentacao.html) |

## 🎯 Objetivos

Ao final desta seção, o aluno deverá ser capaz de:

- construir expressões comparativas e interpretar seu resultado booleano;
- combinar condições com `&&`, `||` e `!`, respeitando a precedência dos operadores;
- explicar e aplicar a avaliação de curto-circuito;
- usar `if`, `if-else` e encadeamentos `else if` para controlar o fluxo do programa;
- escolher condições sem intervalos sobrepostos nem valores esquecidos;
- atualizar variáveis com operadores de atribuição cumulativa;
- usar `switch-case` quando uma decisão depende de valores exatos;
- empregar a expressão condicional ternária em decisões simples;
- reconhecer o escopo de uma variável e garantir sua inicialização antes do uso;
- fazer o teste de mesa de um programa com decisões.

## 🖥️ Apresentação

[apresentacao.html](./apresentacao.html) reúne os sete blocos da aula em slides, um por material, incluindo o diagrama desta seção. Basta abrir o arquivo no navegador; navegação por <kbd>←</kbd> <kbd>→</kbd> ou <kbd>Espaço</kbd>, <kbd>Esc</kbd> para a visão geral e <kbd>F</kbd> para tela cheia.

> [!NOTE]
> A imagem do Duke (`duke.svg`) é de autoria de sbmehta, obtida no Wikimedia Commons e distribuída sob **licença BSD** — o Duke foi liberado como código aberto pela Sun Microsystems em 2006.

## 📚 Conteúdos

- **A1** · [Expressões comparativas](./A1%20-%20Expressoes%20comparativas.md)
- **A2** · [Expressões lógicas](./A2%20-%20Expressoes%20logicas.md)
- **A3** · [Estrutura condicional if-else](./A3%20-%20Estrutura%20condicional%20if-else.md)
- **A4** · [Operadores de atribuição cumulativa](./A4%20-%20Operadores%20de%20atribuicao%20cumulativa.md)
- **A5** · [Estrutura switch-case](./A5%20-%20Estrutura%20switch-case.md)
- **A6** · [Expressão condicional ternária](./A6%20-%20Expressao%20condicional%20ternaria.md)
- **A7** · [Escopo e inicialização](./A7%20-%20Escopo%20e%20inicializacao.md)
- **A8** · [A certificação OCP Java SE 25 e esta seção](./A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md)

## 🗓️ Planejamento da aula

| Tempo | Conteúdo | Condução sugerida |
| :---: | --- | --- |
| 0-10 min | Expressões comparativas | Avaliar comparações simples no `jshell` ou na IDE e guardar os resultados em variáveis `boolean` |
| 10-22 min | Expressões lógicas | Construir as tabelas-verdade e demonstrar o curto-circuito com uma divisão protegida |
| 22-40 min | `if`, `if-else` e `else if` | Montar gradualmente um programa de classificação de notas e fazer seu teste de mesa |
| 40-48 min | Atribuição cumulativa | Transformar cálculos como `saldo = saldo - saque` em `saldo -= saque` e discutir a diferença de tipo |
| 48-60 min | `switch-case` | Reescrever uma escolha de dia da semana, primeiro com `if-else` e depois com `switch` |
| 60-68 min | Operador ternário | Substituir somente decisões simples que produzem um valor |
| 68-82 min | Escopo e inicialização | Provocar erros de variável fora do bloco e de variável possivelmente não inicializada, depois corrigi-los |
| 82-90 min | Fechamento e prática | Comparar as alternativas, fazer um teste de mesa final e encaminhar os exercícios do Estudante360 |

> [!TIP]
> A grade de referência soma aproximadamente 54 minutos. Em um encontro de 60 minutos, o corte natural é manter `switch`, ternário e atribuição cumulativa como leitura guiada, preservando mais tempo para `if-else`, expressões lógicas e teste de mesa.

## 📝 Observações

- A ordem dos materiais é intencional: uma condição simples aparece antes de combinações lógicas, e ambas aparecem antes do primeiro `if`.
- Todos os exemplos usam apenas conteúdos das Seções 1 a 3 e o tópico que está sendo introduzido. Não são necessários arrays, coleções, métodos próprios, exceções nem orientação a objetos.
- O material usa chaves mesmo quando o bloco tem uma única instrução. Isso reduz erros durante a aprendizagem e facilita a inclusão de novas linhas.
- Cada um dos sete blocos da apresentação termina com um slide **Mão na massa**: cinco exercícios para fazer na IDE, na ordem em que o conteúdo foi apresentado. Vários pedem que o erro seja provocado de propósito antes da correção. Se o encontro estiver curto, eles funcionam como tarefa de casa.
- Três slides têm um **traçador**: ao clicar em um valor, o código acende só o caminho percorrido — o curto-circuito do `&&` (Bloco 2), a cadeia de `else if` (Bloco 3) e o *fall-through* do `switch` (Bloco 5). Vale pedir à turma que preveja o resultado antes do clique.
- Operadores cumulativos, incremento e decremento e a comparação de valores `double` são apresentados aqui pela primeira vez; a Seção 3 mantém todas as atualizações na forma explícita.
- A comparação de textos por conteúdo ainda não é necessária nos exemplos centrais. O material explica apenas por que `==` não deve ser usado para esse fim e adia o aprofundamento em objetos.
- Os exercícios para iniciantes das aulas 38 e 39 ficam no Estudante360 e não são versionados neste repositório.

---

<div align="center">

⬅️ [Seção 3 · Estrutura sequencial](../secao-03-estrutura-sequencial/README.md) &nbsp;·&nbsp; 📚 [Documentação](../README.md) &nbsp;·&nbsp; [Seção 5 · Estruturas repetitivas](../secao-05-estruturas-repetitivas/README.md) ➡️

</div>
