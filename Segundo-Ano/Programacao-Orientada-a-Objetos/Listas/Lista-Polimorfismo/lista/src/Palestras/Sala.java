package Palestras;

public class Sala {
    int capacidade;
    String nome;
    String local;

    public Sala(int capacidade, String nome, String local) {
        this.capacidade = capacidade;
        this.nome = nome;
        this.local = local;
    }

    public void ImprimirDados(){
        System.out.println("Informações Sala: \n");
        System.out.println("Capacidade: " + this.capacidade);
        System.out.println("Nome: " + this.nome);
        System.out.println("Local: " + this.local);

    }

    public int getCapacidade() {
        return capacidade;
    }
    public void setCapacidade(int capacidade) {
        this.capacidade = capacidade;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getLocal() {
        return local;
    }
    public void setLocal(String local) {
        this.local = local;
    }
}
