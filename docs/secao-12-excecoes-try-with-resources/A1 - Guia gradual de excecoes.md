# Guia gradual de exceções

## 1. Hierarquia

`Throwable` possui dois grandes ramos:

- `Error`: problemas graves que normalmente não são tratados pela aplicação;
- `Exception`: condições que o programa pode tratar.

Dentro de `Exception`, `RuntimeException` e suas subclasses são unchecked. Outras subclasses são checked e precisam ser capturadas ou declaradas.

```java
void read() throws java.io.IOException {
    throw new java.io.IOException("failed");
}
```

## 2. `throw` e `throws`

- `throw` lança um objeto;
- `throws` declara possíveis tipos na assinatura.

```java
static void validate(int age) {
    if (age < 0) throw new IllegalArgumentException("negative age");
}
```

## 3. `try`, `catch` e `finally`

```java
try {
    riskyOperation();
} catch (IllegalArgumentException e) {
    System.out.println(e.getMessage());
} finally {
    System.out.println("always attempted");
}
```

`finally` executa após conclusão normal ou abrupta do `try`/`catch`, salvo situações como encerramento forçado da JVM. Um `return` em `finally` pode esconder retorno ou exceção anterior e deve ser evitado.

Capturas mais específicas vêm antes das mais gerais. Caso contrário, o `catch` posterior fica inalcançável.

## 4. Multi-catch

```java
try {
    process();
} catch (java.io.IOException | java.sql.SQLException e) {
    System.out.println(e.getMessage());
}
```

Os tipos não podem ter relação de subclasse entre si. A variável do multi-catch é efetivamente `final`.

## 5. Exceção personalizada

```java
class InvalidBalanceException extends Exception {
    InvalidBalanceException(String message) {
        super(message);
    }
}
```

Estender `Exception` cria checked exception; estender `RuntimeException` cria unchecked.

## 6. Sobrescrita

Um método sobrescrito não pode adicionar checked exception mais ampla do que a declaração ancestral. Pode declarar subtipo mais específico ou nenhuma. Restrições equivalentes não se aplicam a unchecked exceptions.

## 7. Try-with-resources

```java
try (var reader = java.nio.file.Files.newBufferedReader(path)) {
    System.out.println(reader.readLine());
}
```

O recurso deve implementar `AutoCloseable`. Recursos são fechados na ordem inversa à declaração:

```java
try (Resource first = new Resource("first");
     Resource second = new Resource("second")) {
    // second fecha antes de first
}
```

Uma variável local final ou efetivamente final também pode ser usada:

```java
var reader = Files.newBufferedReader(path);
try (reader) { /* ... */ }
```

## 8. Exceções suprimidas

Se o corpo lança uma exceção e `close()` lança outra, a do corpo é a principal e a do fechamento fica suprimida. Consulte `getSuppressed()`. Se não havia falha no corpo, a falha de `close()` é propagada normalmente.

## Revisão OCPJ25

Ao ler uma questão:

1. verifique se compila pelas regras de checked exceptions;
2. determine qual bloco lança primeiro;
3. escolha o primeiro `catch` compatível;
4. execute `finally` e fechamentos na ordem correta;
5. diferencie exceção principal de suprimida.

## Referências

- [JLS 25 — Exceptions](https://docs.oracle.com/javase/specs/jls/se25/html/jls-11.html)
- [JLS 25 — Try Statement](https://docs.oracle.com/javase/specs/jls/se25/html/jls-14.html#jls-14.20)
- [API Java 25 — AutoCloseable](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/AutoCloseable.html)
