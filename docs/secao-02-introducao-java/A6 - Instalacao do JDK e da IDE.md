# Instalação do JDK e da IDE

Para escrever e executar programas Java são necessários dois softwares: o **JDK**, que compila e executa, e uma **IDE**, que oferece editor, atalhos, depurador e automação de tarefas.

## Instalando o JDK

O curso usa o **JDK 25 (LTS)**. Qualquer distribuição serve; a mais simples de instalar sem exigências de licença é o **Eclipse Temurin**.

| Origem | Endereço |
|--------|----------|
| Eclipse Temurin (Adoptium) | <https://adoptium.net> |
| Oracle JDK | <https://www.oracle.com/java/technologies/downloads/> |

### Windows

1. Baixar o instalador `.msi` do JDK 25.
2. Executar o instalador e aceitar as opções padrão.
3. Marcar a opção que adiciona o Java ao `PATH` e que define a variável `JAVA_HOME`, quando o instalador oferecer.

### Linux

```bash
# Fedora
sudo dnf install java-25-openjdk-devel

# Debian / Ubuntu
sudo apt install openjdk-25-jdk
```

### Verificando a instalação

Abra um terminal novo e execute:

```bash
java -version    # mostra a versão do runtime
javac -version   # mostra a versão do compilador
```

As duas versões devem ser a mesma. Se `javac` não for encontrado mas `java` sim, provavelmente foi instalado apenas um runtime, e não o JDK completo.

### Variáveis de ambiente

- **`JAVA_HOME`** aponta para o diretório de instalação do JDK. Ferramentas como Maven, Gradle e o próprio Eclipse a utilizam.
- **`PATH`** precisa conter `%JAVA_HOME%\bin` (Windows) ou `$JAVA_HOME/bin` (Linux) para que `java` e `javac` funcionem de qualquer diretório.

```bash
# Linux, verificação
echo $JAVA_HOME
which java
```

> É comum ter mais de um JDK instalado na mesma máquina. Nesse caso, o que vale para a linha de comando é o que está primeiro no `PATH`, e o que vale para a IDE é o que estiver configurado dentro dela. Os dois podem ser diferentes, e essa é uma fonte frequente de confusão.

## Escolhendo a IDE

| IDE | Observações |
|-----|-------------|
| **Eclipse / Spring Tools (STS)** | Gratuita, usada como referência neste curso. O STS é o Eclipse já com ferramentas para Spring. |
| **IntelliJ IDEA Community** | Gratuita, muito usada no mercado. Assistência de código mais elaborada. |
| **VS Code + Extension Pack for Java** | Leve, exige instalar o pacote de extensões da Microsoft. |
| **NetBeans** | Gratuita, mantida pela Apache. |

Todas compilam com o mesmo `javac` do JDK instalado. A escolha é de conforto, não de capacidade.

## Instalando o Eclipse (Spring Tools — STS)

1. Baixar o STS em <https://spring.io/tools> ou o Eclipse IDE for Java Developers em <https://www.eclipse.org/downloads/>.
2. Descompactar em uma pasta sem espaços e sem acentos no caminho.
3. Executar o `SpringToolSuite4.exe` (ou `eclipse`).
4. Escolher a pasta de *workspace*, que é onde os projetos serão gravados. Também deve ficar em um caminho sem espaços e sem acentos.

## Configurando o JDK dentro do Eclipse

O Eclipse não usa automaticamente o JDK mais recente instalado. É preciso registrá-lo:

1. **Window → Preferences → Java → Installed JREs**
2. **Add… → Standard VM → Next**
3. Em *JRE home*, apontar para o diretório do JDK 25.
4. Confirmar e **marcar a caixa de seleção** do JDK 25 para torná-lo o padrão.

Em seguida, ajustar o nível de compilação:

1. **Window → Preferences → Java → Compiler**
2. Definir *Compiler compliance level* como **25**.

> Se o nível de compilação estiver abaixo de 25, recursos novos da linguagem, como os arquivos-fonte compactos, serão marcados como erro pelo editor mesmo com o JDK 25 instalado.

## Criando o primeiro projeto

1. **File → New → Java Project**
2. Informar o nome do projeto, sem espaços e sem acentos.
3. Confirmar que o *JRE* selecionado é o JDK 25.
4. Clicar com o botão direito em `src` → **New → Class**.
5. Informar o nome da classe em `PascalCase` e marcar a opção que gera o método `main`.

## Problemas frequentes

| Sintoma | Causa provável |
|---------|----------------|
| `javac` não é reconhecido no terminal | O `PATH` não inclui a pasta `bin` do JDK, ou o terminal foi aberto antes da instalação. |
| O Eclipse não abre e reclama de JVM | O Eclipse não encontrou um Java compatível. Instalar o JDK antes da IDE. |
| Recursos do Java 25 aparecem como erro | *Compiler compliance level* configurado em uma versão anterior. |
| `UnsupportedClassVersionError` ao executar | O código foi compilado por um JDK mais novo do que o runtime que está executando. |
