# Depuração no Eclipse

<sub>📚 [Documentação](../README.md) › [Seção 5 · Estruturas repetitivas](./README.md) › Material 1 de 8</sub>

Depurar é executar o programa de forma controlada para observar o que acontece em cada linha. Em vez de tentar adivinhar por que um resultado saiu errado, o aluno acompanha o fluxo e verifica o valor das variáveis.

O depurador não corrige o programa. Ele mostra evidências para que o programador encontre a linha em que o comportamento se afastou do esperado.

## Programa usado na demonstração

Comece com um código formado apenas por conteúdos já estudados:

```java
public class ExemploDebug {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;
        int quociente = a / b;
        int resto = a % b;

        if (resto == 0) {
            System.out.println("Divisao exata");
        } else {
            System.out.println("Quociente: " + quociente);
            System.out.println("Resto: " + resto);
        }
    }
}
```

Antes de depurar, faça a previsão: `quociente` deve valer `3`, `resto` deve valer `1` e o programa deve seguir pelo `else`.

## Ponto de interrupção

Um **ponto de interrupção**, ou *breakpoint*, marca uma linha em que a execução deve parar temporariamente.

No Eclipse:

1. abra o arquivo Java;
2. dê dois cliques na margem esquerda da linha `int a = 10;`, ou use **Run > Toggle Breakpoint**;
3. confirme que apareceu um marcador ao lado da linha;
4. execute com **Debug As > Java Application**.

Quando o programa chegar ao ponto marcado, o Eclipse suspende a execução e normalmente oferece a perspectiva **Debug**.

## Linha atual e próxima instrução

A linha destacada é a próxima instrução que será executada. Isso significa que, ao parar sobre `int a = 10;`, a variável `a` ainda não recebeu `10`.

Depois de avançar uma linha, a atribuição já aconteceu e `a` aparece na visualização de variáveis.

Essa distinção evita um erro comum: olhar a linha destacada e imaginar que ela já foi concluída.

## Comandos principais

| Ação | Atalho comum | O que faz |
| --- | :---: | --- |
| Step Over | `F6` | executa a linha atual e para na próxima linha do mesmo método |
| Step Into | `F5` | entra no método chamado pela linha atual |
| Step Return | `F7` | termina o método atual e volta ao chamador |
| Resume | `F8` | continua até o próximo breakpoint ou até o fim |
| Terminate | botão quadrado | encerra a execução |

Nesta etapa, **Step Over** é o comando principal. O programa está inteiro no `main`, e ainda não é necessário entrar no funcionamento interno de `println` ou de outras classes.

> [!NOTE]
> Os atalhos podem variar conforme o sistema e as configurações da IDE. Os comandos também estão disponíveis nos menus e na barra da perspectiva Debug.

## Visualização Variables

A aba **Variables** mostra os nomes e os valores disponíveis no ponto atual.

Ao avançar pelo exemplo, a evolução esperada é:

| Depois de executar | Variáveis observáveis |
| --- | --- |
| `int a = 10;` | `a = 10` |
| `int b = 3;` | `a = 10`, `b = 3` |
| `int quociente = a / b;` | `quociente = 3` |
| `int resto = a % b;` | `resto = 1` |
| condição do `if` | o fluxo avança para o bloco do `else` |

Os valores no depurador devem ser comparados com o teste de mesa feito antes da execução.

## Depurando uma condição

Coloque um breakpoint na linha do `if` e use Step Over. O Eclipse mostra qual linha será executada em seguida:

- se `resto == 0` for `true`, o destaque entra no primeiro bloco;
- se for `false`, o destaque salta para o bloco do `else`.

Esse salto é a representação concreta do fluxo condicional estudado na Seção 4.

## Depurando uma repetição

Depois de estudar `while`, use este trecho:

```java
int contador = 1;
int soma = 0;

while (contador <= 3) {
    soma += contador;
    contador++;
}

System.out.println(soma);
```

Coloque o breakpoint na condição do `while` e avance com Step Over. A linha da condição será visitada várias vezes, e a aba Variables mostrará `contador` e `soma` mudando.

| Chegada à condição | `contador` | `soma` | Condição |
| ---: | ---: | ---: | :---: |
| 1ª | 1 | 0 | `true` |
| 2ª | 2 | 1 | `true` |
| 3ª | 3 | 3 | `true` |
| 4ª | 4 | 6 | `false` |

A condição é avaliada quatro vezes, embora o corpo execute três. O depurador ajuda a enxergar essa diferença.

## Breakpoint condicional ainda não é necessário

O Eclipse permite configurar um breakpoint para suspender apenas quando uma expressão for verdadeira. Esse recurso é útil em repetições longas, mas não é necessário nos primeiros exercícios. Primeiro domine:

- breakpoint simples;
- Step Over;
- visualização de variáveis;
- comparação com o teste de mesa;
- Resume e Terminate.

## Roteiro para investigar um erro

1. escreva qual resultado era esperado;
2. escolha uma linha antes do ponto em que o resultado fica errado;
3. coloque o breakpoint;
4. execute em modo Debug;
5. avance com Step Over;
6. compare cada valor com sua previsão;
7. pare na primeira divergência;
8. revise a expressão ou condição responsável por ela.

A primeira divergência costuma ser mais útil que a última linha errada, porque erros anteriores se propagam.

## Referências

- [Eclipse Help - Debugging your programs](https://help.eclipse.org/latest/topic/org.eclipse.jdt.doc.user/gettingStarted/qs-13.htm).
- [Eclipse Help - Stepping through the execution of a Java program](https://help.eclipse.org/latest/topic/org.eclipse.jdt.doc.user/tasks/task-stepping.htm).

---

<div align="center">

📂 [Seção 5](./README.md) &nbsp;·&nbsp; [A2 · Estrutura repetitiva while](./A2%20-%20Estrutura%20repetitiva%20while.md) ➡️

</div>
