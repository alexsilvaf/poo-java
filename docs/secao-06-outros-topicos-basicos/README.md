# Seção 6 — Outros tópicos básicos sobre Java

<sub>📚 [Documentação](../README.md) › Seção 6</sub>

| 🎓 Aulas do curso | 🎬 Aulas de referência | ⏱️ Duração na grade | 🖥️ Slides |
| :---: | :---: | :---: | :---: |
| 58 a 63 | 63 a 68 | 49 min | — |

## 🎯 Objetivos

Ao final desta seção, o aluno deverá ser capaz de:

- distinguir regras obrigatórias de convenções de nomenclatura;
- reconhecer identificadores válidos, palavras reservadas e o uso especial de `_`;
- interpretar operadores bit a bit e deslocamentos sobre valores inteiros;
- manipular textos com os métodos essenciais de `String`;
- comparar textos por conteúdo e explicar a imutabilidade de `String`;
- escrever comentários de linha, de bloco e de documentação;
- declarar e chamar métodos `static` simples;
- usar parâmetros, argumentos, tipos de retorno, `void` e `return`;
- decompor um problema sequencial em métodos pequenos;
- relacionar esses assuntos aos objetivos da OCP Java SE 25 sem antecipar orientação a objetos.

## 📚 Conteúdos

- **A1** · [Restrições e convenções para nomes](./A1%20-%20Restricoes%20e%20convencoes%20para%20nomes.md)
- **A2** · [Operadores bitwise](./A2%20-%20Operadores%20bitwise.md)
- **A3** · [Funções interessantes para String](./A3%20-%20Funcoes%20interessantes%20para%20String.md)
- **A4** · [Comentários em Java](./A4%20-%20Comentarios%20em%20Java.md)
- **A5** · [Métodos: declaração e chamada](./A5%20-%20Metodos%20declaracao%20e%20chamada.md)
- **A6** · [Parâmetros, retorno e passagem de valores](./A6%20-%20Parametros%20retorno%20e%20passagem%20de%20valores.md)
- **A7** · [Prática integrada](./A7%20-%20Pratica%20integrada.md)
- **A8** · [A certificação OCP Java SE 25 e esta seção](./A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md)

## 🗓️ Planejamento da aula

| Tempo | Conteúdo | Condução sugerida |
| :---: | --- | --- |
| 0-8 min | Identificadores e convenções | Classificar nomes válidos e inválidos antes de revisar `camelCase`, `PascalCase` e constantes |
| 8-22 min | Operadores bitwise | Representar valores pequenos em binário e calcular `&`, `|`, `^`, `~` e deslocamentos |
| 22-40 min | Métodos de `String` | Explorar índices, buscas, comparação por conteúdo, transformação e imutabilidade |
| 40-45 min | Comentários | Comparar `//`, `/* */` e `/** */`, incluindo os limites de aninhamento |
| 45-67 min | Métodos | Extrair cálculos já conhecidos para métodos `static` com parâmetros e retorno |
| 67-80 min | Passagem de valores | Alterar parâmetros locais e observar que a variável do chamador não muda |
| 80-90 min | Prática e OCPJ25 | Montar o analisador de texto e resolver questões curtas de previsão de saída |

> [!TIP]
> A grade de referência soma aproximadamente 49 minutos. O planejamento estendido reserva tempo para prática e para a ligação com a OCPJ25. Em um encontro de 60 minutos, a prática integrada pode ficar como atividade posterior.

## 📝 Observações

- A ordem é gradual: os métodos de biblioteca usados em `String` são observados primeiro; somente depois o aluno declara seus próprios métodos.
- Os métodos auxiliares permanecem `static` para serem chamados pelo `main`. A diferença completa entre membros estáticos e de instância pertence à Seção 7.
- Sobrecarga, varargs, arrays, referências mutáveis, pilha de chamadas e detalhes de heap não são necessários aqui. Esses assuntos ficam registrados para as seções correspondentes.
- `split`, `toCharArray` e métodos que devolvem arrays foram adiados até a apresentação de arrays.
- A cobertura global da certificação é acompanhada em [Cobertura OCP Java SE 25](../README.md#cobertura-ocpj25). A Seção 6 cobre apenas a parcela compatível com os pré-requisitos atuais.

---

<div align="center">

⬅️ [Seção 5 · Estruturas repetitivas](../secao-05-estruturas-repetitivas/README.md) &nbsp;·&nbsp; 📚 [Documentação](../README.md) &nbsp;·&nbsp; [Seção 7 · Introdução à Programação Orientada a Objetos](../secao-07-introducao-poo/README.md) ➡️

</div>
