# Restrições e convenções para nomes

<sub>📚 [Documentação](../README.md) › [Seção 6 · Outros tópicos básicos sobre Java](./README.md) › Material 1 de 8</sub>

Um **identificador** é o nome escolhido para uma variável, classe, método, pacote ou outro elemento do programa. Algumas regras são verificadas pelo compilador. Outras são convenções que tornam o código previsível para quem lê.

## Regras obrigatórias

Um identificador pode conter letras, algarismos, `_` e `$`, mas não pode:

- começar com algarismo;
- ser uma palavra reservada, como `class`, `int`, `if`, `for` ou `return`;
- ser apenas `_`;
- conter espaço, hífen ou sinais como `@`, `#` e `%`.

```java
int idade = 20;
int nota2 = 8;
int _indice = 0;
int valor$temporario = 10;
```

Os exemplos acima compilam. Os seguintes não:

```java
// int 2nota = 8;       // começa com algarismo
// int valor-total = 5; // hífen não é permitido
// int class = 1;       // palavra reservada
// int _ = 3;           // _ sozinho é palavra reservada
```

O caractere `$` é permitido, mas costuma aparecer em código gerado por ferramentas. Evite usá-lo em nomes escritos manualmente.

## Maiúsculas e minúsculas importam

Java diferencia letras maiúsculas de minúsculas:

```java
int total = 10;
int Total = 20;

System.out.println(total); // 10
System.out.println(Total); // 20
```

Os dois nomes são válidos e representam variáveis diferentes. Mesmo assim, escolher nomes que diferem apenas pela capitalização dificulta a leitura.

## Palavras reservadas e literais especiais

Palavras reservadas fazem parte da sintaxe da linguagem. Além delas, `true`, `false` e `null` não podem ser usados como identificadores.

```java
// int true = 1;
// String null = "texto";
```

> [!TIP]
> Não é necessário memorizar toda a lista imediatamente. A IDE destaca essas palavras e o compilador informa o erro. Para a OCPJ25, porém, é preciso reconhecer nomes evidentemente inválidos.

## Convenções de nomenclatura

| Elemento | Convenção | Exemplos |
| --- | --- | --- |
| variável | `camelCase` | `precoFinal`, `quantidadeItens` |
| método | `camelCase`, geralmente começando por verbo | `calcularMedia`, `mostrarMenu` |
| classe | `PascalCase` | `ContaBancaria`, `Calculadora` |
| constante | maiúsculas com `_` | `TAXA_JUROS`, `LIMITE_MAXIMO` |
| pacote | minúsculas, domínio invertido | `br.com.exemplo.curso` |

Convenções não mudam o resultado do programa, mas comunicam a função do nome.

```java
final double TAXA_DESCONTO = 0.10;
double precoFinal = 90.0;
```

## Nomes que explicam a intenção

Compare:

```java
double x = 120.0;
double y = x * 0.90;
```

com:

```java
double preco = 120.0;
double precoComDesconto = preco * 0.90;
```

O segundo trecho permite entender o cálculo sem procurar uma explicação externa.

## Exercício rápido

Classifique cada nome como válido ou inválido e, quando válido, diga se segue a convenção:

1. `saldoAtual`
2. `SaldoAtual`
3. `3tentativas`
4. `valor_total`
5. `LIMITE_TENTATIVAS`
6. `_`
7. `class`
8. `calcularArea`

Respostas esperadas:

- válidos: `saldoAtual`, `SaldoAtual`, `valor_total`, `LIMITE_TENTATIVAS`, `calcularArea`;
- inválidos: `3tentativas`, `_`, `class`;
- `SaldoAtual` parece nome de classe; `valor_total` compila, mas a convenção para variável seria `valorTotal`.

## Referências

- [Java Language Specification 25 - Identifiers](https://docs.oracle.com/javase/specs/jls/se25/html/jls-3.html#jls-3.8).
- [Java Language Specification 25 - Keywords](https://docs.oracle.com/javase/specs/jls/se25/html/jls-3.html#jls-3.9).

---

<div align="center">

📂 [Seção 6](./README.md) &nbsp;·&nbsp; [A2 · Operadores bitwise](./A2%20-%20Operadores%20bitwise.md) ➡️

</div>
