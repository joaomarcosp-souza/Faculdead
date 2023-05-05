package Principal;

public final class Ponteiro extends Jogadores{
    private double altura;

    public Ponteiro(String nome, int idade, double altura) {
        super(nome, idade);
        this.altura = altura;
    }

    // 
    public void imprimirJogador(){
        System.out.printf("Nome: %s \n Idade: %i \n Altura: %.2f", nome, idade, altura);
    }

    // GETS e SETS
    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }
    
    
}
