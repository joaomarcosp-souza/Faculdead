#include <stdio.h>

void calcularMedia(float notas[], int tamanhoVetor, float *media)
{
    *media = 0.0;
    float soma = 0;

    for (int i = 0; i < tamanhoVetor; i++)
    {
        soma += notas[i];
    }

    *media = soma / tamanhoVetor;
}

int main()
{
    int tamanhoVetor;
    float mediaFinal;
    float media;

    printf("Quantidade de notas?: ");
    scanf("%d", &tamanhoVetor);

    float notas[tamanhoVetor];

    for (int i = 0; i < tamanhoVetor; i++)
    {
        printf("Informe a %dª nota: ", i + 1);
        scanf("%f", &notas[i]);
    }

    calcularMedia(notas, tamanhoVetor, &media);
    printf("A média final é: %.2f\n", media);

    return 0;
}
