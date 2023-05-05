package exercicio_Funcionario;


public class Engenheiro extends Funcionario{

    private double engenheiroBonus = 0.2;

    public Engenheiro(double horas_trabalhadas, double valor_hora, double salario) {
        super(horas_trabalhadas, valor_hora, salario);
    }

    @Override
    public double calcularSalario(){
        double salario = super.calcularSalario();
        return salario + engenheiroBonus;
    };
    
}
