package Principal;

// Utilizando o modificador 'final' para que não seja possivel herdar de uma subclasse
public final class Levantador extends Jogadores{
    private int experiencia;

    public Levantador(String nome, final int idade, final int experiencia) {
        super(nome, idade);
        this.experiencia = experiencia;
    }

    public void imprimirJogador() {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("Altura: " + experiencia);
    }

    // Metodo GET
    public int getExperiencia(){
        return experiencia;
    }

    // Metodo SET
    public void setExperiencia(int experiencia){
        this.experiencia = experiencia;
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
