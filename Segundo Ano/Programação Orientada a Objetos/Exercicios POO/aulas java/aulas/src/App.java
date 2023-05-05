public class App {
    public static void main(String[] args){
        int contagem = 0; //Iniciando um objeto
        Carro camaro = new Carro(); // Instanciando um objeto
        camaro.cor = "Preto";
        Anunciante jao = new Anunciante();
        jao.nome = "João";
        System.out.println(jao.nome);
    }
}
