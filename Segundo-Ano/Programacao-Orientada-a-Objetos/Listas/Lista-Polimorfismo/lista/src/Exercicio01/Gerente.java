package Exercicio01;
public class Gerente extends Funcionario {
    private double bonificacao = 5.5;

    @Override
    public void calcular_salario() {
        System.out.println("O salário do gerente eh, " + "salario: " + (salario_base * bonificacao));
    }
}
