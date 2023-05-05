public class Carro {
    String cor, sentido;
    int porta, portas, velocidade;
    boolean ligado;


    public void acelerar(){
        if (ligado) {
            velocidade++;
            System.out.println("Carro acelerando..." + velocidade);
        }else{
            System.out.println("Carro Desligado");
        }
    }

    public void frear(){
        if (velocidade > 0) {
            velocidade--;
            System.out.println("O carro está freando..." + velocidade);
        } else {
            System.out.println("Carro já está parado.");
        }
    }

    public void engatarRe() {
        if (velocidade == 0) {
            sentido = "Ré";
            System.out.println("Marcha engatada: " + sentido);
        } else {
            System.out.println("Não é possível engatar a ré com o carro em movimento.");
        }
    }
    
}


