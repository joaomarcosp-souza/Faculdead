package ClasseReservas;

import java.time.LocalDateTime;

import ClassesInformacoes.Pessoa;

public class Reserva extends Armario {
    private LocalDateTime dataHoraDevoculacao;
    private LocalDateTime HoraEmprestimo;
    private Pessoa pessoa;

    public Reserva(String numero, boolean ativo, String observacoes, Reserva reserva,
            LocalDateTime dataHoraDevoculacao,
            LocalDateTime horaEmprestimo, Pessoa pessoa) {
        super(numero, ativo, observacoes, reserva);
        this.dataHoraDevoculacao = dataHoraDevoculacao;
        HoraEmprestimo = horaEmprestimo;
        this.pessoa = pessoa;
    }

    public void imprimirDados() {
        System.out.printf("Número Armario: %s");
        System.out.println("Data Devolução: " + dataHoraDevoculacao);
        System.out.println("Hora Emprestimo: " + HoraEmprestimo);
        System.out.println("Pessoa: " + pessoa);
    }

    public LocalDateTime getDataHoraDevoculacao() {
        return dataHoraDevoculacao;
    }

    public void setDataHoraDevoculacao(LocalDateTime dataHoraDevoculacao) {
        this.dataHoraDevoculacao = dataHoraDevoculacao;
    }

    public LocalDateTime getHoraEmprestimo() {
        return HoraEmprestimo;
    }

    public void setHoraEmprestimo(LocalDateTime horaEmprestimo) {
        HoraEmprestimo = horaEmprestimo;
    }

    public Pessoa getPessoa() {
        return pessoa;
    }

    public void setPessoa(Pessoa pessoa) {
        this.pessoa = pessoa;
    }

}
