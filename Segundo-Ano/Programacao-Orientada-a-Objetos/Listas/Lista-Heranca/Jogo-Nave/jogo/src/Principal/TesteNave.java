package Principal;

import java.util.Scanner;

import Classes.Inimigo;
import Classes.NaveJogador;
import Classes.Projetil;

public class TesteNave {
    public static void main(String[] args) {
        try (Scanner ler = new Scanner(System.in)) {
            NaveJogador naveJogador = new NaveJogador(0, 0, 5, 0, 3);
            Inimigo inimigo = new Inimigo(0, 5, 3, 100);
            Projetil projetil = new Projetil(0, 0, 0, null);

            boolean rodando = true;
            while (rodando) {
                System.out
                        .println("Pressione as teclas W, A, S ou D para mover a nave, e a tecla espaço para disparar.");
                String input = ler.nextLine();

                if (input.equalsIgnoreCase("w")) {
                    naveJogador.movimento("cima");
                } else if (input.equalsIgnoreCase("a")) {
                    naveJogador.movimento("esquerda");
                } else if (input.equalsIgnoreCase("s")) {
                    naveJogador.movimento("baixo");
                } else if (input.equalsIgnoreCase("d")) {
                    naveJogador.movimento("direita");
                } else if (input.equalsIgnoreCase(" ")) {
                    naveJogador.atirar();
                }

                inimigo.movimento_inimigo(input);
                projetil.movimento(input);

                if (naveJogador.verificarColisao(inimigo)) {
                    rodando = false;
                }

                if (inimigo.verificarColisao(projetil)) {
                }

                if (naveJogador.getVidas() <= 0) {
                    rodando = false;
                }

                renderizarJogo(naveJogador, inimigo, projetil);

                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    private static void renderizarJogo(NaveJogador jogador, Inimigo inimigo, Projetil projetil) {
    }
}
