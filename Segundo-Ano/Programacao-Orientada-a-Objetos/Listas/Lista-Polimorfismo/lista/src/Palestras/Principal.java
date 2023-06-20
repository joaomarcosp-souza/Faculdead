package Palestras;

import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        Certificado certificado = new Certificado(150, 12, 5, 2536);
        Palestra palestra = new Palestra("Teste", "2024-03-12", true);
        Palestrante palestrante = new Palestrante("Joao", null, null, null, null, null, null);
        
    }
}
