# Linguagem de programação

Uma linguagem de programação possui regras léxicas, sintáticas e semânticas para representar instruções de maneira precisa.

## Léxica

Diz respeito à formação dos elementos individuais da linguagem, chamados de *tokens*. Palavras-chave, identificadores, números, operadores e símbolos precisam ser escritos de maneira válida.

### Exemplo

Na língua portuguesa, `cachorro` e `caxorro` ilustram a diferença ortográfica. Em uma linguagem de programação, um exemplo comum de erro léxico é iniciar uma sequência de texto e não usar o delimitador de fechamento:

| Certo | Errado |
| --- | --- |
| `"Olá"` | `"Olá` |

Os tokens disponíveis e as regras para escrevê-los são definidos por cada linguagem.

## Sintática

Diz respeito à maneira como os elementos da linguagem podem ser combinados para formar instruções válidas.

### Exemplo

| Certo | Errado |
| --- | --- |
| O cachorro está com fome. | A cachorro está com fome. |
| A comida é boa. | A é boa comida. |

### Exemplo em uma linguagem de programação

| Certo | Errado | Separação em tokens |
| --- | --- | --- |
| `x = 2 + y;` | `x = + 2 y;` | `x` · `=` · `2` · `+` · `y` · `;` |
| `int idade = 20;` | `int idade = ;` | `int` · `idade` · `=` · `20` · `;` |

## Semântica

Diz respeito ao significado de uma instrução. Um programa pode respeitar as regras léxicas e sintáticas e, ainda assim, produzir um resultado diferente do esperado.

### Exemplo

Para calcular a média de `x` e `y`, a expressão correta é:

```text
media = (x + y) / 2
```

Sem os parênteses, `x + y / 2` normalmente realiza primeiro a divisão e produz outro resultado.

## Tipos de erro

- **Erro léxico ou sintático:** impede a tradução do programa.
- **Erro de execução:** ocorre enquanto o programa está sendo executado.
- **Erro semântico ou lógico:** o programa executa, mas produz um comportamento incorreto.
