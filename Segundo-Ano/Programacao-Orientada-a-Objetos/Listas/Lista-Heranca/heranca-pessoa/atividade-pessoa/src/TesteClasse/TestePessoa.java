package TesteClasse;

import java.util.Scanner;

import javax.print.event.PrintEvent;

import Classes.Funcionario;
import Classes.Pessoa;

public class TestePessoa {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        Pessoa pessoa = new Pessoa(null);
        // System.out.println("Informe o nome da Pessoa: ");
        // String nome = ler.nextLine();
        pessoa.setNome("João Marcos");
        
        Funcionario funcionario = new Funcionario(pessoa.getNome(), "1215484456", "1215488752");

        funcionario.imprimirPessoa(); // Usando o metodo imprimir pra printar os valores
        funcionario.verificaInstancia(funcionario); //Utilizando o metodo criado pra verificar a classe
    }
}