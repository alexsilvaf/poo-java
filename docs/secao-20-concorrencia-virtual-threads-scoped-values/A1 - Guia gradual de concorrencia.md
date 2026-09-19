# Guia gradual de concorrência

## 1. Tarefas e threads

```java
Runnable task = () -> System.out.println(Thread.currentThread());
Thread thread = new Thread(task);
thread.start();
```

`start()` agenda outra thread; chamar `run()` diretamente executa na thread atual. Estados incluem `NEW`, `RUNNABLE`, `BLOCKED`, `WAITING`, `TIMED_WAITING` e `TERMINATED`.

`Callable<V>` devolve valor e pode lançar checked exception.

## 2. Executores

```java
ExecutorService service = Executors.newFixedThreadPool(2);
try {
    Future<Integer> future = service.submit(() -> 40 + 2);
    System.out.println(future.get());
} finally {
    service.shutdown();
}
```

`execute` recebe `Runnable`; `submit` devolve `Future`. Conheça `invokeAll`, `invokeAny`, cancelamento, timeouts e desligamento.

## 3. Virtual threads

```java
Thread.ofVirtual().start(task);

try (ExecutorService executor = Executors.newVirtualThreadPerTaskExecutor()) {
    Future<String> result = executor.submit(() -> "done");
}
```

Virtual threads são adequadas para muitas tarefas bloqueantes e independentes. Não tornam código CPU-bound mais rápido por si só e não eliminam a necessidade de proteger estado compartilhado.

No Java 25, sincronização foi aprimorada para evitar pinning comum de virtual threads em blocos `synchronized`, mas contenção e seções críticas longas continuam problemas de projeto.

## 4. Race condition e atomicidade

```java
count++; // leitura, soma e escrita: não é operação atômica composta
```

Alternativas conforme a necessidade:

```java
synchronized (lock) { count++; }
AtomicInteger count = new AtomicInteger();
count.incrementAndGet();
```

`volatile` fornece visibilidade e ordem para leituras/escritas da variável, mas não torna `count++` atômico.

## 5. Locks

```java
Lock lock = new ReentrantLock();
lock.lock();
try {
    update();
} finally {
    lock.unlock();
}
```

`tryLock`, timeouts e múltiplas `Condition` oferecem controle adicional. Sempre libere em `finally` após aquisição bem-sucedida.

## 6. Problemas clássicos

- deadlock: tarefas esperam recursos umas das outras;
- starvation: uma tarefa não obtém oportunidade suficiente;
- livelock: tarefas continuam reagindo sem progredir;
- race condition: resultado depende de interleaving não controlado.

Uma ordem global de aquisição ajuda a evitar deadlock.

## 7. Coleções concorrentes e paralelismo

`ConcurrentHashMap`, `CopyOnWriteArrayList`, `ConcurrentLinkedQueue` e blocking queues oferecem garantias específicas. Iterar uma coleção comum enquanto outra thread a modifica não é seguro.

Em streams paralelas, reduções devem ser associativas e livres de mutação compartilhada. `findAny` pode aproveitar melhor o paralelismo; ordem de encontro ainda influencia várias operações.

## 8. Scoped values

Scoped Values são permanentes no Java 25 e permitem compartilhar dados imutáveis com chamadas dentro de um escopo:

```java
static final ScopedValue<String> USER = ScopedValue.newInstance();

ScopedValue.where(USER, "ana").run(() -> {
    System.out.println(USER.get());
});
```

O binding é limitado dinamicamente ao escopo, não é uma variável global mutável e pode ser herdado de forma controlada por tarefas estruturadas. Fora do binding, `get()` falha; use `isBound()` ou `orElse` quando apropriado.

Structured Concurrency ainda é preview no Java 25. Não a trate como API permanente nem como sinônimo de scoped values.

## Revisão OCPJ25

Determine a thread que executa, visibilidade e atomicidade, ordem de locks, tipo de executor, bloqueio de `Future`, segurança da coleção e associatividade de reduções paralelas.

## Referências

- [API Java 25 — java.util.concurrent](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/package-summary.html)
- [API Java 25 — ScopedValue](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/lang/ScopedValue.html)
- [Java 25 — Scoped Values](https://openjdk.org/jeps/506)
