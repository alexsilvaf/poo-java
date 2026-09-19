# Seção 7 — Introdução à Programação Orientada a Objetos

<sub>📚 [Documentação](../README.md) › Seção 7</sub>

| 🎓 Aulas do curso | 🎬 Aulas de referência | ⏱️ Duração na grade | 🖥️ Slides |
| :---: | :---: | :---: | :---: |
| 64 a 75 | 69 a 80 | 1 h 29 min | — |

## 🎯 Objetivos

Ao final desta seção, o aluno deverá ser capaz de:

- explicar a relação entre classe, objeto, atributo e método;
- criar objetos simples e acessar seus membros;
- distinguir valor primitivo de valor de referência;
- acompanhar conceitualmente referências na stack e objetos na heap;
- explicar o papel básico do coletor de lixo;
- comparar membros de instância e membros estáticos;
- usar `toString` para obter uma representação textual de um objeto.

## 📚 Conteúdos

- **A1** · [O problema dos triângulos sem orientação a objetos](./A1%20-%20O%20problema%20dos%20triangulos%20sem%20orientacao%20a%20objetos.md)
- **A2** · [Classes, objetos e atributos](./A2%20-%20Classes%20objetos%20e%20atributos.md)
- **A3** · [Métodos de instância](./A3%20-%20Metodos%20de%20instancia.md)
- **A4** · [Referências, stack, heap e coleta de lixo](./A4%20-%20Referencias%20stack%20heap%20e%20coleta%20de%20lixo.md)
- **A5** · [`Object` e `toString`](./A5%20-%20Object%20e%20toString.md)
- **A6** · [Problema de exemplo: estoque de produtos](./A6%20-%20Problema%20de%20exemplo%20estoque%20de%20produtos.md)
- **A7** · [Membros estáticos e membros de instância](./A7%20-%20Membros%20estaticos%20e%20membros%20de%20instancia.md)
- **A8** · [A certificação OCP Java SE 25 e esta seção](./A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md)

## 🗓️ Planejamento das aulas

| Aula | Tema | Atividade ou recurso | Observações |
| ---: | --- | --- | --- |
| 1 | Limites do código apenas com variáveis | Resolver e comparar áreas de dois triângulos | O incômodo da repetição cria a necessidade da classe |
| 2 | Classe, objeto e atributo | Modelar `Triangle` e criar duas instâncias | Ainda sem construtores ou membros privados |
| 3 | Métodos de instância | Mover o cálculo de área para o objeto | Retomar os métodos `static` da Seção 6 por contraste |
| 4 | Referências e memória | Simular atribuição, aliasing, `null` e elegibilidade para coleta | Usar o diagrama conceitual, sem endereços de memória |
| 5 | `Object` e `toString` | Comparar a saída padrão com uma representação útil | Herança será apenas reconhecida, não aprofundada |
| 6 | Estoque de produtos | Criar operações que alteram o estado de um produto | Campos ainda estão expostos para preservar a progressão |
| 7 | `static` e instância | Classificar membros e criar um utilitário de conversão | Introduzir constantes com `static final` |
| 8 | Revisão e OCPJ25 | Prever compilação, saída e estado dos objetos | Consolidar antes de apresentar construtores |

## 📝 Observações

- Esta seção recebe explicitamente os conceitos de objetos, referências, stack, heap e coleta de lixo que foram adiados nas Seções 2, 3 e 6.
- A explicação de memória deve permanecer conceitual e ligada ao ciclo de vida dos objetos. Detalhes de implementação da JVM não são pré-requisitos para criar a primeira classe.
- Construtores, `this`, sobrecarga, encapsulamento e modificadores de acesso ficam concentrados na Seção 8.
- Igualdade lógica com `equals`, cópia de objetos e referências em arrays ou coleções ficam para seções posteriores.
- A cobertura global da certificação é acompanhada em [Cobertura OCP Java SE 25](../README.md#cobertura-ocpj25).

---

<div align="center">

⬅️ [Seção 6 · Outros tópicos básicos sobre Java](../secao-06-outros-topicos-basicos/README.md) &nbsp;·&nbsp; 📚 [Documentação](../README.md) &nbsp;·&nbsp; [Seção 8 · Construtores, palavra this, sobrecarga e encapsulamento](../secao-08-construtores-this-sobrecarga-encapsulamento/README.md) ➡️

</div>
