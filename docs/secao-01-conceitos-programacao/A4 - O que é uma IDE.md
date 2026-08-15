# IDE - Ambiente Integrado de Desenvolvimento
É um conjunto de softwares utilizado para a construção de programas

## Exemplos:
C/C++: Code Blocks
Java: Eclipse, NetBeans
C#: Microsoft Visual Studio

### Exemplo de um programa:
Suponha um programa que solicita do usuário dois números e depois mostra a média aritmética deles:
```
Digite o primeiro numero: 3
Digite o segundo numero: 6

Media = 4.5
```

### Solução em linguagem C

```c
#include <stdio.h>

int main() {
    double x, y, media;

    printf("Digite o primeiro numero: ");
    scanf("%lf", &x);
    printf("Digite o segundo numero: ");
    scanf("%lf", &y);
    media = (x + y) / 2.0;
    printf("Media = %.1f\n", media);

    return 0;
}
```

### Solução em linguagem C++

```cpp
#include <iostream>

using namespace std;

int main() {
    double x, y, media;

    cout << "Digite o primeiro numero: ";
    cin >> x;
    cout << "Digite o segundo numero: ";
    cin >> y;
    media = (x + y) / 2.0;
    cout << "Media = " << media << endl;

    return 0;
}
```

### Solução em linguagem C#

```csharp
using System;

namespace programa {
    class Program {
        static void Main(string[] args) {
            double x, y, media;

            Console.Write("Digite o primeiro numero: ");
            x = double.Parse(Console.ReadLine());
            Console.Write("Digite o segundo numero: ");
            y = double.Parse(Console.ReadLine());
            media = (x + y) / 2.0;
            Console.WriteLine("Media = " + media);
        }
    }
}
```

### Solução em linguagem Java

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double x, y, media;

        System.out.print("Digite o primeiro numero: ");
        x = sc.nextDouble();
        System.out.print("Digite o segundo numero: ");
        y = sc.nextDouble();
        media = (x + y) / 2.0;
        System.out.println("Media = " + media);

        sc.close();
    }
}
```
