import java.util.Scanner;

public class Aula1 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer resposta = null;
        System.out.print("Insira o ano: ");
        resposta = sc.nextInt();
        
        if (resposta % 4 == 0) {
            System.out.println("É bissexto!");
        } else {
            System.out.println("Não é bissexto!");
        }
    }
}