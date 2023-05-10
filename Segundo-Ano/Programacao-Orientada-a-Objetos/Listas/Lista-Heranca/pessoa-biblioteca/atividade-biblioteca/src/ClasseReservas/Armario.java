package ClasseReservas;

public class Armario {
    private String numero;
    private boolean ativo;
    private String observacoes;
    private Reserva reserva;

    public Armario(String numero, boolean ativo, String observacoes, Reserva reserva) {
        this.numero = numero;
        this.ativo = ativo;
        this.observacoes = observacoes;
        this.reserva = reserva;
    }

    public void imprimirDados(){
        System.out.printf("Número Armario: %s");
        System.out.println("Ativo: " + ativo);
        System.out.printf("Obeservações: %s \n Reserva: %s", observacoes, reserva);
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public boolean isAtivo() {
        return ativo;
    }

    public void setAtivo(boolean ativo) {
        this.ativo = ativo;
    }

    public String getObservacoes() {
        return observacoes;
    }

    public void setObservacoes(String observacoes) {
        this.observacoes = observacoes;
    }

    public Reserva getReserva() {
        return reserva;
    }

    public void setReserva(Reserva reserva) {
        this.reserva = reserva;
    }
    
}
