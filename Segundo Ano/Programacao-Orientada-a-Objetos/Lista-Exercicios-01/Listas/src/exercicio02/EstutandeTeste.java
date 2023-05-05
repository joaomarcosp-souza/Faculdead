package exercicio02;

import java.util.Scanner;

public class EstutandeTeste {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        Estudande[] estudantes = new Estudande[2]; // criação de uma array 

        //FOR para ler as notas do estudante
        for (int i = 0; i < 2; i++) {
            System.out.printf("Informe as duas notas do %dº Estudante: \n", i + 1);
            double notaUm = ler.nextDouble();
            double notaDois = ler.nextDouble();
            estudantes[i] = new Estudande(notaUm, notaDois); // criando um array de objetos para cada estudande
        }

        //lendo as notas e a media dos 2 Estudantes
        for (int i = 0; i < 2; i++) {
            System.out.printf("Estudante %d - Nota 1: %.2f | Nota 2: %.2f | Média: %.2f\n", i + 1,
                    estudantes[i].notaUm, estudantes[i].notaDois, estudantes[i].media);
        }

    }
}
