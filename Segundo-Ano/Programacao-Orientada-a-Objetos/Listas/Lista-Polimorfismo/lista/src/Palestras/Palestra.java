package Palestras;

import java.util.Date;

public class Palestra {
    String tema;
    Date diaHora;
    boolean exigeFrequencia;
    
    public Palestra(String tema, Date diaHora, boolean exigeFrequencia) {
        this.tema = tema;
        this.diaHora = diaHora;
        this.exigeFrequencia = exigeFrequencia;
    }

    public String getTema() {
        return tema;
    }
    public void setTema(String tema) {
        this.tema = tema;
    }
    public Date getDiaHora() {
        return diaHora;
    }
    public void setDiaHora(Date diaHora) {
        this.diaHora = diaHora;
    }
    public boolean isExigeFrequencia() {
        return exigeFrequencia;
    }
    public void setExigeFrequencia(boolean exigeFrequencia) {
        this.exigeFrequencia = exigeFrequencia;
    }
}
