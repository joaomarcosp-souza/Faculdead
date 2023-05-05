package exercicio_01;

public class Funcionario {
    double salario_Base;
    double total_de_vendas;
    double salario_final;

    public Funcionario(double salario_Base, double total_de_vendas) {

        this.salario_Base = salario_Base;
        this.total_de_vendas = total_de_vendas;

        if (this.total_de_vendas <= 0) {
            this.salario_final = this.salario_Base - this.total_de_vendas;

        } else if (this.total_de_vendas > 0 && this.total_de_vendas <= 1000) {
            this.salario_final = this.salario_Base + (this.total_de_vendas * 0.1);

        } else if (this.total_de_vendas > 1000 && this.total_de_vendas <= 2000) {
            this.salario_final = this.salario_Base + (this.total_de_vendas * 0.15);

        } else if (this.total_de_vendas > 2000) {
            this.salario_final = this.salario_Base + (this.total_de_vendas * 0.2);
        }
    }

    public void imprimirAtributos() {
        System.out.println(String.format("Salário Base: %.2f\nTotal Vendas: %.2f\nSalário Final: %.2f", salario_Base,
                total_de_vendas, salario_final));
    }

}
