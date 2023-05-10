package ClassesInformacoes;

import java.time.LocalDate;
import java.util.Date;

import ClasseReservas.Reserva;

public final class Estudante extends Pessoa{
    private String ra;
    
    public Estudante(String nome, String email, String telefone, String senha, boolean ativo, 
            LocalDate dataAtuzalizacao,
            LocalDate dataCriacao, Reserva reserva, String ra) {
        super(nome, email, telefone, senha, ativo, dataAtuzalizacao, dataCriacao, reserva);
        this.ra = ra;
    }

    public void imprimirDados() {
        System.out.printf("Nome: %s \nE-mail: %s \nTelefone: %s \nSenha: %s \nRA: %s", nome, email, telefone, senha, ra);
        System.out.println("Ativo: " + ativo);
        System.out.println("Data :" + dataAtuzalizacao);
    }


    public String getRa() {
        return ra;
    }

    public void setRa(String ra) {
        this.ra = ra;
    }

    // GERAÇÃO DOS GETTERS E SETTERS DA SUPERCLASSE
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public boolean isAtivo() {
        return ativo;
    }

    public void setAtivo(boolean ativo) {
        this.ativo = ativo;
    }

    public LocalDate getDataAtuzalizacao() {
        return dataAtuzalizacao;
    }

    public void setDataAtuzalizacao(LocalDate dataAtuzalizacao) {
        this.dataAtuzalizacao = dataAtuzalizacao;
    }

    public LocalDate getDataCriacao() {
        return dataCriacao;
    }

    public void setDataCriacao(LocalDate dataCriacao) {
        this.dataCriacao = dataCriacao;
    };
    
}
