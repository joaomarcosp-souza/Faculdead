package exercicio_01;

import java.util.Scanner;

public class TesteFuncionario {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        System.out.println("Informe o Sálario Base: ");
        double salario_Base = ler.nextDouble();
        
        System.out.println("Tota de Vendas: ");
        double total_de_vendas = ler.nextDouble();
        
        Funcionario funcionario = new Funcionario(salario_Base, total_de_vendas);

        funcionario.imprimirAtributos();

    }
}
