package Principal;

public final class Ponteiro extends Jogadores{
    private double altura;

    public Ponteiro(String nome, int idade, double altura) {
        super(nome, idade);
        this.altura = altura;
    }

    // 
    public void imprimirJogador(){
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("Altura: " + altura);
    }

    // GETS e SETS
    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    // GETS e SETS da super classe
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
