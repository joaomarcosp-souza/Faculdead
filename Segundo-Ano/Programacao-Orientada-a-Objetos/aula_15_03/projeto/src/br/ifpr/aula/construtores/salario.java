package br.ifpr.aula.construtores;

import java.util.Scanner;

public class salario {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        double salario, aumento;

        System.out.println("Digite o seu salario: ");
        salario = ler.nextDouble();

        System.out.println("Informe o seu porcentagem de reajuste: ");
        aumento = ler.nextDouble();

        double reajuste = calculo(salario, aumento);
        imprimir(reajuste);

    }

    static double calculo(double salario, double aumento) {
        double reajuste = salario + salario * (aumento / 100);
        return reajuste;
    }

    static void imprimir(double reajuste) {
        System.out.printf("Seu reajuste é de: %.2f", reajuste);
    }
}
