package exercicio01;

public class CalculadoraFinanceira extends Calculadora{

    public double calcularJuros(double capital, double taxa, double tempo) {
        return capital * taxa * tempo;
    }

    public double calcularJurosCompostos(double capital, double taxa, double tempo) {
        return capital * Math.pow(1 + taxa, tempo) - capital;
    }

    
}
