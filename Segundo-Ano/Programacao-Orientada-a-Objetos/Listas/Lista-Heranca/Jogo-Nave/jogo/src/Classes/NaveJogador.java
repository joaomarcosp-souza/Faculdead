package Classes;

public class NaveJogador extends Entidade{
    private int pontuacao;
    private int vidas;

    public NaveJogador(int coordenada_x, int coordenada_y, int velocidade, int pontuacao, int vidas) {
        super(coordenada_x, coordenada_y, velocidade);
        this.pontuacao = pontuacao;
        this.vidas = vidas;
    }

    //
    public void movimento(String string) {
    };

    public void atirar() {
    };

    public boolean verificarColisao(Inimigo inimigo1) {
        return false;
    }

    //
    public int getPontuacao() {
        return pontuacao;
    }

    public void setPontuacao(int pontuacao) {
        this.pontuacao = pontuacao;
    }

    public int getVidas() {
        return vidas;
    }

    public void setVidas(int vidas) {
        this.vidas = vidas;
    }

}
