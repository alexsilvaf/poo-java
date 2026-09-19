# Prática integrada: conta bancária

<sub>📚 [Documentação](../README.md) › [Seção 8 · Construtores, palavra this, sobrecarga e encapsulamento](./README.md) › Material 7 de 8</sub>

O projeto reúne construtores, `this`, sobrecarga, encapsulamento, getters e métodos que preservam regras simples.

## Requisitos

Uma conta possui:

- número, definido na criação e sem setter;
- titular, que pode ser alterado;
- saldo, consultável mas sem setter;
- depósito opcional na abertura;
- operações de depósito e saque;
- taxa fixa de `5.00` em cada saque.

## Classe `BankAccount`

```java
public class BankAccount {
    private static final double WITHDRAW_FEE = 5.00;

    private final int number;
    private String holder;
    private double balance;

    public BankAccount(int number, String holder) {
        this(number, holder, 0.0);
    }

    public BankAccount(int number, String holder, double initialDeposit) {
        this.number = number;
        this.holder = holder;
        deposit(initialDeposit);
    }

    public int getNumber() {
        return number;
    }

    public String getHolder() {
        return holder;
    }

    public void setHolder(String holder) {
        if (holder != null && !holder.isBlank()) {
            this.holder = holder;
        }
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0.0) {
            balance += amount;
        }
    }

    public void withdraw(double amount) {
        if (amount > 0.0) {
            balance -= amount + WITHDRAW_FEE;
        }
    }

    @Override
    public String toString() {
        return "Account "
                + number
                + ", Holder: "
                + holder
                + ", Balance: $ "
                + String.format("%.2f", balance);
    }
}
```

## Decisões de projeto

### Número `final`

```java
private final int number;
```

O campo recebe valor uma vez durante a construção e não pode ser reatribuído. Não há setter porque o número identifica a conta.

### Saldo sem setter

O saldo muda por `deposit` e `withdraw`, não por uma substituição arbitrária. O getter permite consulta, mas não entrega permissão de alteração.

### Taxa da classe

```java
private static final double WITHDRAW_FEE = 5.00;
```

A taxa é compartilhada, constante e usada apenas internamente.

### Construtores encadeados

O construtor sem depósito delega ao mais completo:

```java
this(number, holder, 0.0);
```

Assim, a lógica de inicialização principal fica em um único lugar.

## Programa principal

```java
import java.util.Locale;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter account number: ");
        int number = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter account holder: ");
        String holder = sc.nextLine();

        System.out.print("Is there an initial deposit (y/n)? ");
        char answer = sc.next().charAt(0);

        BankAccount account;
        if (answer == 'y' || answer == 'Y') {
            System.out.print("Enter initial deposit value: ");
            double initialDeposit = sc.nextDouble();
            account = new BankAccount(number, holder, initialDeposit);
        } else {
            account = new BankAccount(number, holder);
        }

        System.out.println("Account data:");
        System.out.println(account);

        System.out.print("Enter a deposit value: ");
        account.deposit(sc.nextDouble());
        System.out.println("Updated account data:");
        System.out.println(account);

        System.out.print("Enter a withdraw value: ");
        account.withdraw(sc.nextDouble());
        System.out.println("Updated account data:");
        System.out.println(account);

        sc.close();
    }
}
```

## Limite intencional

Esta versão permite que o saque deixe o saldo negativo, conforme a regra proposta. Não use uma coleção de contas, exceções ou persistência ainda; esses recursos serão adicionados quando seus pré-requisitos forem apresentados.

## Desafios compatíveis com a seção

1. Acrescente um método privado que normalize o nome do titular com `strip()`.
2. Impedir depósito de valor não positivo já está implementado; explique por que o construtor reutiliza esse método.
3. Preveja o saldo depois de depósito de `200.00` e saque de `50.00` em uma conta que começou zerada.

---

<div align="center">

⬅️ [A6 · Modificadores de acesso e geração pelo Eclipse](./A6%20-%20Modificadores%20de%20acesso%20e%20geracao%20pelo%20Eclipse.md) &nbsp;·&nbsp; 📂 [Seção 8](./README.md) &nbsp;·&nbsp; [A8 · A certificação OCP Java SE 25 e esta seção](./A8%20-%20A%20certificacao%20OCP%20Java%20SE%2025.md) ➡️

</div>
