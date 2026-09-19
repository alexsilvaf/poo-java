# A certificação OCP Java SE 25 e esta seção

<sub>📚 [Documentação](../README.md) › [Seção 7 · Introdução à Programação Orientada a Objetos](./README.md) › Material 8 de 8</sub>

Esta seção apresenta parte do domínio de orientação a objetos da OCP Java SE 25. O objetivo não é esgotar o exame agora, mas construir a base que as próximas seções utilizarão.

## O que já deve estar claro

- classe é a definição de um tipo; objeto é uma instância;
- `new` cria uma instância e devolve uma referência;
- campos de instância recebem valores padrão;
- variáveis locais precisam ser inicializadas antes da leitura;
- atribuir uma referência não copia o objeto;
- mais de uma variável pode referenciar a mesma instância;
- `null` representa ausência de referência a um objeto;
- objetos inalcançáveis podem se tornar elegíveis para coleta;
- métodos de instância operam em relação a um objeto;
- membros `static` pertencem à classe;
- `toString()` fornece uma representação textual e pode ser sobrescrito.

## Questões de leitura de código

### 1. Campos e variáveis locais

```java
class Sample {
    int field;

    void print() {
        int local;
        System.out.println(field);
        // System.out.println(local);
    }
}
```

`field` possui valor padrão `0`. A linha comentada não compilaria porque `local` ainda não recebeu valor.

### 2. Duas referências

```java
class Box {
    int value;
}

Box a = new Box();
Box b = a;
a.value = 4;
b.value += 3;
System.out.println(a.value);
```

Saída: `7`. `a` e `b` alcançam o mesmo objeto.

### 3. Reatribuição

```java
Box a = new Box();
Box b = a;
a = new Box();
b.value = 5;
System.out.println(a.value + " " + b.value);
```

Saída: `0 5`. A nova atribuição mudou a referência guardada em `a`; não transformou o objeto de `b`.

### 4. Passagem por valor

```java
static void update(Box box) {
    box.value = 10;
    box = new Box();
    box.value = 20;
}

Box box = new Box();
update(box);
System.out.println(box.value);
```

Saída: `10`. O primeiro acesso altera o objeto compartilhado. Depois, apenas a cópia local da referência é redirecionada.

### 5. Acesso estático

```java
class Counter {
    static int total;
    int current;
}

Counter first = new Counter();
Counter second = new Counter();
first.current++;
Counter.total++;
second.current++;
Counter.total++;
```

Ao final, `first.current` e `second.current` valem `1`; `Counter.total` vale `2`.

### 6. Contexto estático

```java
class Test {
    int value = 3;

    static void show() {
        // System.out.println(value);
    }
}
```

A linha comentada não compila. Um contexto estático não possui instância atual da qual retirar `value`.

### 7. `null`

```java
Box box = null;
System.out.println(box == null);
```

Saída: `true`. Comparar a referência é válido; acessar `box.value` causaria `NullPointerException`.

### 8. Coleta de lixo

```java
Box first = new Box();
Box second = new Box();
first = second;
```

O primeiro objeto criado fica sem uma referência por esse trecho e torna-se elegível para coleta. Não é possível afirmar quando será coletado.

### 9. `toString`

```java
class Label {
    String text;

    @Override
    public String toString() {
        return "[" + text + "]";
    }
}
```

Se `text` vale `Java`, `System.out.println(label)` mostra `[Java]`.

### 10. `static final`

```java
class Measure {
    static final int LIMIT = 10;
}
```

`LIMIT` está associado à classe e não pode receber uma segunda atribuição após sua inicialização.

## Armadilhas frequentes

- confundir a variável de referência com o objeto;
- acreditar que `b = a` clona a instância;
- afirmar que um objeto será coletado imediatamente;
- usar o nome de uma referência para acessar um membro estático;
- tentar acessar um campo de instância diretamente no `main`;
- pensar que o texto padrão de `Object.toString()` é um endereço de memória.

## Conteúdo ainda não concluído

Para o domínio completo da certificação ainda faltam, entre outros assuntos:

- construtores, `this`, sobrecarga, inicializadores e controle de acesso, na Seção 8;
- igualdade lógica e contrato de `equals`/`hashCode`;
- herança, polimorfismo, classes abstratas e interfaces;
- enums, records, classes seladas e pattern matching;
- classes aninhadas e genéricos.

## Referências

- [JLS 25 - Classes](https://docs.oracle.com/javase/specs/jls/se25/html/jls-8.html).
- [JLS 25 - Run-Time Evaluation of Class Instance Creation](https://docs.oracle.com/javase/specs/jls/se25/html/jls-15.html#jls-15.9.4).
- [JVMS 25 - Run-Time Data Areas](https://docs.oracle.com/javase/specs/jvms/se25/html/jvms-2.html#jvms-2.5).

---

<div align="center">

⬅️ [A7 · Membros estáticos e membros de instância](./A7%20-%20Membros%20estaticos%20e%20membros%20de%20instancia.md) &nbsp;·&nbsp; 📂 [Seção 7](./README.md) &nbsp;·&nbsp; [Seção 8 · Construtores, palavra this, sobrecarga e encapsulamento](../secao-08-construtores-this-sobrecarga-encapsulamento/README.md) ➡️

</div>
