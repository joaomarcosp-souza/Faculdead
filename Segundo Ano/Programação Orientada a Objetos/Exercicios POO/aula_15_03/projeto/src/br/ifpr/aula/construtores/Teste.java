package br.ifpr.aula.construtores;

import java.util.*;

import javax.print.attribute.standard.Media;

public class Teste {

    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        int a, b, c;

        System.out.println("Informe os tres valores respectivamente (A, B, C): ");
        a = ler.nextInt();
        b = ler.nextInt();
        c = ler.nextInt();

        double media = media(a, b, c);
        imprimir(media);

    }

    static double media(int a, int b, int c) {

        int soma = a + b + c;
        double media = soma / 3;
        return media;
    }

    static void imprimir(double media) {
        System.out.println("Sua media: " + media);
    }

}
