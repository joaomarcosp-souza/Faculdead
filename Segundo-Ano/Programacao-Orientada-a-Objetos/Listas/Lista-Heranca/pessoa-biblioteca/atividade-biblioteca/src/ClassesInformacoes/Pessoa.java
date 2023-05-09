package ClassesInformacoes;

import java.util.Date;

import ClasseReservas.Reserva;

public class Pessoa {
    protected String nome;
    protected String email;
    protected String telefone;
    protected String senha;
    protected boolean ativo = true;
    protected Date dataAtuzalizacao;
    protected Date dataCriacao; 
    protected Reserva reserva;

    public Pessoa(String nome,String email, String telefone, String senha, 
        boolean ativo, Date dataAtuzalizacao, Date dataCriacao, Reserva reserva){
            this.nome = nome;
            this.email = email;
            this.telefone = telefone;
            this.senha = senha;
            this.ativo = ativo;
            this.dataAtuzalizacao = dataAtuzalizacao;
            this.dataCriacao = dataCriacao;
            this.reserva = reserva;
    }   

    //Metodo PARA IMPRIMIR
    public void imprimirDados(){}

    
}
