package Classes;

public class PessoaFisica extends Pessoa{
    protected String rg;
    
    public PessoaFisica(String nome, String rg) {
        super(nome);
        this.rg = rg;
    }

    public void imprimirPessoa() {
        System.out.println("Nome: " + nome);
        System.out.println("Rg: " + rg);
    };

    public String getRg(){
        return rg;
    }

    /*public final String getRg() { // testando o modificador 'Final' que fara com que o metodo não seja sobrescrito por outras subclasses
        return rg;
    }*/

    public void setRg(String rg) {
        this.rg = rg;
    }

}
