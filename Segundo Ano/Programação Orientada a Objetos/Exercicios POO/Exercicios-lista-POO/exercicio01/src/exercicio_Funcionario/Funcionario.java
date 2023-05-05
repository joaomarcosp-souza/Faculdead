package exercicio_Funcionario;


public class Funcionario {
    protected double horas_trabalhadas;
    protected double valor_hora;
    protected double salario;


    public Funcionario(double horas_trabalhadas, double valor_hora,double salario){
        this.salario = salario;
        this.horas_trabalhadas = horas_trabalhadas;
        this.valor_hora = valor_hora;
    };

    public double calcularSalario(){
        salario = horas_trabalhadas * valor_hora;
        return salario;
    }

    public double getHoras_trabalhadas() {
        return horas_trabalhadas;
    }

    public void setHoras_trabalhadas(double horas_trabalhadas) {
        this.horas_trabalhadas = horas_trabalhadas;
    }

    public double getValor_hora() {
        return valor_hora;
    }

    public void setValor_hora(double valor_hora) {
        this.valor_hora = valor_hora;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    };

    

}
