#include <stdio.h>

void media(float vetor[], int qtdeVenda, float *media)
{
    *media = 0;
    for (int i = 0; i < qtdeVenda; i++)
    {
        *media += vetor[i];
    }
    *media = *media / qtdeVenda;
}

void acharMaior(float vetor[], int qtdeVenda, float *maior)
{
    *maior = 0;
    for (int i = 0; i < qtdeVenda; i++)
    {
        if (vetor[i] > *maior)
        {
            *maior = vetor[i];
        }
    }
}

int main()
{
    float vetor[] = {12.5, 50, 63, 85};
    int qtdeVendas = 4;
    float maiorVenda;
    float mediaVenda;

    media(vetor, qtdeVendas, &mediaVenda);
    acharMaior(vetor, qtdeVendas, &maiorVenda);

    printf("Media das Vendas: %f", mediaVenda);
    printf("Maior Venda %f", maiorVenda);

    return 0;
}