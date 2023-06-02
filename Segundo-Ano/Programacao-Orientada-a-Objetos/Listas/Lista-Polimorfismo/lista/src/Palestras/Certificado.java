package Palestras;

public class Certificado {
    int livro;
    int folha;
    int pagina;
    int numeroDoCertificado;

    public Certificado(int livro, int folha, int pagina, int numeroDoCertificado) {
        this.livro = livro;
        this.folha = folha;
        this.pagina = pagina;
        this.numeroDoCertificado = numeroDoCertificado;
    }

    public void ImprimirDados(){
        System.out.println("Informações Certificado: \n");
        System.out.println("Livro: " + this.livro);
        System.out.println("Folha: " + this.folha);
        System.out.println("Página: " + this.pagina);
        System.out.println("Número do Certificado: " + this.numeroDoCertificado);

    }

    public int getLivro() {
        return livro;
    }
    public void setLivro(int livro) {
        this.livro = livro;
    }
    public int getFolha() {
        return folha;
    }
    public void setFolha(int folha) {
        this.folha = folha;
    }
    public int getPagina() {
        return pagina;
    }
    public void setPagina(int pagina) {
        this.pagina = pagina;
    }
    public int getNumeroDoCertificado() {
        return numeroDoCertificado;
    }
    public void setNumeroDoCertificado(int numeroDoCertificado) {
        this.numeroDoCertificado = numeroDoCertificado;
    }

    
}
