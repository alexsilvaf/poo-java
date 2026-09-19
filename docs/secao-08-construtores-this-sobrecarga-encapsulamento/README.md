# Seção 8 — Construtores, palavra this, sobrecarga e encapsulamento

<sub>📚 [Documentação](../README.md) › Seção 8</sub>

| 🎓 Aulas do curso | 🎬 Aulas de referência | ⏱️ Duração na grade | 🖥️ Slides |
| :---: | :---: | :---: | :---: |
| 76 a 83 | 81 a 88 | 52 min · parcial | — |

## 🎯 Objetivos

Ao final desta seção, o aluno deverá ser capaz de:

- declarar construtores e explicar quando existe um construtor padrão;
- criar objetos em estado inicial coerente;
- usar `this` para indicar a instância atual e resolver sombreamento de nomes;
- sobrecarregar métodos e construtores por meio de listas de parâmetros diferentes;
- encadear construtores com `this(...)`;
- acompanhar a ordem básica de inicialização de campos, blocos e construtores;
- aplicar encapsulamento com campos `private` e operações públicas;
- distinguir `public`, `protected`, acesso de pacote e `private`;
- reconhecer a regra de corpos flexíveis de construtores do Java 25 sem antecipar herança.

## 📚 Conteúdos

- **A1** · [Construtores](./A1%20-%20Construtores.md)
- **A2** · [A palavra `this`](./A2%20-%20A%20palavra%20this.md)
- **A3** · [Sobrecarga e encadeamento de construtores](./A3%20-%20Sobrecarga%20e%20encadeamento%20de%20construtores.md)
- **A4** · [Ordem de inicialização](./A4%20-%20Ordem%20de%20inicializacao.md)
- **A5** · [Encapsulamento, getters e setters](./A5%20-%20Encapsulamento%20getters%20e%20setters.md)
- **A6** · [Modificadores de acesso e geração pelo Eclipse](./A6%20-%20Modificadores%20de%20acesso%20e%20geracao%20pelo%20Eclipse.md)
- **A7** · [Prática integrada: conta bancária](./A7%20-%20Pratica%20integrada%20conta%20bancaria.md)
- **A8** · [A certificação OCP Java SE 25 e esta seção](./A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md)

## 🗓️ Planejamento das aulas

| Aula | Tema | Atividade ou recurso | Observações |
| ---: | --- | --- | --- |
| 1 | Construtores | Transformar a criação vazia de `Product` em criação válida | Comparar construtor padrão e construtor sem argumentos escrito pelo programador |
| 2 | `this` | Distinguir parâmetros, campos e instância atual | Ainda sem herança ou `super` |
| 3 | Sobrecarga | Criar assinaturas diferentes e encadear construtores | Resolver chamadas simples antes de conversões mais complexas |
| 4 | Inicialização | Rastrear valores padrão, inicializadores, blocos e construtor | Usar o diagrama da ordem básica |
| 5 | Encapsulamento | Tornar campos privados e definir operações públicas | Nem todo campo precisa de setter |
| 6 | Acesso e IDE | Classificar acessibilidade e revisar código gerado | `protected` é reconhecido; seu uso pleno virá com herança |
| 7 | Prática integrada | Implementar `BankAccount` com invariantes simples | Sem arrays, coleções ou exceções |
| 8 | Revisão e OCPJ25 | Resolver questões de compilação, saída e inicialização | Introduzir separadamente os corpos flexíveis de construtores, recurso final do Java 25 |

## 📝 Observações

- A seção parte dos objetos mutáveis e campos públicos da Seção 7; não exige herança, interfaces, arrays ou coleções.
- A ordem de inicialização fica limitada ao que pode ser demonstrado em uma classe simples. A ordem completa em hierarquias será retomada junto de herança.
- Corpos flexíveis de construtores são um recurso final do Java 25 (JEP 513) e aparecem nos objetivos da OCPJ25. A sintaxe é apresentada nesta seção, mas não é usada como requisito nos exemplos introdutórios; a regra completa, com `super(...)`, volta na Seção 10.
- Sobrecarga com varargs depende de arrays e fica para a seção correspondente.
- A cobertura global da certificação é acompanhada em [Cobertura OCP Java SE 25](../README.md#cobertura-ocpj25).

---

<div align="center">

⬅️ [Seção 7 · Introdução à Programação Orientada a Objetos](../secao-07-introducao-poo/README.md) &nbsp;·&nbsp; 📚 [Documentação](../README.md)

</div>
