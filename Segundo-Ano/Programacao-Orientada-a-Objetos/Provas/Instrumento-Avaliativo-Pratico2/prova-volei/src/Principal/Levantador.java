package Principal;

// Utilizando o modificador 'final' para que não seja possivel herdar de uma subclasse
public final class Levantador extends Jogadores{
    private int experiencia;

    public Levantador(String nome, final int idade, final int experiencia) {
        super(nome, idade);
        this.experiencia = experiencia;
    }

    public void imprimirJogador() {
        System.out.printf("Nome: %s \n Idade: %i \n Altura: %.2f", nome, idade, experiencia);
    }

    // Metodo GET
    public int getExperiencia(){
        return experiencia;
    }

    // Metodo SET
    public void setExperiencia(int experiencia){
        this.experiencia = experiencia;
    }

}
