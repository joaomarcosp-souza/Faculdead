package ClassesInformacoes;

import java.util.Date;

import ClasseReservas.Reserva;

public final class Estudante extends Pessoa{
    private String ra;
    
    public Estudante(String nome, String email, String telefone, String senha, boolean ativo, Date dataAtuzalizacao,
            Date dataCriacao, Reserva reserva, String ra) {
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

    public Date getDataAtuzalizacao() {
        return dataAtuzalizacao;
    }

    public void setDataAtuzalizacao(Date dataAtuzalizacao) {
        this.dataAtuzalizacao = dataAtuzalizacao;
    }

    public Date getDataCriacao() {
        return dataCriacao;
    }

    public void setDataCriacao(Date dataCriacao) {
        this.dataCriacao = dataCriacao;
    };
    
}
