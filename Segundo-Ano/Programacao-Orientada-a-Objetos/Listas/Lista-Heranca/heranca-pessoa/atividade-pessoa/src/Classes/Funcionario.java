package Classes;

public final class Funcionario extends PessoaFisica{
    private String cartao;

    public Funcionario(String nome, String rg, String cartao){
        super(nome, rg);
        this.cartao = cartao;
    }

    public void imprimirPessoa() {
        System.out.println("Nome: " + nome);
        System.out.println("Rg: " + rg);
        System.out.println("Cartão: " + cartao);
        System.out.println("Este Objeto pertence à classe: " + this.getClass().getName());
    };

    public void verificaInstancia(Object obj){
        if(obj instanceof Pessoa){ // instanceof e usado para verficiar a qual objeto a classe está instaciada
            System.out.println("Está classe é uma instacia da classe Pessoa");
        };

        if(obj instanceof PessoaFisica){
            System.out.println("Está classe é uma instacia da classe Pessoa Fisica");
        };

        if(obj instanceof PessoaJuridica){
            System.out.println("Está classe é uma instacia de Pessoa juridica.");
        }
    };

    public String getCartao() {
        return cartao;
    }

    public void setCartao(String cartao) {
        this.cartao = cartao;
    }
}
