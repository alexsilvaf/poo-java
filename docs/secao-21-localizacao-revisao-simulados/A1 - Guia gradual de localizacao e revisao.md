# Guia gradual de localização e revisão

## 1. `Locale`

```java
Locale brazil = Locale.forLanguageTag("pt-BR");
Locale canadaFrench = Locale.CANADA_FRENCH;
Locale custom = new Locale.Builder()
        .setLanguage("pt")
        .setRegion("BR")
        .build();
```

Idioma usa minúsculas em tags; região costuma usar maiúsculas. Um `Locale` identifica preferências culturais, não traduz conteúdo sozinho.

`Locale.setDefault` altera o padrão global; sobrecargas com `Locale` explícito são mais previsíveis.

## 2. Números, moeda e porcentagem

```java
NumberFormat number = NumberFormat.getNumberInstance(brazil);
NumberFormat currency = NumberFormat.getCurrencyInstance(brazil);
NumberFormat percent = NumberFormat.getPercentInstance(brazil);

System.out.println(number.format(1234.5));
System.out.println(currency.format(1234.5));
System.out.println(percent.format(0.25));
```

`parse` pode aceitar prefixo válido e ignorar o restante; use `ParsePosition` ou confira a posição quando precisar validar a entrada inteira. O tipo concreto devolvido por `parse` é `Number`.

## 3. Datas localizadas

```java
DateTimeFormatter formatter = DateTimeFormatter
        .ofLocalizedDate(FormatStyle.LONG)
        .withLocale(brazil);

String text = LocalDate.of(2026, 9, 19).format(formatter);
```

Não misture símbolos de padrões legados com `DateTimeFormatter` sem verificar seus significados. Formatação e parsing dependem do tipo temporal conter os campos exigidos.

## 4. Resource bundles

Arquivos:

```text
messages.properties
messages_pt.properties
messages_pt_BR.properties
```

Uso:

```java
ResourceBundle bundle = ResourceBundle.getBundle("messages", brazil);
String title = bundle.getString("title");
```

A busca considera locale solicitado, locale padrão e bundle raiz conforme as regras de candidatos e fallback. Um bundle mais específico pode herdar chaves de um menos específico.

Bundles podem ser `.properties` ou classes. Propriedades repetidas usam a última definição lida. Ausência completa de bundle gera `MissingResourceException`; ausência de chave gera a mesma família de erro.

## 5. `MessageFormat`

```java
String pattern = "Em {0,date,long}, o total foi {1,number,currency}.";
MessageFormat format = new MessageFormat(pattern, brazil);
String message = format.format(new Object[] {new Date(), 1234.5});
```

Apóstrofos têm significado de escape em padrões. `MessageFormat` usa índices de argumentos e formatos dependentes do locale.

## 6. Estratégia para leitura de código

Em qualquer questão:

1. identifique a versão e se há preview explicitamente habilitado;
2. verifique imports, packages, módulos e acesso;
3. confira declarações, tipos e inicialização;
4. confirme se compila;
5. só então execute mentalmente;
6. acompanhe mutabilidade, aliasing e efeitos colaterais;
7. observe exceções, fechamento de recursos e concorrência;
8. confira ordem, locale e contratos das APIs.

## 7. Mapa de revisão

| Domínio | Seções principais |
| --- | --- |
| tipos, texto, datas e booleanos | 3, 4, 6, 14 e 21 |
| controle de fluxo | 4, 5, 9 e 13 |
| orientação a objetos | 7, 8, 10, 11 e 13 |
| exceções | 12 |
| arrays, collections e generics | 9 e 15 |
| lambdas e streams | 16 e 17 |
| módulos e deployment | 19 |
| concorrência | 20 |
| I/O | 18 |
| localização | 21 |

## 8. Recursos Java 25

Permanentes no Java 25 e relevantes ao curso:

- flexible constructor bodies;
- module import declarations;
- compact source files e instance `main`;
- scoped values.

Também fazem parte da plataforma moderna coberta: Gatherers e variáveis/padrões sem nome. Primitive types in patterns e Structured Concurrency continuam preview no Java 25 e estão identificados como tal.

## Referências

- [API Java 25 — Locale](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Locale.html)
- [API Java 25 — ResourceBundle](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/ResourceBundle.html)
- [Java 25 Internationalization Guide](https://docs.oracle.com/en/java/javase/25/intl/)
