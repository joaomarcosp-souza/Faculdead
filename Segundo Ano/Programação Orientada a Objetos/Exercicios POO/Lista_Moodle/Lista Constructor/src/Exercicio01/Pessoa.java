package Exercicio01;

import java.time.LocalDate;
import java.time.ZoneId;
import java.util.Date;

public class Pessoa {
    int diaNascimento, mesNascimento, anoNascimento, idade;
    Date date = new Date();

    public Pessoa(int diaNascimento, int mesNascimento, int anoNascimento) {

        this.diaNascimento = diaNascimento;
        this.mesNascimento = mesNascimento;
        this.anoNascimento = anoNascimento;

        LocalDate localDate = date.toInstant()
                .atZone(ZoneId.systemDefault())
                .toLocalDate();

        int ano = localDate.getYear();
        int mes = localDate.getMonthValue();
        int dia = localDate.getDayOfMonth();

        while(diaNascimento > 31 || diaNascimento < 1 || mesNascimento > 12 || mesNascimento < 1 || anoNascimento < 1900 || anoNascimento > ano){

        }

        this.idade = ano;
        idade -= anoNascimento;
        if (mesNascimento > mes || (mesNascimento == mes && diaNascimento > dia)) {
            idade--;
        }
    }

}
