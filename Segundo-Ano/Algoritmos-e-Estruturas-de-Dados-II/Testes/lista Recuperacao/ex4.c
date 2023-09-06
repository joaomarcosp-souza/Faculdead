#include <stdio.h>
#include <string.h>

struct Carro
{
    char modelo[50];
    int ano;
    float preco;
    char placa[8];
};

int carroBarato(struct Carro carros[], int qtdeCarros)
{
    int carroMaisBarato = 0;
    float menorPreco = carros[0].preco;

    for (int i = 1; i < qtdeCarros; i++)
    {
        if (carros[i].preco < menorPreco)
        {
            menorPreco = carros[i].preco;
            carroMaisBarato = i;
        }
    }

    return carroMaisBarato;
}

int main()
{
    struct Carro carros[30];

    printf("Informe a quantidade de carros (até 30): ");
    int qtdeCarros;
    scanf("%d", &qtdeCarros);

    for (int i = 0; i < qtdeCarros; i++)
    {
        printf("Informe o modelo do %dº carro: ", i + 1);
        scanf("%s", carros[i].modelo);

        printf("Informe o ano de fabricação do modelo %s: ", carros[i].modelo);
        scanf("%d", &carros[i].ano);

        printf("Informe o preço do modelo %s: ", carros[i].modelo);
        scanf("%f", &carros[i].preco);

        printf("Informe a placa do modelo %s (formato XXX-9999): ", carros[i].modelo);
        scanf("%s", carros[i].placa);
    }

    int maisBarato = carroBarato(carros, qtdeCarros);

    printf("O carro mais barato é o modelo %s, fabricado em %d.\n", carros[maisBarato].modelo, carros[maisBarato].ano);

    return 0;
}
