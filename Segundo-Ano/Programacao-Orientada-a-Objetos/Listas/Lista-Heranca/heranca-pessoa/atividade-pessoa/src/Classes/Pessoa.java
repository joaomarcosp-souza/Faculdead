package Classes;

public class Pessoa {
    protected String nome;

    public Pessoa(String nome){
        this.nome = nome;
    }

    public void imprimirPessoa(){};

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

}
