package Principal;

public class Jogadores {
    protected String nome;
    protected int idade;

    public Jogadores(String nome, int idade){
        this.nome = nome;
        this.idade = idade;
    }

    //Metodo para imprimir os atributos do jogador
    public void imprimirJogador(){}

    // GETS e SETS
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    };

    
}
