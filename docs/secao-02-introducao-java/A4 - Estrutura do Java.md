# Estrutura de uma aplicação Java

<sub>📚 [Documentação](../README.md) › [Seção 2 · Introdução à linguagem Java](./README.md) › Material 4 de 8</sub>

Java é uma linguagem orientada a objetos. A organização do código segue uma hierarquia de agrupamentos, do menor para o maior:

**classe → pacote → módulo → aplicação**

## Classes

Classe é uma unidade usada para organizar código Java. A orientação a objetos e o conteúdo interno das classes serão estudados a partir da Seção 7; por enquanto, basta reconhecer a declaração e sua relação com o arquivo.

![Classes](./classes.svg)

```java
public class Produto {
    // O conteúdo será estudado gradualmente.
}
```

### Regras entre classe e arquivo-fonte

Um arquivo `.java` pode conter mais de uma classe, mas precisa respeitar estas regras:

- Um arquivo-fonte pode ter **no máximo uma classe `public`**.
- Se existe uma classe `public`, o **nome do arquivo deve ser idêntico ao nome dessa classe**, respeitando maiúsculas e minúsculas, mais a extensão `.java`.
- Se nenhuma classe do arquivo for `public`, o arquivo pode ter qualquer nome.

```java
// Arquivo: Produto.java
public class Produto {   // pública, dá nome ao arquivo
    // ...
}

class Categoria {        // sem modificador, permitida no mesmo arquivo
    // ...
}
```

> [!IMPORTANT]
> Java diferencia maiúsculas de minúsculas. `Produto` e `produto` são nomes distintos.

## Pacotes

Pacote é um agrupamento lógico de classes relacionadas.

![Pacotes](./pacote.svg)

O pacote é declarado na **primeira instrução** do arquivo, antes de qualquer `import` e de qualquer classe. Por convenção usa-se o nome de domínio invertido, todo em minúsculas.

```java
package com.exemplo.produtos;   // 1. declaração de pacote

import java.util.Scanner;       // 2. importações, quando necessárias

public class Aplicacao {        // 3. declaração de tipo
    // O Scanner será usado na Seção 3.
}
```

Pontos importantes sobre pacotes:

- A estrutura de diretórios no disco precisa espelhar o nome do pacote: `com/exemplo/produtos/Inventario.java`.
- Tipos do pacote `java.lang`, como `String` e `System`, ficam disponíveis automaticamente.
- Classes do **mesmo pacote** não precisam de `import`.
- Sem `import`, o tipo precisa ser escrito com o nome completo, como `java.util.Scanner`.
- `import java.util.*;` importa todos os tipos do pacote `java.util`, mas **não** os de seus subpacotes.

## Módulos

Módulos são agrupamentos lógicos de pacotes relacionados. Foram introduzidos na versão 9 do Java, pelo *Project Jigsaw*.

_Observação: Runtime é o agrupamento físico._

![Módulos](./modulo.svg)

Um módulo é declarado em um arquivo chamado `module-info.java`, colocado na raiz do código-fonte do módulo:

```java
module com.exemplo.produtos {
    requires java.sql;                  // do que este módulo depende
    exports com.exemplo.produtos.api;   // o que este módulo torna público
}
```

O que os módulos acrescentam em relação aos pacotes:

- **Encapsulamento forte:** um pacote só é visível de fora do módulo se for explicitamente exportado com `exports`. Pacotes internos ficam realmente inacessíveis.
- **Dependências explícitas:** `requires` declara de quais módulos este depende, e a falta de um deles é detectada logo na inicialização, e não no meio da execução.
- **Imagens menores:** como as dependências são conhecidas, o `jlink` consegue montar um runtime contendo apenas o necessário.

Todo módulo depende implicitamente do módulo `java.base`, que contém `java.lang`, `java.util`, `java.io` e os demais pacotes fundamentais. Por isso não é preciso escrever `requires java.base;`.

### Importação de módulos (Java 25)

A partir do Java 25 existe uma declaração capaz de importar os pacotes exportados por um módulo:

```java
import module java.base;
```

Nesta etapa, basta reconhecer a declaração. Os tipos que ela disponibiliza serão apresentados conforme aparecerem no curso; não é necessário estudar coleções ou arquivos agora.

## Aplicação

Agrupamento de módulos relacionados.

![Aplicação](./aplicacao.svg)

Na prática, uma aplicação é distribuída de uma destas formas:

- **Arquivo `.jar`:** um pacote compactado com as classes compiladas e seus recursos. Pode ser modular (contém `module-info.class`) ou não modular.
- **Imagem de runtime:** gerada pelo `jlink`, já inclui a JVM e apenas os módulos necessários. Não exige um Java instalado na máquina de destino.

```bash
javac -d bin com/exemplo/produtos/*.java   # compila
jar --create --file app.jar -C bin .       # empacota
java -jar app.jar                          # executa
```

---

<div align="center">

⬅️ [A3 · Versões do Java (desde a versão 8)](./A3%20-%20Versoes%20do%20Java.md) &nbsp;·&nbsp; 📂 [Seção 2](./README.md) &nbsp;·&nbsp; [A5 · Instalação do JDK e da IDE](./A5%20-%20Instalacao%20do%20JDK%20e%20da%20IDE.md) ➡️

</div>
