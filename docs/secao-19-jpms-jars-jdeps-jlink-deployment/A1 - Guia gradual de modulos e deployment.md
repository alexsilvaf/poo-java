# Guia gradual de módulos e deployment

## 1. Classpath e JAR

```text
javac -d out src/com/example/Main.java
jar --create --file app.jar --main-class com.example.Main -C out .
java -jar app.jar
```

Um JAR é um ZIP com classes e metadados. No classpath, classes ficam no módulo sem nome e a organização depende de packages.

## 2. Módulo nomeado

```java
module com.example.app {
    requires com.example.service;
    exports com.example.api;
}
```

- `requires`: dependência de leitura;
- `exports`: pacote acessível por código de outros módulos;
- `opens`: acesso reflexivo;
- `requires transitive`: consumidores também leem a dependência;
- `requires static`: exigida na compilação, opcional em execução.

Exportar não torna membros privados acessíveis. Acessibilidade exige regras da linguagem e do módulo.

## 3. Serviços

```java
module com.example.api {
    exports com.example.spi;
}

module com.example.provider {
    requires com.example.api;
    provides com.example.spi.PaymentService
        with com.example.provider.CardService;
}

module com.example.consumer {
    requires com.example.api;
    uses com.example.spi.PaymentService;
}
```

O consumidor usa `ServiceLoader.load(PaymentService.class)` e não depende diretamente do provedor.

## 4. Tipos de módulo e migração

- explícito/nomeado: possui `module-info.class`;
- automático: JAR comum no module path recebe nome derivado;
- sem nome: conteúdo no classpath.

Uma migração comum move dependências para o module path gradualmente, usa módulos automáticos como ponte e cria descritores explícitos depois.

## 5. Linha de comando modular

```text
javac --module-source-path src -d out -m com.example.app
java --module-path out -m com.example.app/com.example.Main
jar --create --file app.jar -C out/com.example.app .
```

Conheça também `jar --describe-module` e `java --show-module-resolution`.

## 6. `jdeps` e `jlink`

```text
jdeps --print-module-deps app.jar
jlink --module-path mods --add-modules com.example.app --output runtime
```

`jdeps` analisa dependências. `jlink` produz uma imagem de runtime com módulos selecionados. Ele trabalha com módulos nomeados; JARs automáticos não são uma base direta adequada para a imagem.

## 7. `import module` no Java 25

O recurso é permanente no Java 25:

```java
import module java.base;

class Demo {
    List<String> names = List.of("Ana", "Bia");
}
```

Ele importa tipos públicos dos pacotes exportados pelo módulo e por dependências transitivas legíveis. Não adiciona `requires` ao descritor e pode criar nomes ambíguos; um import mais específico pode resolver.

## 8. Compact source files e instance `main`

Também permanentes no Java 25:

```java
void main() {
    System.out.println("Hello, Java 25");
}
```

O arquivo compacto declara implicitamente uma classe. Um candidato `main` pode ser de instância, não receber argumentos e ter acesso público, protegido ou de pacote. A forma clássica continua válida.

Execução direta de fonte:

```text
java Hello.java
```

Programas multifonte podem ser lançados em modo fonte quando os arquivos relacionados estão disponíveis conforme as regras da ferramenta `java`.

## Revisão OCPJ25

Separe package, acesso, leitura do módulo e exportação. Depois confira classpath versus module path, nome da classe principal, diretivas de serviço e objetivo de cada ferramenta.

## Referências

- [Java 25 — Module Import Declarations](https://openjdk.org/jeps/511)
- [Java 25 — Compact Source Files and Instance Main Methods](https://openjdk.org/jeps/512)
- [Java 25 Tool Specifications](https://docs.oracle.com/en/java/javase/25/docs/specs/man/)
