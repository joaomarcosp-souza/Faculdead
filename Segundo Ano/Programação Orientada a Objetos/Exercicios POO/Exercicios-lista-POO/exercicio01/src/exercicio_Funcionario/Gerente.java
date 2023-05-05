package exercicio_Funcionario;


public class Gerente extends Funcionario{

    private double gerenteBonus = 1.1;

    public Gerente(double horas_trabalhadas, double valor_hora, double salario) {
        super(horas_trabalhadas, valor_hora, salario);
    }

    @Override //classe usada para sobescrever um metodo da classe mae
    public double calcularSalario(){
        double salario = super.calcularSalario();
        return salario + gerenteBonus;
    };
}
