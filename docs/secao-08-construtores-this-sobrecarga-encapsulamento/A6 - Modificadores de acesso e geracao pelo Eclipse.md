# Modificadores de acesso e geração pelo Eclipse

<sub>📚 [Documentação](../README.md) › [Seção 8 · Construtores, palavra this, sobrecarga e encapsulamento](./README.md) › Material 6 de 8</sub>

Java controla onde classes, construtores, campos e métodos podem ser acessados.

## Os quatro níveis para membros

| Declaração | Mesma classe | Mesmo pacote | Subclasse em outro pacote | Outro código em outro pacote |
| --- | :---: | :---: | :---: | :---: |
| `public` | sim | sim | sim | sim |
| `protected` | sim | sim | sim, pelas regras de herança | não |
| sem modificador | sim | sim | não | não |
| `private` | sim | não | não | não |

Quando nenhum modificador é escrito, o membro possui **acesso de pacote**. “Default” é um apelido comum para esse nível, mas não existe uma palavra-chave `default` usada para declará-lo.

```java
public int publicValue;
protected int protectedValue;
int packageValue;
private int privateValue;
```

O acesso `protected` possui detalhes adicionais em subclasses que estão em outro pacote. Eles serão praticados quando herança e packages forem combinados; por enquanto, guarde a tabela como visão inicial.

## Classes de topo

Uma classe declarada diretamente no arquivo, sem estar dentro de outra classe, pode ser:

- `public`; ou
- sem modificador, com acesso de pacote.

Ela não pode ser `private` nem `protected`:

```java
public class Product { }
class Helper { }

// private class Hidden { }   // não compila como classe de topo
// protected class Shared { } // não compila como classe de topo
```

Apenas uma classe de topo `public` pode aparecer em cada arquivo-fonte, e o arquivo deve ter o mesmo nome dela.

## Escolha prática

Para as classes de domínio desta etapa:

- classe pública para ser usada pelo programa;
- campos `private` para proteger o estado;
- construtores e operações `public` que fazem parte do uso normal;
- métodos auxiliares `private` quando forem apenas detalhes internos.

Exemplo:

```java
public class Product {
    private String name;
    private double price;

    public Product(String name, double price) {
        this.name = normalizeName(name);
        this.price = price;
    }

    private String normalizeName(String value) {
        return value.strip();
    }

    public String getName() {
        return name;
    }
}
```

## Gerando código no Eclipse

O Eclipse pode gerar construtores, getters, setters e `toString`. O fluxo geral é:

1. abra a classe no editor;
2. posicione o cursor dentro da classe;
3. abra o menu **Source**;
4. escolha a opção de geração desejada, como **Generate Constructor using Fields...**, **Generate Getters and Setters...** ou **Generate toString()...**;
5. selecione os campos e revise as opções;
6. confirme e leia o código produzido.

Atalhos e textos do menu podem variar entre versões e sistemas. O ponto didático é revisar o resultado, não memorizar a posição exata de um botão.

## Código gerado ainda exige decisão

Não selecione automaticamente setters para todos os campos. Antes de aceitar o resultado, pergunte:

- este campo pode realmente mudar depois da criação?
- qualquer valor é válido?
- existe uma operação melhor, como `deposit` ou `addProducts`?
- o método deve ser público ou apenas interno?

A IDE remove trabalho repetitivo; ela não conhece as regras do problema.

## Referências

- [JLS 25 - Access Control](https://docs.oracle.com/javase/specs/jls/se25/html/jls-6.html#jls-6.6).
- [JLS 25 - Top Level Type Declarations](https://docs.oracle.com/javase/specs/jls/se25/html/jls-7.html#jls-7.6).

---

<div align="center">

⬅️ [A5 · Encapsulamento, getters e setters](./A5%20-%20Encapsulamento%20getters%20e%20setters.md) &nbsp;·&nbsp; 📂 [Seção 8](./README.md) &nbsp;·&nbsp; [A7 · Prática integrada: conta bancária](./A7%20-%20Pratica%20integrada%20conta%20bancaria.md) ➡️

</div>
