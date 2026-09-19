# A certificação OCP Java SE 25 e esta seção

<sub>📚 [Documentação](../README.md) › [Seção 6 · Outros tópicos básicos sobre Java](./README.md) › Material 8 de 8</sub>

Este material relaciona a Seção 6 com a certificação **Oracle Certified Professional, Java SE 25 Developer** (exame **1Z0-831**). Ele revisa somente identificadores, operadores, `String`, comentários e métodos compatíveis com o conteúdo estudado até aqui.

> [!IMPORTANT]
> Concluir esta seção não significa concluir a preparação para a OCPJ25. A matriz [Cobertura OCP Java SE 25](../README.md#cobertura-ocpj25) registra os domínios já apresentados e os que ainda exigem seções futuras.

## Grupos de objetivos relacionados

| Grupo de objetivos | Conteúdo desta seção |
| --- | --- |
| Handling Date, Time, Text, Numeric and Boolean Values | identificadores, operadores bitwise, imutabilidade e métodos de `String` |
| Implementing Program Flow Control | uso de métodos com decisões, laços e retornos antecipados |
| Applying Object-Oriented Principles | sintaxe inicial de métodos, parâmetros e passagem por valor |

## O que desta seção cai na prova

### Identificadores

- o primeiro caractere não pode ser algarismo;
- palavras reservadas, `true`, `false` e `null` não são identificadores;
- `_` sozinho é reservado, mas pode aparecer em nomes maiores;
- Java diferencia maiúsculas de minúsculas;
- convenções de nomes não interferem na compilação.

### Operadores bitwise

- `&`, `|` e `^` funcionam com tipos inteiros e também com `boolean`;
- `~` inverte todos os bits de um valor inteiro;
- `<<` desloca à esquerda;
- `>>` preserva o sinal;
- `>>>` insere zeros à esquerda;
- as formas `&=`, `|=`, `^=`, `<<=`, `>>=` e `>>>=` fazem atribuição cumulativa;
- `&` e `|` sobre `boolean` avaliam os dois operandos, ao contrário do possível curto-circuito de `&&` e `||`.

### `String`

- índices começam em zero e o fim de `substring(inicio, fim)` é exclusivo;
- `indexOf` devolve `-1` quando não encontra;
- `equals` compara conteúdo e `equalsIgnoreCase` ignora diferenças de caixa;
- `isEmpty` testa tamanho zero; `isBlank` também aceita apenas espaços em branco;
- `String` é imutável, portanto chamadas como `strip` e `replace` não alteram a variável existente;
- chamadas encadeadas são avaliadas da esquerda para a direita.

`StringBuilder`, pool de strings, comparação de referências e detalhes de memória dependem do estudo de objetos. Eles não foram removidos do curso: permanecem registrados para seções posteriores.

### Métodos

- parâmetros são declarados com tipo e nome;
- argumentos precisam ser compatíveis e respeitar a ordem dos parâmetros;
- um método `void` não produz valor para uma expressão;
- um método com tipo de retorno precisa devolver um valor compatível em todos os caminhos alcançáveis;
- `return` encerra a execução daquele método;
- Java passa argumentos por valor;
- parâmetros e variáveis locais ficam limitados ao bloco do método.

Sobrecarga será estudada na Seção 8. Varargs dependem de arrays e ficam para a seção correspondente.

## Questões no estilo da prova

**1. Quais declarações compilam?**

```java
int _valor = 1;
int $total = 2;
int valor2 = 3;
// int 2valor = 4;
// int _ = 5;
```

<details>
<summary><b>💡 Resposta</b></summary>

Compilam `_valor`, `$total` e `valor2`. Um identificador não começa por algarismo e `_` sozinho é reservado.
</details>

**2. Qual é a saída?**

```java
int a = 0b1100;
int b = 0b1010;

System.out.println(a & b);
System.out.println(a | b);
System.out.println(a ^ b);
```

<details>
<summary><b>💡 Resposta</b></summary>

`8`, `14` e `6`, cada um em sua linha.
</details>

**3. Qual é a saída?**

```java
System.out.println(8 << 2);
System.out.println(16 >> 2);
```

<details>
<summary><b>💡 Resposta</b></summary>

`32` e `4`.
</details>

**4. Qual é o valor final de `x`?**

```java
int x = 0;
boolean resultado = false & (x++ > 0);
```

<details>
<summary><b>💡 Resposta</b></summary>

`x` vale 1. O operador booleano `&` avalia os dois lados. Com `false && (x++ > 0)`, o curto-circuito manteria `x` em 0.
</details>

**5. Qual é a saída?**

```java
String nome = "  Ana  ";
nome.strip();
System.out.println("[" + nome + "]");
```

<details>
<summary><b>💡 Resposta</b></summary>

`[  Ana  ]`. `String` é imutável e o resultado de `strip()` não foi guardado.
</details>

**6. Qual é a saída?**

```java
String texto = "certificacao";
System.out.println(texto.substring(0, 5));
System.out.println(texto.indexOf('f'));
```

<details>
<summary><b>💡 Resposta</b></summary>

`certi` e `5`. O fim do `substring` não entra no resultado.
</details>

**7. Qual é a saída?**

```java
String resposta = "Java";

System.out.println(resposta.equals("java"));
System.out.println(resposta.equalsIgnoreCase("java"));
```

<details>
<summary><b>💡 Resposta</b></summary>

`false` e `true`.
</details>

**8. O código compila?**

```java
static int sinal(int numero) {
    if (numero > 0) {
        return 1;
    }
}
```

<details>
<summary><b>💡 Resposta</b></summary>

Não. Falta devolver um `int` quando `numero <= 0`.
</details>

**9. Qual é a saída?**

```java
static void alterar(int valor) {
    valor = 50;
}

int numero = 10;
alterar(numero);
System.out.println(numero);
```

<details>
<summary><b>💡 Resposta</b></summary>

`10`. O parâmetro recebe uma cópia do valor de `numero`.
</details>

**10. O que é impresso?**

```java
String endereco = "https://exemplo.com";
System.out.println(endereco);
```

<details>
<summary><b>💡 Resposta</b></summary>

`https://exemplo.com`. O `//` está dentro do literal de texto e não inicia um comentário.
</details>

## Assuntos deliberadamente posteriores

| Assunto | Momento previsto |
| --- | --- |
| objetos, referências, heap, stack e coleta de lixo | Seção 7 e aprofundamentos posteriores |
| membros estáticos e de instância | Seção 7 |
| sobrecarga e modificadores de acesso | Seção 8 |
| arrays, varargs e `for-each` | seção futura de arrays |
| `StringBuilder`, pool de strings e identidade de referências | depois da introdução a objetos |
| wrappers e conversões completas | seção futura de APIs fundamentais |
| exceções, coleções, streams, módulos, concorrência, I/O e localização | seções futuras próprias |

## Referências

- [Certificação Oracle Certified Professional, Java SE 25 Developer](https://education.oracle.com/java-se-25-developer-professional/pexam_1Z0-831).
- [Java SE 25 API - String](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/String.html).
- [Java Language Specification 25 - Lexical Structure](https://docs.oracle.com/javase/specs/jls/se25/html/jls-3.html).
- [Java Language Specification 25 - Expressions](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html).
- [OCPJ21 Study Guide - Chapter 4: Working with Data](../ocpj21-book/ch04.md).

---

<div align="center">

⬅️ [A7 · Prática integrada](./A7%20-%20Pratica%20integrada.md) &nbsp;·&nbsp; 📂 [Seção 6](./README.md) &nbsp;·&nbsp; [Seção 7 · Introdução à Programação Orientada a Objetos](../secao-07-introducao-poo/README.md) ➡️

</div>
