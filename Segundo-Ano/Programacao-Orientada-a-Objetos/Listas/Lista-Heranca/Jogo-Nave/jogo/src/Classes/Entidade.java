package Classes;

public class Entidade {
    protected int coordenada_x;
    protected int coordenada_y;
    protected int velocidade;
    
    public Entidade(int coordenada_x, int coordenada_y, int velocidade) {
        this.coordenada_x = coordenada_x;
        this.coordenada_y = coordenada_y;
        this.velocidade = velocidade;
    }

    public int getCoordenada_x() {
        return coordenada_x;
    }

    public void setCoordenada_x(int coordenada_x) {
        this.coordenada_x = coordenada_x;
    }

    public int getCoordenada_y() {
        return coordenada_y;
    }

    public void setCoordenada_y(int coordenada_y) {
        this.coordenada_y = coordenada_y;
    }

    public int getVelocidade() {
        return velocidade;
    }

    public void setVelocidade(int velocidade) {
        this.velocidade = velocidade;
    }

    
}
