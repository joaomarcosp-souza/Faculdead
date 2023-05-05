package exercicios.resolvidos;

import java.util.Scanner;

public class exercicio06 {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        String nome;
        int diaNasc, mesNasc, anoNasc;

        System.out.println("Nome: ");
        nome = ler.nextLine();

        System.out.println("Informe a sua Data de Nascimento.");

        System.out.println("Dia: ");
        diaNasc = ler.nextInt();
        System.out.println("Mês: ");
        mesNasc = ler.nextInt();
        System.out.println("Ano: ");
        anoNasc = ler.nextInt();

        imprimi(diaNasc, mesNasc, anoNasc, nome);
    }

    static String NomeIdade(int diaNasc, int mesNasc, int anoNasc, String nome) {

        int idade = 2023;
        idade -= anoNasc;
        if (mesNasc > 3 || (mesNasc == 3 && diaNasc > 15)) {
            idade--;
        }
        return nome + ", sua idade é " + idade + " anos, ";
    }

    static void imprimi(int diaNasc, int mesNasc, int anoNasc, String nome) {
        String idade = NomeIdade(diaNasc, mesNasc, anoNasc, nome);
        String resultadoFinal = idade + " em 15/03/2023";
        System.out.println(resultadoFinal);
    }
}