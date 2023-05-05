package exercicios.resolvidos;

import java.util.Scanner;

public class salario_reajuste {

    public static void main(String[] args) {

        Scanner ler = new Scanner(System.in);

        double salario, porcentagem;

        System.out.println("Informe o seu Salario: ");
        salario = ler.nextDouble();

        System.out.println("Informe a porcentagem do reajuste: ");
        porcentagem = ler.nextDouble();

        double reajuste = calculo(salario, porcentagem);
        imprimir(reajuste);

    }

    static double calculo(double salario, double porcentagem) {
        double reajuste = salario + salario * (porcentagem / 100);
        return reajuste;
    }

    static void imprimir(double reajuste) {
        System.out.println(String.format("O seu novo salário é: R$ %.2f", reajuste));
    }

}
