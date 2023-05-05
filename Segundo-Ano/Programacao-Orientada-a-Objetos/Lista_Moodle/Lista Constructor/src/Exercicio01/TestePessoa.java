package Exercicio01;

import java.time.LocalDate;
import java.time.ZoneId;
import java.util.Date;
import java.util.Scanner;

public class TestePessoa {
    public static void main(String[] args) {

        Scanner ler = new Scanner(System.in);
        Pessoa[] pessoa = new Pessoa[50];
        Date dt = new Date();

        for (int i = 0; i < pessoa.length; i++) {
            System.out.printf("Informe a data de nascimento da %dº Pessoa. \n", i + 1);
            System.out.println("Dia: ");
            int diaNascimento = ler.nextInt();

            System.out.println("Mês: ");
            int mesNascimento = ler.nextInt();

            System.out.println("Ano: ");
            int anoNascimento = ler.nextInt();

            LocalDate localDate = dt.toInstant()
                    .atZone(ZoneId.systemDefault())
                    .toLocalDate();
            int ano = localDate.getYear();

            while (diaNascimento < 1 || diaNascimento > 31 || mesNascimento < 1 || mesNascimento > 12
                    || anoNascimento < 1900 || anoNascimento > ano) {
                System.out.printf("Informação Incorreta, Por favor, informe um novo valor para..\n");
                if (diaNascimento < 1 || diaNascimento > 31) {
                    System.out.println("Dia: ");
                    diaNascimento = ler.nextInt();

                } else if (mesNascimento < 1 || mesNascimento > 12) {
                    System.out.println("Mês: ");
                    mesNascimento = ler.nextInt();

                } else if (anoNascimento < 1900 || anoNascimento > 2023) {
                    System.out.println("Ano: ");
                    anoNascimento = ler.nextInt();
                }
            }
            pessoa[i] = new Pessoa(diaNascimento, mesNascimento, anoNascimento); //Criando Objeto pessoa.
        }

        for (int i = 0; i < pessoa.length; i++) {
            System.out.printf("Data Nascimento é idade para a %dº Pessoa\n", i + 1);
            System.out.printf("Dia: %d\nMês: %d\nAno: %d\nIdade: %d\n", pessoa[i].diaNascimento,
                    pessoa[i].mesNascimento, pessoa[i].anoNascimento, pessoa[i].idade);
        }
    }
}
