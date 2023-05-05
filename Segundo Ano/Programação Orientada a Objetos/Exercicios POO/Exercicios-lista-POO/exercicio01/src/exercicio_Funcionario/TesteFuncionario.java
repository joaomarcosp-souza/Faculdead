package exercicio_Funcionario;

public class TesteFuncionario {
    public static void main(String[] args) {
        
        Engenheiro engenheiro = new Engenheiro(60,10,1500);
        Gerente gerente = new Gerente(25, 150, 5000);

        double salarioEngenheiro = engenheiro.calcularSalario();
        double salarioGerente = gerente.calcularSalario();

        System.out.printf("Salario Engeheiro = %.2f\n Salario Gerente = %.2f", salarioEngenheiro, salarioGerente);
    
    }
}
