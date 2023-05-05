package Aulas;

public class Pessoa {
    String nome;
    String idade;
    int ano_nascimento;

    public Pessoa() {
        ano_nascimento = 1990;
    }

    public Pessoa(String nome) {
        this(); // chamando o metodo Pessoa
        this.nome = nome; //operador para acessar algo dentro da classe 
        this.log();
    }

    public void log(){
        System.out.println(nome);
        System.out.println(idade);
        System.out.println(ano_nascimento);
    }
}
