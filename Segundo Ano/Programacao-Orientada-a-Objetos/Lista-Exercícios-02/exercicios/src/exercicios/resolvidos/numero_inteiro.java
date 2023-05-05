package exercicios.resolvidos;

import java.util.Scanner;

public class numero_inteiro {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        int num;
        int soma = 0;

        System.out.println("Informe o número a ser somado: ");
        num = ler.nextInt();

        soma = calcula(num, soma);
        imprimir(num, soma);
    }

    static int calcula(int num, int soma) {
        for (int i = 0; i <= num; i++) {
            soma += i;
        }
        return soma;
    }

    static void imprimir(int num, int soma) {
        System.out.println(String.format("Soma dos números de 0 a %d é %d", num, soma));
    }
}