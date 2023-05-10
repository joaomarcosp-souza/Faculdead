package ClassesTeste;

import java.time.LocalDateTime;
import java.util.Scanner;

import ClassesInformacoes.Pessoa;


public class TestePessoa {
    public static void main(String[] args) {

        Scanner ler = new Scanner(System.in);

        int cont_pessoa = 0, qtde_pessoa = 0;

        System.out.println("Quantas pessoas farão a reserva?");
        qtde_pessoa = ler.nextInt();

        Pessoa[] pessoa = new Pessoa[qtde_pessoa];
        

        while (cont_pessoa != qtde_pessoa) {
            System.out.println("Informe o nome: ");
            String nome = ler.next();
            ler.nextLine();

            System.out.println("Informe o E-mail: ");
            String email = ler.nextLine();

            System.out.println("Informe o Telefone: ");
            String telefone = ler.nextLine();

            System.out.println("Informe o Senha: ");
            String senha = ler.nextLine();

            LocalDateTime dataAtuzalizacao = LocalDateTime.now();
            LocalDateTime dataCriacao = LocalDateTime.now();

            pessoa[cont_pessoa] = new Pessoa(nome, email, telefone, senha, false, dataAtuzalizacao, dataCriacao, null);
            cont_pessoa++;

            System.out.println("Salvo");
        }

        for (int i = 0; i < cont_pessoa; i++) {
            System.out.println("info: " + (i + 1));
            pessoa[i].imprimirDados();
        }
    }
}
