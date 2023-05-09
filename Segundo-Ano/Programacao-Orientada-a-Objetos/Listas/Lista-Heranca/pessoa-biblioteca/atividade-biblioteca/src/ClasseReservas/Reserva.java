package ClasseReservas;

import java.util.Date;

public class Reserva extends Armario{
    private Date dataHoraDevoculacao;
    private Date HoraEmprestimo;
    private Armario armario;

    

    public Reserva(String numero, boolean ativo, String observacoes, Date dataHoraDevoculacao, Date horaEmprestimo,
            Armario armario) {
        super(numero, ativo, observacoes);
        this.dataHoraDevoculacao = dataHoraDevoculacao;
        HoraEmprestimo = horaEmprestimo;
        this.armario = armario;
    }

    public void imprimirReserva(){};

    public Date getDataHoraDevoculacao() {
        return dataHoraDevoculacao;
    }

    public void setDataHoraDevoculacao(Date dataHoraDevoculacao) {
        this.dataHoraDevoculacao = dataHoraDevoculacao;
    }

    public Date getHoraEmprestimo() {
        return HoraEmprestimo;
    }

    public void setHoraEmprestimo(Date horaEmprestimo) {
        HoraEmprestimo = horaEmprestimo;
    }

    public Armario getArmario() {
        return armario;
    }

    public void setArmario(Armario armario) {
        this.armario = armario;
    }

    
}
