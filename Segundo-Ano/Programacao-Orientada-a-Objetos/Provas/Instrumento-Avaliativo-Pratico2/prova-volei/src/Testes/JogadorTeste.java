package Testes;

import java.util.Scanner;

import Principal.Jogadores;
import Principal.Levantador;
import Principal.Ponteiro;

public class JogadorTeste {
    public static void main(String[] args) {
        // Classe para ler os atributos
        Scanner ler = new Scanner(System.in);

        // Declaração das Variaveis.
        int cont_jogador = 0, opc = 0, qtde_cadastro = 0;

        System.out.println("Quantos Jogadores serão cadastrados? ");
        qtde_cadastro = ler.nextInt();

        // array de objeto
        Jogadores[] jogadores = new Jogadores[qtde_cadastro];

        while (opc != 3) {
            System.out.println("1 - Cadastrar Jogador \n2 - Listar Jogadores \n3 - Sair");
            System.out.println("opção: ");
            opc = ler.nextInt();
            System.out.println(" ");

            while (opc < 1 || opc > 3) {
                System.out.println("Opção invalida, Por favor, escolha uma opção valida.");
                System.out.println("1 - Cadastrar Jogador \n2 - Listar Jogadores \n3 - Sair");
                System.out.println("opção: ");
                opc = ler.nextInt();
                System.out.println(" ");
            }

            if (opc == 1) {
                int opc_tipo = 0;
                while (opc_tipo != 3) {
                    System.out.println("1 - Cadastrar Ponteiro \n2 - Cadastrar Levantador \n3 - Sair");
                    System.out.println("opção: ");
                    opc_tipo = ler.nextInt();
                    System.out.println(" ");
                    if (opc_tipo == 1) {
                        System.out.printf("Nome:");
                        String nome = ler.next();
                        ler.nextLine(); // Criado para ler os demais valores informados.
                        System.out.println("Idade:");
                        int idade = ler.nextInt();
                        System.out.println("Altura:");
                        double altura = ler.nextDouble();
                        jogadores[cont_jogador] = new Ponteiro(nome, idade, altura);
                        cont_jogador++;
                    } else if (opc_tipo == 2) {
                        System.out.println("Nome:");
                        String nome = ler.next();
                        ler.nextLine(); // Criado para ler os demais valores informados.
                        System.out.println("Idade:");
                        int idade = ler.nextInt();
                        System.out.println("Experiencia:");
                        int experiencia = ler.nextInt();
                        jogadores[cont_jogador] = new Levantador(nome, idade, experiencia);
                        cont_jogador++;
                    } else if (opc_tipo == 3) {
                        System.out.println("Voltando..");
                    } else {
                        System.out.println("Opção invalida, Por favor, escolha uma opção valida.");
                    }
                }
            } else if (opc == 2) {
                for (int i = 0; i < cont_jogador; i++) {
                    System.out.println("Jogador: " + (i + 1));
                    jogadores[i].imprimirJogador();
                }

            } else if (opc == 3) {
                System.out.println("Saindo...");
                break;

            } else {
                System.out.println("Opção invalida, Por favor, escolha uma opção valida.");
            }
        }
        ;
    }
}
