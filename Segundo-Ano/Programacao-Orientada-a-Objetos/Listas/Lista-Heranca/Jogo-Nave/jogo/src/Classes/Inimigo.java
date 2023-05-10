package Classes;

public class Inimigo extends Entidade{
    private int pontos_por_inimigo;

    public Inimigo(int coordenada_x, int coordenada_y, int velocidade, int pontos_por_inimigo) {
        super(coordenada_x, coordenada_y, velocidade);
        this.pontos_por_inimigo = pontos_por_inimigo;
    }

    public void movimento_inimigo(String direcao){

    };

    public int getPontos_por_inimigo() {
        return pontos_por_inimigo;
    }

    public void setPontos_por_inimigo(int pontos_por_inimigo) {
        this.pontos_por_inimigo = pontos_por_inimigo;
    }

    public boolean verificarColisao(Projetil projetil1) {
        return false;
    }
    
}
