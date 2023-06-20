package Palestras;

import java.util.Date;

public class Palestra {
    String tema;
    String diaHora;
    boolean exigeFrequencia;
    
    public Palestra(String tema, String diaHora, boolean exigeFrequencia) {
        this.tema = tema;
        this.diaHora = diaHora;
        this.exigeFrequencia = exigeFrequencia;
    }

    public void ImprimirDados() {
        System.out.println("Informações Palestra: \n");
        System.out.println("Tema: " + this.tema);
        System.out.println("Dia e Hora: " + this.diaHora);
        System.out.println("Exige frequencia: " + this.exigeFrequencia);
    }

    public String getTema() {
        return tema;
    }
    public void setTema(String tema) {
        this.tema = tema;
    }
    public String getDiaHora() {
        return diaHora;
    }
    public void setDiaHora(String diaHora) {
        this.diaHora = diaHora;
    }
    public boolean isExigeFrequencia() {
        return exigeFrequencia;
    }
    public void setExigeFrequencia(boolean exigeFrequencia) {
        this.exigeFrequencia = exigeFrequencia;
    }
}
