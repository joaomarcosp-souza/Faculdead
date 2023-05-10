package Classes;

public class Projetil extends Entidade{
    private String direcao;

    public Projetil(int coordenada_x, int coordenada_y, int velocidade, String direcao) {
        super(coordenada_x, coordenada_y, velocidade);
        this.direcao = direcao;
    }

    public void movimento(String direcao) {

    }

    public String getDirecao() {
        return direcao;
    }

    public void setDirecao(String direcao) {
        this.direcao = direcao;
    }

}
