package ClassesInformacoes;

import java.time.LocalDateTime;

import ClasseReservas.Reserva;

public final class Bibliotecario extends Pessoa {
    private String siape;

    public Bibliotecario(String nome, String email, String telefone, String senha, boolean ativo,
            LocalDateTime dataAtuzalizacao,
            LocalDateTime dataCriacao, Reserva reserva, String siape) {
        super(nome, email, telefone, senha, ativo, dataAtuzalizacao, dataCriacao, reserva);
        this.siape = siape;
    }

    public void imprimirDados() {
        System.out.printf("Nome: %s\n E-mail: %s \n Telefone: %s \n Senha: %s \n Siape: %s", nome, email, telefone,
                senha, siape);
        System.out.println("Ativo: " + ativo);
        System.out.println("Data :" + dataAtuzalizacao);
    }

    //
    public String getSiape() {
        return siape;
    }

    public void setSiape(String siape) {
        this.siape = siape;
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

    public LocalDateTime getDataAtuzalizacao() {
        return dataAtuzalizacao;
    }

    public void setDataAtuzalizacao(LocalDateTime dataAtuzalizacao) {
        this.dataAtuzalizacao = dataAtuzalizacao;
    }

    public LocalDateTime getDataCriacao() {
        return dataCriacao;
    }

    public void setDataCriacao(LocalDateTime dataCriacao) {
        this.dataCriacao = dataCriacao;
    };

}
