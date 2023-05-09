package Classes;

public final class PessoaJuridica extends Pessoa{
    private String cnpj;

    public PessoaJuridica(String nome, String cnpj){
        super(nome);   
        this.cnpj = cnpj; 
    }

    public void imprimirPessoa() {
        System.out.println("Nome: " + nome);
        System.out.println("CNPJ: " + cnpj);
    };

    public String getCnpj() {
        return cnpj;
    }

    public void setCnpj(String cnpj) {
        this.cnpj = cnpj;
    }
}
