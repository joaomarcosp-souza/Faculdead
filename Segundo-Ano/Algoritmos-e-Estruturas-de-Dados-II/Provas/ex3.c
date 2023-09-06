#include <stdio.h>

float atualizarPreco(float *precoAtual, float *aumentoPercentual)
{
    float precoFinal = 0.0;
    precoFinal = *precoAtual + (*precoAtual * (*aumentoPercentual / 100.0));
    return precoFinal;
}

int main()
{
    float precoAtual;
    float aumentoPercentual;
    float precoFinal;

    printf("Informe o preço atual do Produto: ");
    scanf("%f", &precoAtual);

    printf("Informe o aumento Percentual: ");
    scanf("%f", &aumentoPercentual);

    precoFinal = atualizarPreco(&precoAtual, &aumentoPercentual);
    printf("O preço do produto com o aumento fica %.2f\n", precoFinal);

    return 0;
}
