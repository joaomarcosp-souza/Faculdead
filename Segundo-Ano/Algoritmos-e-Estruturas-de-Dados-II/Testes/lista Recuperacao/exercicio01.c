#include <stdio.h>

int soma(int vetor[], int tamanho)
{
    int total = 0;
    for (int i = 0; i < tamanho; i++)
    {
        total += vetor[i];
    }

    return total;
}

int main()
{
    int tamanhoVetor;
    int somaTotal = 0;

    printf("Informe quantos  valores serao somados: ");
    scanf("%d", &tamanhoVetor);

    int vetor[tamanhoVetor];

    for (int i = 0; i < tamanhoVetor; i++)
    {
        printf("Informe o %i valor: ", i + 1);
        scanf("%d ", &vetor[i]);
    }

    somaTotal = soma(vetor, tamanhoVetor);
    printf("%d", somaTotal);

    return 0;
}