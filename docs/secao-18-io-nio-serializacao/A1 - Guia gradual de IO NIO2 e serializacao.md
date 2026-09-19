# Guia gradual de I/O, NIO.2 e serialização

## 1. Bytes e caracteres

- `InputStream`/`OutputStream`: bytes;
- `Reader`/`Writer`: caracteres;
- classes com `Buffered` reduzem acessos ao dispositivo e oferecem operações convenientes.

```java
try (var reader = new BufferedReader(new FileReader("input.txt"));
     var writer = new BufferedWriter(new FileWriter("output.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        writer.write(line.toUpperCase());
        writer.newLine();
    }
}
```

Charsets importam na conversão entre bytes e texto. Prefira sobrecargas que recebem `Charset` quando o formato do arquivo é conhecido.

## 2. `Path`

```java
Path path = Path.of("data", "report.txt");
Path absolute = path.toAbsolutePath();
Path normalized = Path.of("a", "..", "b").normalize();
```

`normalize` é lexical; `toRealPath` consulta o sistema de arquivos e resolve links conforme opções. `resolve`, `relativize`, `getName`, `getParent`, `getRoot`, `subpath` e `startsWith` aparecem com frequência.

## 3. `Files`

```java
Files.createDirectories(Path.of("data"));
Files.writeString(path, "Java 25");
String text = Files.readString(path);
Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
Files.move(source, target);
Files.deleteIfExists(target);
```

Métodos podem lançar `IOException`. A operação pode não ser atômica; use opções quando a API e o sistema suportarem.

## 4. Streams lazy de arquivos

```java
try (Stream<String> lines = Files.lines(path)) {
    long count = lines.filter(s -> !s.isBlank()).count();
}

try (Stream<Path> paths = Files.walk(directory)) {
    paths.filter(Files::isRegularFile).forEach(System.out::println);
}
```

O stream mantém recurso aberto e precisa ser fechado.

## 5. Diretórios e atributos

`Files.list` percorre um nível; `Files.walk` percorre recursivamente; `Files.find` filtra com caminho e atributos. `BasicFileAttributes` fornece tamanho, datas e tipo. `Files.isSameFile` consulta se dois caminhos localizam o mesmo arquivo.

## 6. Console e streams padrão

`System.in`, `System.out` e `System.err` são streams padrão. `System.console()` pode devolver `null`, especialmente em IDEs. Java 25 também oferece a classe `java.lang.IO` para programas compactos; conheça `print`, `println` e `readln`, sem confundi-la com `java.io`.

## 7. Serialização

```java
class Customer implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private transient String password;
    private static int count;
}
```

`transient` não é serializado. Campos `static` pertencem à classe, não ao objeto. Todos os objetos alcançáveis por campos não transient também precisam ser serializáveis, ou ocorrerá `NotSerializableException`.

```java
try (var out = new ObjectOutputStream(Files.newOutputStream(path))) {
    out.writeObject(customer);
}
```

Na desserialização de uma classe serializável, seus construtores e inicializadores não são executados como em `new`; o construtor sem argumentos da primeira superclasse não serializável participa.

## 8. Cópias rasas e segurança

Serialização preserva grafos e referências compartilhadas dentro do stream, não é uma estratégia segura para dados não confiáveis. Para formatos de interoperabilidade, prefira formatos explícitos e validação.

## Revisão OCPJ25

Cheque classe base (`InputStream` ou `Reader`), ordem de wrappers, fechamento, tipo de retorno de `Files`, lazy streams, opções de cópia e campos incluídos na serialização.

## Referências

- [API Java 25 — java.io](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/io/package-summary.html)
- [API Java 25 — java.nio.file](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/nio/file/package-summary.html)
- [Java Object Serialization Specification](https://docs.oracle.com/en/java/javase/25/docs/specs/serialization/)
