package Exercicio02;

public class TrocaTroca {
    public int num1 = 5;
    public int num2 = 8;

    public static void main(String[] args) {
        TrocaTroca tro = new TrocaTroca();
        System.out.println("Original: " + tro.num1 + " " + tro.num2);

        // Chama o método de troca de número
        tro.trocaNumero(tro.num1, tro.num2);
    }

    public void trocaNumero(int numA, int numB) {
        int temp = numA;
        numA = numB;
        numB = temp;

        System.out.println("Números trocados: " + numA + " " + numB);
    }
}
