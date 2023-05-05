package exercicio02;

public class Estudande {
    double notaUm, notaDois, media;

    public Estudande(double notaUm, double notaDois) {

        this.notaUm = notaUm;
        this.notaDois = notaDois;

        this.media = this.notaUm + this.notaDois / 2.0;
    }
}
