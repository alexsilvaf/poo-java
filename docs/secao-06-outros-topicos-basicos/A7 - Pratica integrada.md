# Prática integrada

<sub>📚 [Documentação](../README.md) › [Seção 6 · Outros tópicos básicos sobre Java](./README.md) › Material 7 de 8</sub>

Esta prática combina `String`, decisões, repetições e métodos. Cada parte usa apenas conteúdos apresentados até a Seção 6.

## Exemplo 1: analisador de texto

O programa lê um texto, normaliza os espaços externos e informa tamanho, primeira e última letra, quantidade de vogais e presença da palavra `java`.

```java
import java.util.Scanner;

public class AnalisadorTexto {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite um texto: ");
        String texto = sc.nextLine();
        String normalizado = normalizar(texto);

        if (normalizado.isEmpty()) {
            System.out.println("O texto ficou vazio.");
        } else {
            System.out.println("Texto: " + normalizado);
            System.out.println("Tamanho: " + normalizado.length());
            System.out.println("Primeiro: " + normalizado.charAt(0));
            System.out.println("Ultimo: " + normalizado.charAt(normalizado.length() - 1));
            System.out.println("Vogais: " + contarVogais(normalizado));
            System.out.println("Contem java: " + contemJava(normalizado));
        }

        sc.close();
    }

    static String normalizar(String texto) {
        return texto.strip();
    }

    static int contarVogais(String texto) {
        int quantidade = 0;

        for (int i = 0; i < texto.length(); i++) {
            char caractere = texto.toLowerCase().charAt(i);

            if (caractere == 'a' || caractere == 'e'
                    || caractere == 'i' || caractere == 'o'
                    || caractere == 'u') {
                quantidade++;
            }
        }

        return quantidade;
    }

    static boolean contemJava(String texto) {
        return texto.toLowerCase().contains("java");
    }
}
```

### Leitura gradual

1. `main` coordena entrada e saída.
2. `normalizar` devolve o texto sem espaços externos.
3. o `if` protege os acessos com `charAt` quando o texto está vazio;
4. `contarVogais` percorre os índices válidos;
5. `contemJava` produz um resultado `boolean`.

Uma melhoria simples evita recalcular a versão minúscula a cada repetição:

```java
static int contarVogais(String texto) {
    int quantidade = 0;
    String minusculo = texto.toLowerCase();

    for (int i = 0; i < minusculo.length(); i++) {
        char caractere = minusculo.charAt(i);

        if (caractere == 'a' || caractere == 'e'
                || caractere == 'i' || caractere == 'o'
                || caractere == 'u') {
            quantidade++;
        }
    }

    return quantidade;
}
```

## Exemplo 2: permissões com bits

Cada bit representa uma permissão:

```java
public class Permissoes {
    public static void main(String[] args) {
        int leitura = 0b0001;
        int escrita = 0b0010;
        int exclusao = 0b0100;

        int usuario = leitura | escrita;

        System.out.println(temPermissao(usuario, leitura));  // true
        System.out.println(temPermissao(usuario, escrita));  // true
        System.out.println(temPermissao(usuario, exclusao)); // false

        usuario |= exclusao;
        System.out.println(temPermissao(usuario, exclusao)); // true
    }

    static boolean temPermissao(int conjunto, int mascara) {
        return (conjunto & mascara) != 0;
    }
}
```

`|` liga bits. `&` verifica se o bit indicado pela máscara está ligado.

## Exercícios

1. Crie `static int contarEspacos(String texto)`.
2. Crie `static String primeiraMetade(String texto)` usando `substring`.
3. Crie `static boolean terminaComBr(String endereco)` sem diferenciar maiúsculas de minúsculas.
4. Crie `static int ativar(int conjunto, int mascara)` usando `|`.
5. Crie `static int desativar(int conjunto, int mascara)` usando `&` e `~`.
6. Extraia para métodos o cálculo de área e perímetro de um círculo feito na Seção 3.
7. Escreva comentários de documentação para dois dos métodos criados.

## Checklist

- o nome do método comunica sua tarefa?
- cada parâmetro possui tipo e nome?
- todo método não `void` devolve um valor em todos os caminhos?
- o chamador guarda o resultado quando precisa dele?
- índices usados em `charAt` e `substring` permanecem dentro do texto?
- transformações de `String` têm seu resultado atribuído ou devolvido?

---

<div align="center">

⬅️ [A6 · Parâmetros, retorno e passagem de valores](./A6%20-%20Parametros%20retorno%20e%20passagem%20de%20valores.md) &nbsp;·&nbsp; 📂 [Seção 6](./README.md) &nbsp;·&nbsp; [A8 · A certificação OCP Java SE 25 e esta seção](./A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md) ➡️

</div>
